from subprocess import run
import os.path

print('### Setting up project ###')

if not os.path.exists('.git'):
  print('## Not a git repository. Initializing git...')
  run('git init', shell=True)

print('## Installing project dependencies...')
run('pipenv install --dev', shell=True)

print('## Installing the hooks...')
run('pre-commit install && pre-commit install --hook-type commit-msg', shell=True)

print('## Enabling pre-commit for the repository itself...')
run('git config --local init.templateDir .git-template', shell=True)
run('pre-commit init-templatedir .git-template -t pre-commit -t commit-msg', shell=True)

print('### Finished setting up project ###')
