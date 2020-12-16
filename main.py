#!/usr/bin/python3

#Dependencies
import os
import nmap
import sys
import socket
import time

#Local libs
import local_nmap

#For styling
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

# Animations
for i in range(0, 101):
   time.sleep(0.05)
   charging = 'Charging {}%'.format(str(i))
   cprint(charging, 'green')
   if i >= 100:
      time.sleep(2)
      try:
         os.system('clear')
      except:
         os.system('cls')
      break



creator = '         Stefan'
time.sleep(0.8)
print('\n\n               Welcome in my script. \n                  Created by: ')
time.sleep(1)
cprint(figlet_format(creator), "blue")
cprint('Available commands:\n\n1. pip \n2. nmap or port scanner \n3. ping \n4. exit or ex', 'green')


# Main function to run all
def main():
   user = input('\n$(stef@py3)>> ')   
   if user == '' or user == ' ' or user == '  ':
      print('you entered nothing only "spaces" ')
      main()
   elif user == '3' or user == 'ping':
      host = input('Host to ping: ')
      os.system('ping -c 5 {}'.format(host))
      print('ping 5 times')
      time.sleep(1.5)
      choice = str(input('\n\nWould you like to scan that hostname? (y/n):  '))
      if choice == 'y' or choice == 'Y':
         IP = socket.gethostbyname(host)
         local_nmap.Nmap(IP)
         time.sleep(1)
         cprint('\n\n[+]Finish !', 'red')
         main()
      elif choice == 'N' or choice == 'n':
         cprint('Well scan abortion...\nReturn to home', 'green')
         main()
      else:
         cprint('[!] Choice not recognised \nAbortion...', 'red')
      main()
   elif user == 'pip' or user == '1':
      cprint('Upgrading pip...', 'blue')
      os.system('pip install --upgrade pip')
      main()      
   elif user == 'scann' or user == 'nmap' or user == 'vuln' or user == 'nm' or user == '2': #Wake word to scan
      port_scanner()
      main()
   elif user == '4' or user == 'exit' or user == 'ex':
      sys.exit(1)
   elif user == 'ls':
      os.system('ls')
      main()
   elif user == 'ls -a':
      os.system('ls -a')
      main()
   elif user == 'ls -lh':
      os.system('ls -lh')
      main()
   elif user == 'ls -ls':
      os.system('ls -ls')
      main()
   elif user == 'dir':
      os.system('dir')
      main()
   elif user == 'python3 main.py ' or user == 'python main.py':
      try:
         os.system('python3 main.py')
      except:
         os.sytem('python main.py')
   
   
   
   else:
      print('Sorry, "{}" is not recognised'.format(user))
      main()
   
         
                     
# Scanning with nmap
def port_scanner():
      cprint(figlet_format('         nmap'), "red")
      IP = str(input('>>>Enter IP address: '))
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
