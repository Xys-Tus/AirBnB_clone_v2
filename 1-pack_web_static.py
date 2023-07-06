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
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                local(f"tar -czvf web_static{current_dataNtime}.tar.gz {file}")
                print(f"./web_static/{file}")
    else:
        print("Not a directory")
