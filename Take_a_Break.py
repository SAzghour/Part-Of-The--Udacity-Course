import webbrowser
import time                 

total_Break = 6
count = 0

print("This Programe Started on : " + time.ctime() )  

while(count < 6):                   
	time.sleep(7200)                   # Calculation Two hours
	webbrowser.open("http://www.youtube.com")
	count += 1

#print (2*60*60)       
