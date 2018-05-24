#!/usr/bin/python
import argparse
import re
import os

def auth_root():
    root = os.getuid()
    if root == 0:
        print('Activating virtualhost')
    else:
        print('You must run as root')

def host(domain):
    file = open('/etc/hosts', 'a')
    domain = file.write("\n"+"127.0.0.1"+"\t\t"+domain)
    print('Configure /etc/hosts adding your custom domain')
    file.close()

def vhost(domain,loc):
    file = open('/opt/lampp/etc/extra/httpd-vhosts.conf', 'a')
    file.write('\n<VirtualHost *:80>\n\tDocumentRoot "/opt/lampp/htdocs/' +loc+'"\n\tServerName '+domain+'\n</VirtualHost>')
    print('Configure httpd-vhosts.conf adding your custom setting')
    file.close()

def main():
    parser = argparse.ArgumentParser(description="Simple Virtualhost in Lampp Linux")
    
    parser.add_argument(
        '-H', 
        '--host', 
        dest="domain", 
        help="Masukan domain virtual kalian"
    )
    parser.add_argument(
        '-l', 
        '--loc', 
        dest="loc", 
        help="Letak folder yang ingin divirtualkan di htdocs"
    )
    args = parser.parse_args()
    auth_root()
    host(args.domain)
    vhost(args.domain, args.loc)
    print('Restarting lampp.....')
    os.system('/opt/lampp/lampp restart')
    print('Configuration successfull :D')
if __name__ == '__main__':
    main()
    
