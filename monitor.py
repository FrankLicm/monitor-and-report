import time
import smtplib
from optparse import OptionParser

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
            print("send mail successfully")
        except:
            print("failed to send mail")
            exit(0)

    def monitor(self, target_text, subject=None, sleep_time=3, body=None, max_time=20):
        print("start monitoring...")
        print(self.log_file)
        send_time = 0
        while True:
            flag = 0
            with open(self.log_file, "r") as fin:
                lines = fin.read().split("\n")
                line = lines[-1]
                if target_text in line:
                    flag = 1
                    if body is not None:
                        if subject is not None:
                            self.send(subject, body)
                        else:
                            self.send(line, body)
                    else:
                        if subject is not None:
                            self.send(subject, line)
                        else:
                            self.send(line, line)
                    send_time += 1
            if send_time> max_time:
                exit(0)
            if flag == 0:
                pass
            else:
                time.sleep(sleep_time)


if __name__ == '__main__':
    parser = OptionParser(usage="usage: %prog [options]")
    parser.add_option('--log_file',
                      action='store',
                      dest='log_file',
                      default=None,
                      help='log file path')
    parser.add_option('--smtp_adress',
                      action='store',
                      dest='smtp_adress',
                      default=None,
                      help='smtp adress')
    parser.add_option('--port',
                      action='store',
                      dest='port',
                      default=587,
                      help='smtp port')
    parser.add_option('--user',
                      action='store',
                      dest='user',
                      default=None,
                      help='username')
    parser.add_option('--pwd',
                      action='store',
                      dest='pwd',
                      default=None,
                      help='password')
    parser.add_option('--recipient',
                      action='store',
                      dest='recipient',
                      default=None,
                      help='recipient')
    parser.add_option('--target_text',
                      action='store',
                      dest='target_text',
                      default=None,
                      help='target text')
    parser.add_option('--subject',
                      action='store',
                      dest='subject',
                      default=None,
                      help='subject')
    parser.add_option('--body',
                      action='store',
                      dest='body',
                      default=None,
                      help='body')
    parser.add_option('--sleep_time',
                      action='store',
                      dest='sleep_time',
                      default=3,
                      help='sec')
    parser.add_option('--max_time',
                      action='store',
                      dest='max_time',
                      default=20,
                      help='sec')
    (options, args) = parser.parse_args()
    log_file = options.log_file
    smtp_adress = options.smtp_adress
    port = int(options.port)
    sleep_time = int(options.sleep_time)
    user = options.user
    pwd = options.pwd
    recipient = options.recipient
    target_text = options.target_text
    subject = options.subject
    body = options.body
    max_time = int(options.max_time)
    monitor = Monitor(log_file, smtp_adress, port, user, pwd, recipient)
    monitor.monitor(target_text, subject, sleep_time, body, max_time)


