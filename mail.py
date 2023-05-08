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
    
    
    
    
    
    
    
    
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from cryptography.fernet import Fernet

# Create your views here.


import requests

url = "http://127.0.0.1:8000"

headers = {'Content-type': 'application/json'}

data = '{"key": "Hej da-pojk!", "body": "bar", "userId": 1}'

test = requests.post(url, data=data, headers=headers)

print(test.text, test.status_code)


@csrf_exempt
def test(request):
    suu = b'gAAAAABkVP99tg0jLEmuN4GfB1Eq-tzriOLGwcI9Y8B1IrCBdF6iCxEdgHXIYSzMWVBUNE-r25Fxn2TCRufKjsmnBOgRJMyzCA=='
    key = b'bTFhhmfaGVyPN36i1k9qtFH-7hA6qUbZRlrmWVrFS_E='
    k = Fernet(key)

    token = k.encrypt(b"Hej da-pojk!")

    print(token)
    if request.method == "POST" and request.headers["Content-Type"] == "application/json":
        print(json.loads(request.body))
        print(json.loads(request.body)["key"])
        print(k.decrypt(suu))
        if k.decrypt(suu).decode("utf-8") == json.loads(request.body)["key"]:
            print("GG!")
            HttpResponse.status_code=200
            return HttpResponse("Good")
        
    
    

    HttpResponse.status_code=404
    return HttpResponse("Sike" + str(HttpResponse.status_code))


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime

        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return f"{self.first_name} {self.last_name}"

    
    
    
    
    
    
    
    ###### SANITIZE PGP PUBLIC KEY ####

        key_data = request.POST["a"]
        goog = key_data.replace("-----BEGIN PGP PUBLIC KEY BLOCK----- ", "").replace("-----END PGP PUBLIC KEY BLOCK-----", "").split()
        x = 0
        while True:
            if len(goog[x]) != 64:
                goog.pop(x)
            else:
                break
        goog.insert(0,"-----BEGIN PGP PUBLIC KEY BLOCK-----")
        goog.insert(1, "")
        goog.append("")
        goog.append("-----END PGP PUBLIC KEY BLOCK-----")
        key_data = "\n".join(goog)
        print(key_data)
