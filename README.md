# snapshotalyzer-30000
Demo project to manage AWS EC2 instances snapshots


## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshot.

## configuring

shotty uses the configuration file created by the AWS cli. e.g.

'aws configure -- profile shotty'

## running

'pipenv run "python shotty/shotty.py <command. <--project=PROJECT>"'

*command* is list, start, or stop
*project* is optional
