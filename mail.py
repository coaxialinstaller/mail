import smtplib
from email import message
import gnupg

def encrypt_message(pub_key_path, msg):
    gpg = gnupg.GPG()

    with open(pub_key_path) as pub:
        key_data = pub.read()

    pub_key_result = gpg.import_keys(key_data)

    if pub_key_result.count == 0:
        print('Error: no keys found in keyring')
        return 0
    else:
        key_fingerprint = pub_key_result.fingerprints[0]

    return str(gpg.encrypt(msg, key_fingerprint, always_trust=True))


def send_mail(msg, subject, reciver):
    smtp_server = "smtp.office365.com"
    smtp_port = 587

    sender = ""
    sender_passwd = ""

    mail = message.Message()
    mail.add_header("from", sender)
    mail.add_header("to", reciver)
    mail.add_header("subject", subject)
    mail.set_payload(msg)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(sender, sender_passwd)
    server.sendmail(sender, reciver, mail.as_string())
