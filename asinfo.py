#!/usr/bin/env python3
import sys
import requests
import dns.resolver

'''
asinfo
 get various info about an ASN for commandline/bulk processing
'''

def as2name( asn, source='cymru' ):
	if source == 'cymru':
		return as2name_cymru( asn )
	if source == 'ripestat':
		return as2name_ripestat( asn )
	else:
		raise "unknown source %s" % source

def as2name_cymru( asn ):
	answer=dns.resolver.query("as%s.asn.cymru.com" % asn , "TXT")
	data = answer[0]
	fields = str(data).split('|')
	# remove the leading space and the '"'
	return fields[-1][1:-1]
	

def as2name_ripestat( asn ):
	req = requests.get( "https://stat.ripe.net/data/as-overview/data.json?resource=AS%s" % asn )
	j = req.json()
	return j['data']['holder']

if __name__ == "__main__":
	asn = sys.argv[1]
	print("name (via cymru)   : %s" % as2name( asn, source='cymru' ) )
	print("name (via ripestat): %s" % as2name( asn, source='ripestat' ) )
