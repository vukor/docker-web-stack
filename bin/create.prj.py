#!/usr/bin/env python

"""
Usage: create.prj.py [-v5] PRJNAME
Args:
	-v5: documentroot is htdocs/PRJNAME/www, otherwise is htdocs/PRJNAME

Working on python version 2
"""

import sys
import os
import json
import git

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

## check that config exists
if not(os.path.isfile('./config.json')):
    print "config.json does not exist! Exiting.."
    sys.exit(1)


### main
## go to current dir with script
os.chdir(os.path.dirname(sys.argv[0]))

## get prj_host, config values
file=open('config.json').read()
config = json.loads(file)
host_name=config["host_name"].replace("{PRJ_NAME}", prj_name)
dir_name=config["dir_name"].replace("{PRJ_NAME}", prj_name)
relative_prj_host = "../.nginx/etc/nginx/hosts/{}.conf".format(host_name)

## exit if virtual host already exists
if os.path.isfile(relative_prj_host):
	print "prj host {} already exists! Exiting..".format(prj_name)
	sys.exit(2)

## if documentroot already exists
if not(os.path.isdir('../htdocs/'+prj_name)):
    if 'git_access' in file:
        git.Git().clone(config["git_access"], '../htdocs/'+dir_name)
    else:
        os.makedirs('../htdocs/'+dir_name)

## create nginx config
if v5 == 1:
	document_root = "../htdocs/{}/www/".format(host_name)
	s = open('../.nginx/etc/nginx/hosts/template-v5-conf', 'r').read()
else:
	document_root = "../htdocs/{}/".format(host_name)
	s = open('../.nginx/etc/nginx/hosts/template-conf', 'r').read()

s = s.replace('HOST_NAME', host_name)
f = open(relative_prj_host, 'w')
f.write(s)
f.close()

## create document root
if not(os.path.isdir(document_root)):
    os.makedirs(document_root)

## finish
print 'Vhost {} is created:\n\t- your config is {}\n\t- your documentroot is {}\n1. run: docker-compose restart nginx\n2. open http://{}/'.format(prj_name,os.path.normpath(os.path.realpath(relative_prj_host)), os.path.normpath(os.path.realpath(document_root)), host_name)

sys.exit(0)

