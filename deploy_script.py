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
  ssh.connect(server, username = 'ec2-user', key_filename = path)
  print "Connected to server"

  # clone git
  print "cloning git"
  ssh.exec_command("rm -rf Analytics-Ingestion-Engine; git clone https://github.com/asmitav/Analytics-Ingestion-Engine.git")
  ssh.exec_command("cd Analytics-Ingestion-Engine; git checkout json_parser_nishan2")
  print "cloned git"

  print "crontab remove"
  ssh.exec_command("crontab -r") # Removing existing crontabs

  print "setting crontab"
  new_command = "5 * * * * python /home/ec2-user/Analytics-Ingestion-Engine/json_parser.py " + prefix
  print new_command
  ssh.exec_command('(crontab -l ; echo "' + new_command + '" ) | crontab -')

deploy(pem_file, server, prefix)
