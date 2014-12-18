#!/usr/bin/python

#
import random
#
def randomMAC():
	mac = [ 0x00, 0x16, 0x3e,
		random.randint(0x00, 0x7f),
		random.randint(0x00, 0xff),
		random.randint(0x00, 0xff) ]
	return ':'.join(map(lambda x: "%02x" % x, mac))
#
print randomMAC()
import os
import subprocess
p = subprocess.Popen(['ifconfig', 'wlan0', 'down'])
a = subprocess.Popen(['ifconfig', 'urtwn0', 'ether', 'randomMAC'])
b = subprocess.Popen(['ifconfig', 'wlan0', 'up'])
c = subprocess.Popen(['dhclient', 'wlan0'])
p.communicate()
a.communicate()
b.communicate()
c.communicate()
