#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
# Install Nginx if not already installed
if ! command -v nginx &> /dev/null
then
  echo "Installing nginx"
  apt-get -y update
  apt-get -y install nginx
fi
# Create a necessary directories if they do not exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
# Create a symbolic link to the test directory
echo "<html>
  </head>
  <body>
  Holberton School
  </body>
</html>" | tee /data/web_static/releases/test/index.html > /dev/null

# Delete the symbolic link if it exists
rm -f /data/web_static/current

# Create a symbolic link to the latest directory
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
sed -i "/server_name _;/a\\        location /hbnb_static/ {alias /data/web_static/current/;}" "$config_file" > /dev/null
service nginx restart
