#!/usr/bin/env python

import sys
import os
import json
import git
import argparse
import subprocess

## parse args
parser = argparse.ArgumentParser("Create and init web project. Working on python 2.x")
parser.add_argument('--config','-c', type=file, default='config.json', help='config file (default - config.json)')
parser.add_argument('--version-lib','-v', type=int, choices=[4, 5], default=4, help='choose adx lib version (default - 4)')
parser.add_argument('--init-script','-i', type=str, choices=['adx', 'wp'], help='run php script from init-scripts/')
parser.add_argument('project', type=str)
args = parser.parse_args()

## init variables
p = args.project
v = args.version_lib
f = args.config.read()

### main
## go to current dir with script
os.chdir(os.path.dirname(sys.argv[0]))

## get prj_host, config values
config = json.loads(f)
host_name=config["host_name"].replace("{PRJ_NAME}", p)
dir_name=config["dir_name"].replace("{PRJ_NAME}", p)
relative_prj_host = "../.nginx/etc/nginx/hosts/{}.conf".format(host_name)

## exit if virtual host already exists
if os.path.isfile(relative_prj_host):
	print "prj host {} already exists! Exiting..".format(p)
	sys.exit(2)

## if documentroot already exists
if not(os.path.isdir('../htdocs/'+p)):
    if 'git_access' in f:
        git.Git().clone(config["git_access"], '../htdocs/'+dir_name)
    else:
        os.makedirs('../htdocs/'+dir_name)

## create nginx config
if v == 5:
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

## run init-scripts
if not(args.init_script == None):
    subprocess.call(["php", "init-scripts/{}.php".format(args.init_script)])
sys.exit(2)

## finish
print 'Vhost {} is created:\n\t- your config is {}\n\t- your documentroot is {}\n1. run: docker-compose restart nginx\n2. open http://{}/'.format(p,os.path.normpath(os.path.realpath(relative_prj_host)), os.path.normpath(os.path.realpath(document_root)), host_name)

sys.exit(0)

