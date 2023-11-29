#Ferramenta simples para buscar e Printar E-mail registrados em Sites.
#Para Rodar o codigo, não se esqueça de baixar as bibliotecas importada no codigo.
import requests
import re
import time

def GetEmailBySite(SiteList):
    for i in SiteList:
        DataSite = Requests.get(i)
        ReturnRegex = re.findall(f'[\w\.-]+@[\w\.-]+\.\w+',DataSite.text)
        if ReturnRegex:
            return(list(set(ReturnRegex)))
        else:
            return None
        
sites = ["https://www.ev.org.br"]

cont_x=0

try:
    for x in sites:
        mails = (GetEmailBySite([x]))
        if (mails != "None" or mails != None):
            print (mails)
        cont_x = cont_x+1
except:
    print (x)
    pass
