import smtplib
import random

import datetime as dt

with open("quotes.txt.txt","r") as f:
    data = f.readlines()
    hasil = [line.strip() for line in data]
    
    acak = random.choice(hasil)
password = "R0m30Un1f0rmF0xtr0tYank33"
skrg = dt.datetime.now()
email = "restu230904trihanteten@gmail.com"
email_saya = "adrianrufy@gmail.com"
email_pio = ""
with smtplib.SMTP("smtp.gmail.com") as koneksi:
    koneksi.starttls()

    koneksi.login(email_saya, password)
    koneksi.sendmail(from_addr=email_saya, to_addrs=email, msg=f"{acak} /n/n selamat menjalani hari sayang {skrg}")
    koneksi.close()