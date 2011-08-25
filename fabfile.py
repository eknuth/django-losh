from fabric.api import env, local, run


#http://www.sysadminpy.com/2011/04/use-fabric-on-vagrant-instances/ 
def vagrant():
    # change from the default user to 'vagrant'
    env.user = 'vagrant'
    # connect to the port-forwarded ssh
    env.hosts = ['127.0.0.1:2222']
 
    # use vagrant ssh key
    result = local('vagrant ssh_config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]
 
def deploy():
     run('/usr/local/venv/project/bin/pip install -r /vagrant/apps/project/requirements.txt')
     run('/usr/local/venv/project/bin/python /vagrant/apps/project/manage.py syncdb --settings="project.settings_local" --noinput')

def restart():
    run('sudo /etc/init.d/gunicorn-project restart')

