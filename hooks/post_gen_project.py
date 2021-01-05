import logging
import os
import subprocess
import shutil
import sys

YES = "yes"
NO = "no"

_logger = logging.getLogger()


def cleanup():
    # retrieve cookiecutter 
    include_flaskenv = "{{cookiecutter.include_flaskenv}}"
    heroku_deployment = "{{cookiecutter.heroku_deployment}}"
    email = "{{cookiecutter.email}}"
    vcs = "{{cookiecutter.vcs}}"

    # list of files and folders to be deleted
    deletion_list = []

    # flaskenv cleanup
    if include_flaskenv == YES:
        shutil.copy(".flaskenv.example", ".flaskenv")
    
    # remove .flaskenv.example regardless
    deletion_list.append(".flaskenv.example")

    # heroku deployment cleanup
    if heroku_deployment == NO:
        deletion_list = deletion_list + ["Procfile", "wsgi.py"]
    
    # vcs setup
    if vcs == "git":
        try:
            # initialize git repository
            subprocess.call(['git', 'init'])

            # set default email
            # comment this line to prevent the default git email from being overridden
            subprocess.call(['git', 'config', 'user.email', email])

            # make initial commit
            subprocess.call(['git', 'add', '*'])
            subprocess.call(['git', 'commit', '-m', 'Initial commit'])
        except OSError as e:
            _logger.warning("An error occurred while attempting to initialize git repository")
            _logger.warning(f"Error: {e}")
            sys.exit(1)
    else:
        deletion_list = deletion_list + ['.github', '.gitignore']

    # delete unnecessary files
    try:
        for f in deletion_list:
            if os.path.isfile(f):
                os.remove(f)
            else:
                shutil.rmtree(f)
    except OSError as e:
        _logger.warning("An error occurred while attempting to remove file(s)")
        _logger.warning(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    cleanup()
