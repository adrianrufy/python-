import datetime as dt
import random
import pandas as pd
import smtplib
email = ""
email_saya = ""
password = ""            
waktu = dt.datetime.now()
waktu_skrg=(waktu.hour, waktu.minute)


data = pd.read_csv("data.csv")
dicti= data.to_dict()


new_dict={(data_row["hour"] , data_row["minute"]): data_row for(index, data_row) in data.iterrows()}


if waktu_skrg in (new_dict):
    with open("surat_buat_pio.txt") as f:
        contents = f.read()
        contents = contents.replace("[NAME]","pio")

        with open("quotes.txt.txt","r") as f:
            data = f.readlines()
            hasil = [line.strip() for line in data]
    
            acak = random.choice(hasil)
            
            contents = contents.replace("[quotes]",acak)
           
            with smtplib.SMTP("smtp.gmail.com") as koneksi:
                    koneksi.starttls()
                    koneksi.login(email_saya, password)
                    koneksi.sendmail(from_addr=email_saya, to_addrs=email, msg=contents)
                    koneksi.close()


