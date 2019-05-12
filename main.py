# bs link https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# class details http://timetable.unsw.edu.au/2019/COMP4418.html
import time
import random
import requests
from check_enrollment import *
from send_email import *


def main():
    ERROR_INTEVAL = 1 # If connection fails, wait RETRY_INTEVAL in minutes
    CHECK_INTEVAL = 30 # If class is full, wait CHECK_INTEVAL in minutes

    courses = ['COMP4418', 'COMP9444']

    user = 'rjautomatedscript@gmail.com'
    pw = '88004526rj'

    recipients = ['roger.jiang@live.com', 'roger.jiang@health.nsw.gov.au']

    # if there are still courses to be checked
    while len(courses) > 0:
        for course in courses:
            retry = True
            while retry:
                try:
                    if check_enrollment(course):
                        subject = f'Course {course} available for enrollment'
                        body = f'Hurry or you\'re going to miss out!'

                        try:
                            s = SMTPServ(user, pw)
                            for recipient in recipients:
                                s.send_email(recipient, subject, body)
                        finally:
                            s.server.close()
                        courses.remove(course)

                    retry = False

                except smtplib.SMTPException:
                    while retry:
                        time.sleep(ERROR_INTEVAL*60)
                        try:
                            s = SMTPServ(user, pw)
                            for recipient in recipients:
                                s.send_email(recipient, subject, body)
                            retry = False
                        except smtplib.SMTPException:
                            pass
                        finally:
                            s.server.close()

                except requests.exceptions.RequestException as e:
                    print('Check course failed. Exception {e}')
                    time.sleep(ERROR_INTEVAL*60)
        next_check_time = time.strftime('%H:%M:%S', time.localtime(time.time()+ CHECK_INTEVAL*60))
        print(f'No openings, checking again at {next_check_time}')
        time.sleep(CHECK_INTEVAL*60)


# def check_enrollment(course):
#     if random.random() < 0.1:
#         print(f'Hey {course} is available')
#         return True
#     else:
#         print('Better luck next time')
#         return False
#
# class SMTPServ:
#     def __init__(self, user, pw):
#         pass
#
#     def send_email(self, a, b, c):
#         print(f'email sent to {a}!')

if __name__ == '__main__':
    main()
