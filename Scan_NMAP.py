''' Essa script simples tem como objetivo, executar o sistema de scanner
de ip (nmap), via codigo Python. A vantagem desse script é a possibilidade
de registrar varios host de uma vez, para serem scaneados. '''
#Não se esqueça de baixar a biblioteca python-nmap para executar o script.

import nmap
 
nmap_scan = nmap.PortScanner()

# Nessa linha, o script faz o scan do google ou do ip de interesse, passando da porta 21 à 80
nmap_scan.scan('8.8.8.8', '21-80')

for host in nmap_scan.all_hosts():
    print('Host : %s (%s)' % (host, nmap-scan[host].hostname()))
    print('state : %s' % nmap_scan[host].state())
    for proto in nmap_scan[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = nmap_scan[host][proto].keys()

        for port in lport:
            print('port : %s\tstate : %s' % (port, nmap_scan[host][proto][port]['state']))
