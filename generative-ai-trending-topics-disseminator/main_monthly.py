# main_monthly.py

from vertex_ai_text_generator import update_sheet_with_terms
from gcp_helper import check_if_wsheet_present

INPUT_GSHEET_NAME = 'trending-topics'
TARGET_GSHEET_NAME = 'trending-topics-done'
EMAIL_GSHEET_NAME = 'email-list'
email_worksheet = 'Email Sheet'

def main():
    users_details = check_if_wsheet_present(EMAIL_GSHEET_NAME, email_worksheet)
    if users_details:
        # Iterate over all users and send emails according to their topic preferences
        unique_topics = list(set(row[2] for row in users_details.get_all_values()[1:]))
    # Generate and write terms into the sheet
    for unique_topic in unique_topics:
        update_sheet_with_terms(INPUT_GSHEET_NAME, unique_topic)

if __name__ == "__main__":
    main()
