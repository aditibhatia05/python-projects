# main_daily.py

from email_topic_of_the_day import get_topic_of_the_day

INPUT_GSHEET_NAME = 'trending-topics'
TARGET_GSHEET_NAME = 'trending-topics-done'
EMAIL_GSHEET_NAME = 'email-list'

def main():

    get_topic_of_the_day(INPUT_GSHEET_NAME, TARGET_GSHEET_NAME, EMAIL_GSHEET_NAME, 'Email Sheet')

if __name__ == "__main__":
    main()
