#!/usr/bin/env python

"""
Usage: create.prj.py [-v5] PRJNAME
Args:
	-v5: documentroot is www/PRJNAME/www, otherwise is www/PRJNAME
"""

import sys
from subprocess import call
import os

## checks on right argumnets
if '-h' in sys.argv or '--help' in sys.argv:
	print __doc__
	sys.exit(1)

if not (2 <= len(sys.argv) <= 3):
	print "Invalid arguments"
	print __doc__
	sys.exit(1)

if len(sys.argv) == 3 and not(sys.argv[1] == '-v5'):
	print "Invalid arguments"
	print __doc__
	sys.exit(1)
	
if len(sys.argv) == 2 and sys.argv[1] == '-v5':
	print "Invalid arguments"
	print __doc__
	sys.exit(1)

## save project name
if len(sys.argv) == 2:
	prj_name = sys.argv[1]
	v5 = 0
elif len(sys.argv) == 3:
	prj_name = sys.argv[2]
	v5 = 1

### main
## go to current dir with script
os.chdir(os.path.dirname(sys.argv[0]))

## create variables
relative_prj_host = "../.nginx/etc/nginx/hosts/%s.conf" % prj_name

## exit if virtual host already exists
if os.path.isfile(relative_prj_host):
	print "prj host %s already exists! Exiting.." % prj_name
	sys.exit(2)

## create nginx config
if v5 == 1:
	document_root = "../www/%s/www/" % prj_name
	s = open('../.nginx/etc/nginx/hosts/template-v5-conf', 'r').read()
else:
	document_root = "../www/%s/" % prj_name
	s = open('../.nginx/etc/nginx/hosts/template-conf', 'r').read()

s = s.replace('PRJ_NAME', prj_name)
f = open(relative_prj_host, 'w')
f.write(s)
f.close()

## create document root
os.makedirs(document_root)

## need restart docker-compose
print "Host %s succesfully created.\nNow run: docker-compose restart" % prj_name

sys.exit(0)

