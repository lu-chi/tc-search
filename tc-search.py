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
import sys

url = "http://www.threatcrowd.org/searchApi/v2/{}/report/"
#url = "http://www.threatcrowd.org/searchApi/v2/{}/malware/"

wait = 10

def main(args):

	# use only existing (set) arguments
	for i, k in vars(args).iteritems():
		if k is not None:
			d = {}
			c = len(k)
			for item in k:
				d = {i:item}
				print "[+] Querying: {}, {}".format(url.format(i),d) 
				try:
					result = requests.get(url.format(i), d)
					j = json.loads(result.text)
				except:
					print "[!] No results available!"
					sys.exit(1)

				if args.output:
					try:
						with open(args.output, 'ab') as o:
							json.dump(j, o, sort_keys=True, indent=4, separators=(',',': '))
							o.write("\n\n")
					except:
						print "[!] Can't write to a file: {}".format(args.output)
						sys.exit(1)
				else:
					print json.dumps(j, sort_keys=True, indent=4, separators=(',',': '))
					#print json.dumps(j, indent=4)
				c -= 1
				if c > 0:
					print "[!] Waiting {} secs...".format(wait)
					time.sleep(wait)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--domain', nargs='+')
	parser.add_argument('-i', '--ip', nargs='+')
	parser.add_argument('-a', '--antivirus', nargs='+')
	parser.add_argument('-s', '--filehash', dest='md5', nargs='+')
	parser.add_argument('-e', '--email', nargs='+')
	parser.add_argument('-o', '--output')
	parser.add_argument('-f', '--file', dest='inFile')
	args = parser.parse_args()
	if len(sys.argv)==1:
		parser.print_help()
		sys.exit(1)
	else:
		main(args)

