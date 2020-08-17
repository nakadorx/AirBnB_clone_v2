#!/usr/bin/python3
"""
comnt
"""
from os.path import exists
from fabric.api import put, run, env
env.hosts = ['35.237.44.86', '35.237.162.75']


def do_deploy(archive_path):
    """cont """
    if exists(archive_path) is False:
        return False
    try:
        fileName = archive_path.split("/")[-1]
        noEx = fileName.split(".")[0]
        pt = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(pt, noEx))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fileName, pt, noEx))
        run('rm /tmp/{}'.format(fileName))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(pt, noEx))
        run('rm -rf {}{}/web_static'.format(pt, noEx))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(pt, noEx))
        return True
    except:
        return False*
