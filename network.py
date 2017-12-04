from wicore import *
import socket

def connect(name,password):
	# replaced cell.ssid with name 
	scheme=SchemeWPA('wlan0',name,{'ssid':name,"psk":password})

def isInternet(host="8.8.8.8", port=53, timeout=3):
      """d
      Host: 8.8.8.8 (google-public-dns-a.google.com)
      OpenPort: 53/tcp
      Service: domain (DNS/TCP)
      """
	try:
		socket.setdefaulttimeout(timeout)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		return True
	except Exception as ex:
		print ex.message
		return False
