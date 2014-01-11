from fabric.api import *
from fabric.colors import green, red
from fabric.contrib import files
import datetime
import os

def _environment ():
	env.release = datetime.datetime.now().strftime ("%Y-%m-%d-%H%M%S")

	# FIXME: hardcoded path:
	env.path_home = '/opt/lancms2/'
	env.path_root = os.path.join (env.path_home, 'deployment/')
	
	env.path_current = os.path.join (env.path_root, 'current')
	env.path_releases = os.path.join (env.path_root, 'releases/')
	env.path_full_release = os.path.join (env.path_releases, env.release)
	env.path_full_release_local_settings = os.path.join (env.path_full_release, 'lancms2/local_settings.py')
	env.path_full_release_local_sqlite = os.path.join (env.path_full_release, 'lancms2/lancms2.sql')
	env.virenv = 'source %s/virtualenv/bin/activate' % env.path_root

	# FIXME: hardcoded user and group:
	env.owner_user = 'www-data'
	env.owner_group = 'lancms2'


def _upload_and_unpack ():
	# local is on local host
	local ('bzr export --format=tgz %s.tar.gz' % env.release);
	
	# run is on remote host!
	run ('mkdir -p %s' % env.path_full_release)

	# put places local file on remote server
	put ('%s.tar.gz' % env.release, env.path_releases, mode=0750)

	with cd ('%s' % env.path_releases):
		run ('tar -xzf %s.tar.gz' % env.release)
		run ('rm %s.tar.gz' % env.release)
	
	print (green ('Uploaded and unpacked'))


def _create_virtualenv ():
	with cd ('%s' % env.path_root):
		run ('virtualenv virtualenv')
	run ('source %svirtualenv/bin/activate' % env.path_root)
	print (green ('Created (or recreated) virtual environment'))


def _set_release_permissions ():
	sudo ('chown %s:%s -R %s' % (env.owner_user, env.owner_group, env.path_full_release), shell=False)
	sudo ('chmod g+w -R %s' % (env.path_full_release), shell=False)
	print (green ('Set permissions for www-data on %s' % env.path_full_release))


def _install_requirements ():
	with cd ('%s' % env.path_full_release):
		run ('source %svirtualenv/bin/activate; pip install -r requirements.txt' % env.path_root)
	print (green ('Installed requirements in virtual environment'))


def _symlink_local_settings ():
	path_file = os.path.join (env.path_home, 'LOCAL_SETTINGS.py')
	if files.exists (path_file):
		run ('ln -s %s %s' % (path_file, env.path_full_release_local_settings))
		print (green ('Symlinked local_settings'))

def _symlink_local_sqlite ():
	path_file = os.path.join (env.path_home, 'LANCMS2.sql')
	if files.exists (path_file):
		run ('ln -s %s %s' % (path_file, env.path_full_release_local_sqlite))
		print (green ('Symlinked local sqlite'))


def _symlink_current_release ():
	if files.exists (env.path_current):
		run ('rm -f %s' % env.path_current)
	print (red ('Removed symlink for previous release'))
	run ('ln -s %s %s' % (env.path_full_release, env.path_current))
	print (green ('Symlinked current release %s to %s' % (env.release, env.path_current)))


def deploy ():
	_environment ()
	_upload_and_unpack ()
	_create_virtualenv ()
	_install_requirements ()
	_symlink_local_settings ()
	_symlink_local_sqlite ()
	_symlink_current_release ()
	_set_release_permissions ()


def help ():
	print ""
	print "deployment script for lancms2"
	print ""
	print "Only available command is 'deploy'."
	print "Please don't use this if you don't know what it does! No warranties!"
