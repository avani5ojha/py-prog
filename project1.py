import datetime
import os
import webbrowser
import googlesearch
import bs4
#import pycurl
import psutil

choice=int(input("enter choice"))
if choice==1:
    print(datetime.datetime.now().time())
# elif choice==2:
#     os.system("reboot")
elif choice==3:
    userlist=["jack2","mac2","am2"]
    passlist=["jackp","mackp","sackp"]
    # def fun(j):
    #     return(os.system("echo -n "+j+"| sha512sum"))


    for i,j in zip(userlist,passlist):
        os.system("sudo useradd "+i +" -p "+j)
        print("successfully added "+i)
elif choice==4:
    query="shahid kapoor"
    webbrowser.open_new_tab("https://www.google.com/search?q="+query)

elif choice==5:
    # query="adhoc"
    # for j in search(query, tld="co.in", num=10, stop=1, pause=2):
    #         print(j)

    c= pycurl.Curl()
    c.setopt(c.URL, 'http://www.google.co.uk/search?hl=en&q=hello')
    c.perform()

elif choice==6:

   print(psutil.cpu_percent())
   print(psutil.virtual_memory())
   process = psutil.Process(os.getpid())
   print(process.memory_info().rss) #  physical memory usage

elif choice==7:
