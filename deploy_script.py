import os
import paramiko
import sys

def deploy(path, server, prefix):
  """
	The code connects to the EC2 server and clones the git repo.
	It then starts the flask server.
  """
  print "Connecting to box"
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  print server
  print path
  ssh.connect(server, username = 'testtest', key_filename = path)
  print "Connected to server"

  # clone git
  print "cloning git"
  ssh.exec_command("rm -rf Analytics-Ingestion-Engine; git clone https://github.com/asmitav/Analytics-Ingestion-Engine.git")
  print "cloned git"

  # Removing existing crontabs
  print "crontab remove"
  ssh.exec_command("crontab -r") 


  print "Launch server"
  ssh.exec_command('sudo chmod -R ugo+rw /srv/runme')
  ssh.exec_command('python /home/testtest/Analytics-Ingestion-Engine/flask_server.py ' + prefix)
  print "Server launched"
  ssh.exec_command('logout')

# pem_file = "/Users/Asmita/.ssh/asmitavi_oregon_deeplearning.pem"
# server = "ec2-54-218-82-213.us-west-2.compute.amazonaws.com"
# prefix = "test"

deploy(pem_file, server, prefix)
