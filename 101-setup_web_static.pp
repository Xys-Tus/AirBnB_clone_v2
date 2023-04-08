# sets up the web servers for the deployment of web_static

exec { 'command':
  command  => 'sudo apt-get -y update;
  sudo apt-get -y upgrade;
  sudo apt-get -y install nginx;
  sudo mkdir -p /data/web_static/releases/test /data/web_static/shared;
  sudo echo "This is a test" | sudo tee /data/web_static/releases/test/index.html;
  sudo ln -sf /data/web_static/releases/test/ /data/web_static/current;
  sudo chown -hR ubuntu:ubuntu /data/;
  sudo service nginx start',
}
