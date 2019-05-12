# use https://stackoverflow.com/a/12424439


import smtplib

class SMTPserv:
    '''Creates connection to SMTP google server'''
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.server.ehlo()
        self.server.login(user, pwd)

    def send_mail(self, to, subject, body):
        message = f"""From: {self.user}\nTo: {to}\nSubject: {subject}\n\n{body}"""
        self.server.sendmail(self.user, to, message)





# Testing
def main():
    try:
        recipient = 'roger.jiang@live.com'
        subject = 'hi, test 2'
        body = 'some more text...'

        connection = Email('rjautomatedscript@gmail.com', 'rj88004526')
        connection.send_mail(recipient, subject, body)

    finally:
        connection.server.close()

if __name__ == '__main__':
    main()
