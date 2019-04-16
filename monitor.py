import time
import smtplib


class Monitor:
    def __init__(self, log_file, smtp_adress, port, user, pwd, recipient):
        self.log_file = log_file
        self.smtp_adress = smtp_adress
        self.port = port
        self.user = user
        self.pwd = pwd
        self.recipient = recipient

    def send(self, subject, body):
        FROM = self.user
        TO = self.recipient if isinstance(self.recipient, list) else [self.recipient]
        SUBJECT = subject
        TEXT = body
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP(self.smtp_adress, self.port)
            server.ehlo()
            server.starttls()
            server.login(self.user, self.pwd)
            server.sendmail(FROM, TO, message)
            server.close()
        except:
            print("failed to send mail")

    def monitor(self, target_text, subject, sleep_time=3, body=None):
        while True:
            with open(self.log_file, "r") as fin:
                lines = fin.read()
                last_10_lines  = lines[-11:len(lines)]
                for line in last_10_lines:
                    if target_text in line:
                        if body is not None:
                            self.send(subject, body)
                        else:
                            self.send(subject, line)

            time.sleep(sleep_time)

if __name__ == '__main__':
    log_file = ""
    smtp_adress = "smtp.gmail.com"
    port = 587
    user = ""
    pwd = ""
    recipient = ""
    target_text = ""
    subject = ""
    monitor = Monitor(log_file, smtp_adress, port, user, pwd, recipient)
    monitor.monitor(target_text, subject)


