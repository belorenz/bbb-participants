#!/usr/bin/python3

import argparse
import smtplib
import ssl
from email.mime.text import MIMEText

class MailSender:

    def __init__(self, *args):
        self.args = args[0]


    def send_mail(self, subject,  message):

        context = ssl.create_default_context()
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = self.args.mail_from
        msg['To'] = self.args.mail_to

        with smtplib.SMTP_SSL(host=self.args.host_sender, port=self.args.port_sender,
                              context=context) as server:
            server.login(self.args.login_sender, self.args.password_sender)
            server.sendmail(msg['From'], msg['To'], msg.as_string())


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(
        description=__doc__)
    argparser.add_argument(
        '--message',
        type=str,
        required=True,
        metavar='m',
        help='Message to be send via mail.')
    argparser.add_argument(
        '--subject',
        type=str,
        required=True,
        help='Subject of the mail.')
    argparser.add_argument(
        '--host_sender',
        type=str,
        required=True,
        metavar='H',
        help='Hostname of mail server to send report from.')
    argparser.add_argument(
        '--port_sender',
        type=int,
        default=465,
        metavar='P',
        help='Port of mail server to send report from.')
    argparser.add_argument(
        '--login_sender',
        type=str,
        required=True,
        metavar='l',
        help='Login for email account to send report from.')
    argparser.add_argument(
        '--password_sender',
        type=str,
        required=True,
        metavar='p',
        help='Password for email account to send report from.')
    argparser.add_argument(
        '--mail_to',
        type=str,
        required=True,
        metavar='m',
        help='E-Mail address to send report to.')
    argparser.add_argument(
        '--mail_from',
        type=str,
        required=True,
        metavar='M',
        help='E-Mail address to send report from.')
    args = argparser.parse_args()
    MailSender(args).send_mail(args.subject, args.message)