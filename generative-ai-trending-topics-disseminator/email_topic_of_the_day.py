
# email_topic_of_the_day.py


from gcp_helper import write_in_gsheet, read_from_gsheet, check_if_wsheet_present, access_secret_version
from vertex_ai_text_generator import ask_bard_explanation
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
import re


def send_email(subject, text, to_email, to_name):
    # Configure API key authorization: api-key
    configuration = sib_api_v3_sdk.Configuration()
    api_key = access_secret_version("email-api-key") 
    configuration.api_key['api-key'] = api_key

    # create an instance of the API class
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"name": to_name, "email": to_email}],
        sender={"name": "Aditi Bhatia", "email": "admin@abhinavbhatia.in"},
        subject=subject,
        html_content=text
    )

    try:
        # Send a transactional email
        api_response = api_instance.send_transac_email(send_smtp_email)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)

def format_text(text):
    # Replace each newline character with an HTML line break
    text = text.replace('\n', '<br>')
    # Replace ** with bold tags
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    return text

def get_topic_of_the_day(INPUT_GSHEET_NAME, TARGET_GSHEET_NAME, EMAIL_GSHEET_NAME, email_worksheet):

    users_details = check_if_wsheet_present(EMAIL_GSHEET_NAME, email_worksheet)
    if users_details:
        # Iterate over all users and send emails according to their topic preferences
        unique_topics = list(set(row[2] for row in users_details.get_all_values()[1:]))
        for topic_name in unique_topics:
            result = check_if_wsheet_present(TARGET_GSHEET_NAME, topic_name)
            if result is not None:
                target_worksheet = result
                values = target_worksheet.get_all_values()
                data_rows = [term[0] for term in values[1:]]
                random_term = read_from_gsheet(INPUT_GSHEET_NAME, topic_name)[0]
                while random_term in data_rows:
                    random_term = read_from_gsheet(INPUT_GSHEET_NAME, topic_name)[0]
                random_term_list = [random_term]
                write_in_gsheet(TARGET_GSHEET_NAME, topic_name, random_term_list)
                text = ask_bard_explanation(random_term, topic_name)
                text = format_text(text)
                interested_users = [row for row in users_details.get_all_values()[1:] if row[2] == topic_name]
                for user in interested_users:
                    name = user[0]
                    email_id = user[1]
                    send_email(f"Hi {name}, {topic_name} Topic of the Day: {random_term}", text, email_id, name)
            
    else:
        print("Email Sheet not found or empty.")