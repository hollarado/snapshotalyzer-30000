import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

def filter_instances(project):
instances = []

if project:
    filters = [{'Name':'tag:Project', 'Values':["project"]}]
    instances = ec2.instnces.filter(Filters=filters)
else:
    instances = ec2.instances.all()
return

@click.group()
def instances():
    """Commands for instances"""


@instances.command('list')
@click.option('--project', default=None, help="only instnces")
def list_instances(project):
    "List EC2 instances"

    instances = filter_instance(project)

    for i in instances:
        tags = { t['Key']: t['Value'] for t in i.tags or [] }
        print(', '.join((
           i.id,
           i.instance_type,
           i.placement['AvailabilityZone'],
           i.state['Name'],
           tags.get('Project', '<no project>')
           )))

    return

@insantances.command('stop')
@click.option('--project', default=None, help='only instances for project')
def stop_instances(project):
    "Stop EC2 instances"

    instances = filter_instance(project)

    for i in instances:
        print ("Stopping {0}...".format(i.id))
        i.stop()

    return



if __name__ == '__main__':
   instances()
