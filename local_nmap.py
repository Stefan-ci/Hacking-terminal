#! user/bin/env python

import os
import nmap
import socket

#For styling
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format



def Nmap(IP):
      cprint(figlet_format('         nmap'), "red")
      port = str(input('Enter ports (ex: "22-444" or "80-1224",...)\n>>>Port: '))
      cprint('Scanning...', 'blue')
      nm = nmap.PortScanner()
      nm.scan(IP, port)
      print('[+] all hosts: ')
      print(nm.all_hosts())
      print('\n[+] list of all hostnames')
      print(nm[IP].hostnames()) 
      for host in nm.all_hosts():
         cprint(' ==============================================', 'green')
         print('Host : %s (%s)' % (host, nm[host].hostname()))
         print('State : %s' % nm[host].state())
         for proto in nm[host].all_protocols():
            cprint('            ==================', 'green')
            print('Protocol : %s' % proto)
            lport = sorted(nm[host][proto].keys())
            lport.sort()
            for port in lport:
               print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
 
                                                               
if __name__=='__main__':
   main()
