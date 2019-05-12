# use https://stackoverflow.com/a/12424439


import smtplib

class Email:
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        self.server.ehlo()
        self.server.login(user, pwd)

    def send_mail(self, to, subject, body):
        message = f"""From: {self.user}\nTo: {to}\nSubject: {subject}\n\n{body}"""
        self.server.sendmail(self.user, to, message)
