import shutil

def delete_file(path):
  try:
    shutil.rmtree(path)
  except OSError as e:
    print("Error: %s : %s" % (path, e.strerror))

use_cloudformation = '{{ cookiecutter.use_cloudformation }}'.lower() == 'y'
use_terraform = '{{ cookiecutter.use_terraform }}'.lower() == 'y'

if not use_cloudformation:
  delete_file('cloudformation')

if not use_terraform:
  delete_file('terraform')
