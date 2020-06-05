from subprocess import run

readme_md = """# My newly generated CloudFormation repo!

## Setup

Just run the `setup.py` script and start creating your templates!

add the templates in the root folder, using hyphens. E.g: `create-s3-bucket.json`.

You may use .json, .yaml or .yml for your file extensions!
"""

pre_commit_config = """# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
---
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
        stages: [commit]
  - repo: https://github.com/adrienverge/yamllint
    rev: v1.23.0
    hooks:
      - id: yamllint
        stages: [commit]
  - repo: https://github.com/aws-cloudformation/cfn-python-lint
    rev: v0.33.0
    hooks:
      - id: cfn-python-lint
        files: ^([a-zA-Z0-9]|-)+\.(json|yml|yaml)$
        stages: [commit]
  - repo: https://github.com/commitizen-tools/commitizen
    rev: v1.22.2
    hooks:
      - id: commitizen
        stages: [commit-msg]
"""

sample_s3_template = """---
Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Retain
    UpdateReplacePolicy: Retain
    Properties:
      BucketName: my-bucket
"""

setup_py = """from subprocess import run

print('### Setting up project ###')

print('## Installing pipenv...')
run('pip install pipenv', shell=True)

print('## Installing project dependencies...')
run('pipenv shell && pipenv install', shell=True)

print('### Finished setting up project ###')
"""

print('### Quick CloudFormation Setup ###')

print('## Installing pipenv...')
run('pip install pipenv', shell=True)

print('## Initializing project...')
run('pipenv install && pipenv shell', shell=True)

print('## Installing dependencies...')
run('pipenv install --dev cfn-lint pre-commit yamllint Commitizen', shell=True)

print('## Initializing git and Commitizen...')
run('git init && cz init', shell=True)

print('## Generating README.md...')
with open('README.md', 'w+') as f:
  f.write(readme_md)

print('## Configuring the project...')
with open('.pre-commit-config.yaml', 'w+') as f:
  f.write(pre_commit_config)

print('## Creating sample S3 template...')
with open('create-s3-bucket.yaml', 'w+') as f:
  f.write(sample_s3_template)

print('## Creating setup.py file...')
with open('setup.py', 'w+') as f:
  f.write(setup_py)

print('## Installing the hooks...')
run('pre-commit install && pre-commit install --hook-type commit-msg', shell=True)

print('## Enabling pre-commit for the repository itself...')
run('git config --local init.templateDir .git-template', shell=True)
run('pre-commit init-templatedir .git-template -t pre-commit -t commit-msg', shell=True)

print('### Finished creating the repository! ###')
print('tip: use the cz command to commit your files!')
