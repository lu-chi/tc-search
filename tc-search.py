'''
	ThreatCrowd example API queries: 
	===============================
	print requests.get("http://www.threatcrowd.org/searchApi/v2/domain/report/", {"domain": "aoldaily.com"}).text
	print requests.get("http://www.threatcrowd.org/searchApi/v2/ip/report/", {"ip": "188.40.75.132"}).text
	print requests.get("http://www.threatcrowd.org/searchApi/v2/antivirus/report/", {"antivirus" :"plugx"}).text
	
	result =  requests.get("http://www.threatcrowd.org/searchApi/v2/email/report/", params = {"email": "william19770319@yahoo.com"})
	print result.text
	j = json.loads(result.text)
	print j['domains'][0]
'''

import requests
import json
import argparse
import time

url = "http://www.threatcrowd.org/searchApi/v2/{}/report/"
wait = 10

def main(args):

	# use only existing (set) arguments
	for i, k in vars(args).iteritems():
		if k is not None:
			d = {}
			c = len(k)
			print c
			for item in k:
				d = {i:item}
				print d
				print "[+] Querying: {}, {}".format(url.format(i),d) 
				result = requests.get(url.format(i), d)
				j = json.loads(result.text)
				print j
				c -= 1
				if c > 0:
					print "[!] Sleep for {} secs...".format(wait)
					time.sleep(wait)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--domain', nargs='+')
	parser.add_argument('-i', '--ip', nargs='+')
	parser.add_argument('-a', '--antivirus', nargs='+')
	parser.add_argument('-s', '--filehash', nargs='+')
	parser.add_argument('-e', '--email', nargs='+')
	parser.add_argument('-f', '--file')
	parser.add_argument('-o', '--output')
	args = parser.parse_args()
	main(args)



