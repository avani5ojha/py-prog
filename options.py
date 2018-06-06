import cgi
import commands
import time


print("Content-Type:text/html") #ignores unnecessary Information
print("")
data=cgi.FeildStorage() #extracts full html page ,taking data from apache and storing in web variable
#only want to access data in c
command=data.getvalue('c')

if command=="date":
    print("executing...")
    time.sleep(2)
    print("<pre>") #pre tag is used to show output as in the command
    print(commands.getout("date"))
    print("</pre>")
if command=="cal":
    print("executing...")
    time.sleep(2)
    print(commands.getout("cal"))



#give the page execution permission
