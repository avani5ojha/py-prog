
import socket
import nmap
import os

while True:
    print("select any one of the options")
    option=int(input("1.Scan all the ips\n2.send and receice msg\n3.quit"))
    ipaddr=[]
    if option==1:
     nm=nmap.PortScanner()
     a=nm.scan(hosts='192.168.10.*', arguments='-sP')

        # ipaddr=nm.all_hosts()
        # print(ipaddr)
        #print(type(ipaddr))

     for key,value in a['scan'].iteritems():
            if(value['status']['state'])=='up':

                ipaddr.append(value['addresses']['ipv4'] )
     print(ipaddr)


    #print(ipaddr)


    if option==2:
     #creating socket object
     r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
     # own ip address and port no.
     r.bind(("192.168.10.176",8877))
     cip=raw_input("enter ip address")
     while True:

        msg=raw_input("enter msg:")
         # msg_in_bytes=bytes(msg,'utf-8')
        r.sendto(msg,(cip,8877))
         # print(data[1])



        data=r.recvfrom(1000)[0]
        print(data.decode('utf-8'))


    if option==3:
        print("quitting chat program")
        quit()
