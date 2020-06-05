from subprocess import run

print('### Setting up project ###')

print('## Installing pipenv...')
run('pip install pipenv', shell=True)

print('## Installing project dependencies...')
run('pipenv shell && pipenv install', shell=True)

print('### Finished setting up project ###')
