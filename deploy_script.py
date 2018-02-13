import os
import paramiko
import sys

pem_file = sys.argv[1]
server = sys.argv[2]
prefix = sys.argv[3]


def deploy(path, server, prefix):

  print "Connecting to box"
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  print server
  print path
  ssh.connect(server, username = 'testtest', key_filename = path)
  print "Connected to server"

  # clone git
  ssh.exec_command("yum install git -y")
  print "cloning git"
  ssh.exec_command("rm -rf Analytics-Ingestion-Engine; git clone https://github.com/asmitav/Analytics-Ingestion-Engine.git")
  print "cloned git"

  print "crontab remove"
  ssh.exec_command("crontab -r") # Removing existing crontabs

  print "setting crontab"
  new_command = "5 * * * * python /home/testtest/Analytics-Ingestion-Engine/json_parser.py " + prefix
  print new_command
  ssh.exec_command('(crontab -l ; echo "' + new_command + '" ) | crontab -')

  ssh.exec_command('logout')

deploy(pem_file, server, prefix)
