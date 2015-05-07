#!/usr/bin/env python

"""
Usage: create.prj.py [-v5] PRJNAME
Args:
	-v5: documentroot is www/PRJNAME/www, otherwise is www/PRJNAME
"""

import sys
from subprocess import call
import os

if '-h' in sys.argv or '--help' in sys.argv:
	print __doc__
	sys.exit(1)

if len(sys.argv) == 2:
	## go to current dir with script
	os.chdir(os.path.dirname(sys.argv[0]))

	## create variables
	prj_name = sys.argv[1]
	relative_prj_host = "../.nginx/etc/nginx/hosts/%s.conf" % prj_name

	## exit if virtual host already exists
	if os.path.isfile(relative_prj_host):
		print "prj host %s already exists! Exiting.." % prj_name
		sys.exit(2)

	## create nginx config
	s = open('../.nginx/etc/nginx/hosts/template-conf', 'r').read()
	s = s.replace('PRJ_NAME', prj_name)
	f = open(relative_prj_host, 'w')
	f.write(s)
	f.close()

	## create document root
	os.makedirs('../www/'+prj_name)

	## need restart docker-compose
	print "Host %s succesfully created.\nNow run: docker-compose restart" % prj_name

	sys.exit(0)

if len(sys.argv) == 3:
	if '-v5' in sys.argv:
		print "v5"
		sys.exit(0)

print "Incorrect arguments"
print __doc__
sys.exit(1)

