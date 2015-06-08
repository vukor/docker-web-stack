#!/usr/bin/env python2

import sys
import os


def parse_arguments():
    """ Parse command arguments, return args """

    import argparse
    parser = argparse.ArgumentParser("Create and init web project. Working on python 2.x")
    parser.add_argument('--config','-c', type=file, default='config.json', help='config file (default - config.json)')
    parser.add_argument('--profile','-p', type=str, default='default', help='choose profile from config')
    parser.add_argument('project', type=str)
    
    return parser.parse_args()

def parse_config(file,profile,project_name):
    """ Parse json config, return config parametres """
    import json
    config = json.loads(file)

    ## check config
    if not('host_name' in config[profile]):
        print "Not found host_name in config! Exiting.."
        sys.exit(2)
    else:
        host_name = config[profile]["host_name"].replace("PRJ_NAME", project_name)
    
    if not('dir_name' in config[profile]):
        print "Not found dir_name in config! Exiting.."
        sys.exit(2)
    else:
        dir_name = config[profile]["dir_name"].replace("PRJ_NAME",project_name)
    
    if not('template_ngx' in config[profile]):
        print "Not found profile in config! Exiting.."
        sys.exit(2)
    else:
        template_ngx = "../.nginx/etc/nginx/hosts/{}".format(config[profile]["template_ngx"].replace("PRJ_NAME", project_name))
    
    if 'init_script' in config[profile] and config[profile]["init_script"] != "":
        init_script = config[profile]["init_script"].replace("PRJ_NAME", project_name)
    else:
        init_script = None
    
    if 'git_access' in config[profile] and config[profile]["git_access"] != "":
        git_access = config[profile]["git_access"].replace("PRJ_NAME", project_name)
    else:
        git_access = None

    return (
        host_name,
        dir_name,
        git_access,
        template_ngx,
        init_script
    )

def create_virtual_host(templ_nginx_config,nginx_config,profile,project_name,host_name,dir_name):
    """ Create nginx config, docimentroot for web project """

    ## checks
    if os.path.isfile(nginx_config):
        print "nginx config {} already exists! Exiting..".format(nginx_config)
        sys.exit(2)

    if not(os.path.isfile(templ_nginx_config)):
        print "template config {} does not exists! Exiting..".format(templ_nginx_config)
        sys.exit(2)

    s = open(templ_nginx_config, 'r').read()
    s = s.replace('HOST_NAME', host_name)
    s = s.replace('PRJ_NAME', project_name)
    s = s.replace('DIR_NAME', dir_name)
    f = open(nginx_config, 'w')
    f.write(s)
    f.close()

    document_root = "../htdocs/{}".format(dir_name)

    ## create document root
    if not(os.path.isdir(document_root)):
        os.makedirs(document_root)
    return document_root

def clone_repo(repo,local):
    """ clone repo to local """
    import git
    git.Git().clone(repo,local)


def main():

    import subprocess

    ## go to current dir with script
    os.chdir(os.path.dirname(sys.argv[0]))

    ## parse cmd arguments
    args = parse_arguments()
    prj_name = args.project
    profile = args.profile
    config = args.config.read()

    ## parse json config
    config = parse_config(config,profile,prj_name)

    ## check config, init config params
    host_name = config[0]
    dir_name = config[1]
    git_access = config[2]
    template_ngx = config[3]
    init_script = config[4]
    ngx = "../.nginx/etc/nginx/hosts/{}.conf".format(host_name)

    ## init project
    if not(os.path.isdir('../htdocs/{}'.format(prj_name))):
        if not(git_access == None):
            clone_repo(git_access,"../htdocs/{}".format(prj_name))

    ## create virtual host
    document_root = create_virtual_host(template_ngx,ngx,profile,prj_name,host_name,dir_name)

    ## run init-script
    if not(init_script == None):
        subprocess.call(["../{}".format(init_script)])

    ## finish
    print "==============="
    os.chdir('../')
    subprocess.call(["docker-compose", "restart"])
    print "==============="
    os.chdir('bin/')
    print 'web project {} is created:\n\t- your config is {}\n\t- your documentroot is {}\nNow open http://{}/'.format(prj_name,os.path.normpath(os.path.realpath(ngx)), os.path.normpath(os.path.realpath(document_root)), host_name)


if __name__ == "__main__":
    main()

sys.exit(0)

