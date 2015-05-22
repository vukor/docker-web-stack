#!/usr/bin/env python

import sys
import os
import git
import subprocess


def parse_arguments():
    """ Parse command arguments, return args """
    import argparse
    parser = argparse.ArgumentParser("Create and init web project. Working on python 2.x")
    parser.add_argument('--config','-c', type=file, default='config.json', help='config file (default - config.json)')
    parser.add_argument('--version-lib','-v', type=int, choices=[4, 5], default=4, help='choose adx lib version (default - 4)')
    parser.add_argument('--init-script','-i', type=str, choices=['adx', 'wp'], help='after creating web project run adx.php or wp.php from init-scripts/')
    parser.add_argument('project', type=str)
    return parser.parse_args()


def parse_config(f):
    """ Parse json config, return config parametres """
    import json
    config = json.loads(f)

    if 'git_access' in f:
        return (
            config["host_name"].replace("{PRJ_NAME}", p),
            config["dir_name"].replace("{PRJ_NAME}", p),
            config["git_access"].replace("{PRJ_NAME}",p)
        )
    else:
        return (
            config["host_name"].replace("{PRJ_NAME}", p),
            config["dir_name"].replace("{PRJ_NAME}", p)
        )

def create_nginx_config():
    """ Create nginx config for web project """
    if v == 5:
        document_root = "../htdocs/{}/www/".format(p)
        s = open('../.nginx/etc/nginx/hosts/template-v5-conf', 'r').read()
    else:
        document_root = "../htdocs/{}/".format(p)
        s = open('../.nginx/etc/nginx/hosts/template-conf', 'r').read()

    s = s.replace('HOST_NAME', host_name)
    s = s.replace('PRJ_NAME', p)
    f = open(relative_prj_host, 'w')
    f.write(s)
    f.close()
    return document_root


## go to current dir with script
os.chdir(os.path.dirname(sys.argv[0]))

## parse args
args = parse_arguments()
p = args.project
v = args.version_lib
f = args.config.read()

## parse config
config = parse_config(f)
host_name = config[0]
dir_name = config[1]
relative_prj_host = "../.nginx/etc/nginx/hosts/{}.conf".format(host_name)

### main


## exit if virtual host already exists
if os.path.isfile(relative_prj_host):
	print "prj host {} already exists! Exiting..".format(p)
	sys.exit(2)

## if documentroot already exists
if not(os.path.isdir('../htdocs/'+p)):
    if len(config) == 3:
        git.Git().clone(config[2],'../htdocs/'+dir_name)
    else:
        os.makedirs('../htdocs/'+dir_name)

document_root=create_nginx_config()

## create document root
if not(os.path.isdir(document_root)):
    os.makedirs(document_root)

## run init-script
if not(args.init_script == None):
    subprocess.call(["php", "init-scripts/{}.php".format(args.init_script)])

## finish
print "==============="
os.chdir('../')
#subprocess.call(["docker-compose", "restart"])
print "==============="
print 'web project {} is created:\n\t- your config is {}\n\t- your documentroot is {}\nNow open http://{}/'.format(p,os.path.normpath(os.path.realpath(relative_prj_host)), os.path.normpath(os.path.realpath(document_root)), host_name)

sys.exit(0)

