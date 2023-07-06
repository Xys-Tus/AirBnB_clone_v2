#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir
import os


def do_pack():
    """generates a tgz archive"""
    path = "./web_static"
    current_dataNtime = datetime.today().strftime("%Y%m%d%H%M%S")
    print(type(current_dataNtime))
    try:
        if isdir('./versions') is False:
            local("mkdir versions")
        file_name = f"verions/web_static_{current_dataNtime}.tgz"
        local(f"tar -czvf {file_name} web_static")
        return file_name
    except:
        return None
