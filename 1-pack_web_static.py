#!/usr/bin/python3
"""[Fabric script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo]
"""
from fabric.api import local
from datetime import datetime
from os import path


def do_pack():
    """[generates a .tgz archive]
    """
    time = datetime.utcnow()
    filepath = "/versions/web_static_ {}.tgz".format(time)
    local("mkdir versions")
    local("tar -czvf {} web_static".format(filepath))
    if path.exists(filepath):
        return filepath