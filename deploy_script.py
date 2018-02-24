import os
import paramiko
import sys

def deploy(path, server, prefix):

  print "Connecting to box"
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  print server
  print path
  ssh.connect(server, username = 'ec2-user', key_filename = path)
  print "Connected to server"

  # clone git
  print "cloning git"
  ssh.exec_command("rm -rf Analytics-Ingestion-Engine; git clone https://github.com/asmitav/Analytics-Ingestion-Engine.git")
  print "cloned git"

  print "crontab remove"
  ssh.exec_command("crontab -r") # Removing existing crontabs

  print "setting crontab"
  new_command = "*/1 * * * * python /home/ec2-user/Analytics-Ingestion-Engine/json_parser.py " + prefix
  print new_command
  ssh.exec_command('(crontab -l ; echo "' + new_command + '" ) | crontab -')

  print "Launch server"
  ssh.exec_command('python /home/ec2-user/Analytics-Ingestion-Engine/flask_server.py ' + prefix )
  print "Server launched"
  #ssh.exec_command('logout')

pem_file = "/Users/deena/Downloads/msan694_spark.pem"
server = "ec2-54-201-217-62.us-west-2.compute.amazonaws.com"
prefix = "test"

deploy(pem_file, server, prefix)
