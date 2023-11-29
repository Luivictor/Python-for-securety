'''Esse pequeno script tem como função identificar pelo comando Whois quem é
o operador legal de um site. Apos executar o script, ele fara um scan no dominio
no qual temos interece em analisar.'''

import whois
dominio = raw-input("ALVO: ")
consulta_whois = whois.whois(dominio)

#print consulta whois.name
print consulta_whois.text
