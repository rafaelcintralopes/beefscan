# BeEF Scan
# Desenvolvido por Rafael Cintra Lopes
# Site: https://rafaelcintralopes.com.br  |  Email: rafaelcintralopes@gmail.com

import sys
import getopt
import re
import requests
from bs4 import BeautifulSoup
from time import sleep

welcome = """                                                                    

██████╗ ███████╗███████╗███████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔════╝██╔════╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝█████╗  █████╗  █████╗      ███████╗██║     ███████║██╔██╗ ██║
██╔══██╗██╔══╝  ██╔══╝  ██╔══╝      ╚════██║██║     ██╔══██║██║╚██╗██║
██████╔╝███████╗███████╗██║         ███████║╚██████╗██║  ██║██║ ╚████║
╚═════╝ ╚══════╝╚══════╝╚═╝         ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                      
> Desenvolvido por Rafael Cintra Lopes
> Site: https://rafaelcintralopes.com.br  |  Email: rafaelcintralopes@gmail.com

Modo de usar: 
    -u URL

Exemplo: python beefscan.py -u https://google.com

###################################################################################


"""

for char in welcome:
    sleep(0.0010)
    sys.stdout.write(char)
    sys.stdout.flush()

optlist, args = getopt.getopt(sys.argv[1:], 'u:')
for (opcao,argumento) in optlist:
    if opcao == '-u':
        url = argumento

page = requests.get(url)
code = BeautifulSoup(page.text, 'html.parser')
tag = code.find('script')

for script in tag:
    payload = code(text=re.compile(r'hook.js' ))
    if payload:
        print("ALERTA: Este site contém código malicioso!\n\n")
    else:
        print("Este site não contém código malicioso :)\n\n")