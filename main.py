"""
Developed By Aziz Kaplan
aziz.kaplan@infinitumit.com.tr
"""
import time,subprocess,os
from colors import *

print(colors["BOLD"]+colors["GOLD"]+"|==============================================================================|")
print(colors["BOLD"]+colors["GOLD"]+"|=========" + "Log İmzalayıcı".center(60) + "=========|")
print(colors["BOLD"]+colors["GOLD"]+"|=========" + "5651 Sayılı Kanuna Uygun Olarak Hazırlanmıştır".center(60) + "=========|")
print(colors["BOLD"]+colors["GOLD"]+"|=========" + "Güncel versiyon v0.0.1".center(60) + "=========|")
print(colors["BOLD"]+colors["GOLD"]+"|=========" + " ".center(60) + "=========|")
user_info = "Aziz Kaplan Tarafından Geliştirilmiştir."
print(colors["BOLD"]+colors["GOLD"]+"|=========" + user_info.center(60) + "=========|")
dev_info = "Tavsiye/Yardım: aziz.kaplan@infinitumit.com.tr"
print(colors["BOLD"]+colors["GOLD"]+"|=========" + dev_info.center(60) + "=========|")
print(colors["BOLD"]+colors["GOLD"]+"|=========" + "Lisans bilgisi için LİSANS'a bakın".center(60) + "=========|")
print(colors["BOLD"]+colors["GOLD"]+"|==============================================================================|") 

FirstTime=False
mark = 'RUN'
if not os.path.exists(mark):
    FirstTime=True
    print("This script is being run for the first time.")
    with open(mark, 'w') as f:
        f.write("This marker file indicates that the script has been run.")
else:
    with open("LOGPATH","r",encoding="utf-8") as LOGPATH:
        LOGPATH=LOGPATH.read()

if FirstTime==True:
    selection="\n"+colors["RED"]+"["+colors["YELLOW"]+"+"+colors["RED"]+"]"+colors["DRGREEN"]+"Logların Bulunduğu Dizini Girin[Örn: /var/log/]:\n\n"+colors["BOLD"]+colors["GOLD"]+subprocess.check_output("hostname",shell=True).decode().strip()+colors["FAIL"]+"@"+colors["YELLOW"]+subprocess.check_output("whoami",shell=True).decode().strip()+colors["RED"]+"["+colors["END"]+"~"+colors["RED"]+"]"+colors["END"]
    LOGPATH=input(selection)
    createFile_LogSignatures="mkdir /var/log/LogSignatures"
    createFile_Signed="mkdir /var/log/LogSignatures/Signed"
    signaturedFilePath="/var/log/LogSignatures/Signed/"

    subprocess.call(createFile_LogSignatures,shell=True)
    subprocess.call(createFile_Signed,shell=True)

    with open("LOGPATH","w",encoding="utf-8") as f:
        f.write(LOGPATH)



if __name__ == "__main__":
    logFileList=subprocess.check_output("ls "+LOGPATH+"*.log",shell=True).decode().strip()
    logFileList=logFileList.split("\n")
    for logfile in logFileList:
        with open(logfile,"r",encoding="utf-8") as signatured:
            subprocess.call("bash signatureverify.sh sign "+logfile+" ssl/private_key.pem <ssl_pass_phrase>",shell=True)
