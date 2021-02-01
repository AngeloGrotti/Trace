#Author : Heriberto Ramirez
#Date : 01/15/2021
#Language : Python 3

#scapy sniff for cdp packets

from scapy.all import *
import scapy.all as scapy
import requests
import socket
import time
import getpass

#create function to sniff packets 
def cdpsniff() :

    #decode cdp packets
    scapy.load_contrib('cdp')

    #begin of listen
    print('[+] Listening for CDP packet \n')

    #filter for only 1 cdp packet coming from Ethernet interface where destination mac is .
    cdp_packet = scapy.sniff(iface='Ethernet', filter="ether dst 01:00:0c:cc:cc:cc", count=1)

    #debug info
    #cdp_packet[0].show()

    #grabs info about deivce from cdp packet
    switch_name = cdp_packet[0]['CDPMsgDeviceID'].val.decode() #gets switch name
    ipv4_addr = cdp_packet[0]['CDPAddrRecordIPv4'].addr #gets ipv4 address of switch
    port_id = cdp_packet[0]['Port ID'].iface.decode()   #gets port id in use by pc
    vlan_id = cdp_packet[0]['Native VLAN'].vlan #gets vlan id

    #gets local-pc info
    pc_name  = socket.gethostname()
    pc_ip = socket.gethostbyname(pc_name)
    username = getpass.getuser()

    #prints out variables 
    print('[+] Switch Name :', switch_name)
    print('[+] IPv4 Address :', ipv4_addr)
    print('[+] Port ID :', port_id)
    print('[+] VLAN ID :', vlan_id)
    print('[+] PC Name : ', pc_name)
    print('[+] PC IP : ', pc_ip)
    print('[+] User : ', username)
    print()
    time.sleep(3)
    print('[+] Sending info to webserver...')

    #initiate send function and pass variables
    print(send(switch_name, ipv4_addr, port_id, vlan_id, pc_name, pc_ip, username))

def send(switch_name, ipv4_addr, port_id, vlan_id, pc_name, pc_ip, username) :

    #data to send 
    userdata = {
        'sName':switch_name, 
        'sIp':switch_ip, 
        'pId':port_id, 
        'vId':vlan_id, 
        'pName':pc_name, 
        'pIp':pc_ip, 
        'uName':username 
        }

    #sending data
    response = requests.post('http://<server_address>/<filename>.php', data=userdata)

    #return the response of the webserver in text format (human readable)
    return response.text



#initiate boss program    
cdpsniff()
