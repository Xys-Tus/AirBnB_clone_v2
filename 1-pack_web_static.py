#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    path = "./web_static"
    current_dataNtime = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        if isdir('versions') is False:
            local("mkdir versions")
        file_name = "verions/web_static_{}.tgz".format(
            current_dataNtime)
        local("tar -czvf {} web_static".format(file_name))
        return file_name
    except:
        return None
