#!/usr/bin/python3
"""
 Fabric script that generates a .tgz archive
 from the contents of the web_static folder of your AirBnB Clone repo,
 using the function do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    date-will return the current date and time
    archive_name- will return the name of the archive
    local-will use the local command
    print will print the result
    """

    try:
        # Create the "versions" directory if it doesn't exist
        local("mkdir -p versions")

        # Create the archive filename with the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)

        # Compress the contents of the "web_static" directory into the archive
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the path to the archive
        return "versions/{}".format(archive_name)
    except Exception as e:
        return None
