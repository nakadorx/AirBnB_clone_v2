#!/usr/bin/python3
"""
cmnt
"""
from fabric.api import local
from datetime import datetime
from os import path


def do_pack():
    """cmnt
    """
    timeF = '%Y%m%d%H%M%S'
    time = datetime.utcnow().strftime(timeF)
    filepath = "versions/web_static_{}.tgz".format(time)

    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(filepath))
    if path.exists(filepath):
        return filepath
    else:
        return None
