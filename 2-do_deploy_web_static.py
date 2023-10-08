#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from fabric.api import run, put, env
from os.path import exists

env.hosts = ['<54.174.82.78', '18.204.6.61']
env.user = 'ubuntu'
env.key_filename = '/home/ubuntu/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ on the web server
        put(archive_path, "/tmp/")

        # Extract the archive to the /data/web_static/releases/ folder
        archive_filename = archive_path.split("/")[-1]
        folder_name = archive_filename.split(".")[0]
        release_path = "/data/web_static/releases/{}/".format(folder_name)
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_path))

        # Delete the uploaded archive
        run("rm /tmp/{}".format(archive_filename))

        # Delete the current symbolic link
        run("rm -f /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_path))

        return True

    except Exception:
        return False
