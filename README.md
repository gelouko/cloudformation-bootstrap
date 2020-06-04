# Simple Yaml Setup

This is a simple project setup for projects containing just yaml files.
This will make sure the commited code is linted and valid.

# Setup (The main resource of this repo)

0. Requirements:
  0.1 Pipenv
  ```bash
    pip install pipenv
  ```

1. Init your project:
  ```bash
    pipenv install
    pipenv shell
  ```

2. Install the necessary dependencies (pre-commit, [cfn-lint](https://github.com/aws-cloudformation/cfn-python-lint)):
  ```bash
    pipenv install --dev cfn-lint pre-commit Commitizen
  ```

3. Init Commitizen:
  ```bash
    cz init
  ```

4. Generate some basic configuration for pre-commit:
  ```bash
    touch .pre-commit-config.yaml && \
    pre-commit sample-config >> .pre-commit-config.yaml && \
  ```

5. Add the cloudformation and Commitizen-specific configuration. The file should look like this:
  ```
    # See https://pre-commit.com for more information
    # See https://pre-commit.com/hooks.html for more hooks
    repos:
    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v2.4.0
        hooks:
        -   id: trailing-whitespace
        -   id: end-of-file-fixer
        -   id: check-yaml
        -   id: check-added-large-files
    -   repo: https://github.com/aws-cloudformation/cfn-python-lint
        rev: v0.33.0
        hooks:
        -   id: cfn-python-lint
            files: ^([a-zA-Z0-9]|-)+\.(json|yml|yaml)$
    -   repo: https://github.com/commitizen-tools/commitizen
        rev: v1.22.2
        hooks:
        -   id: commitizen
            stages: [commit-msg]
  ```

6. Install the git hook scripts
  ```bash
    pre-commit install && pre-commit install --hook-type commit-msg
  ```

7. Test your current environment!
  ```bash
    git add --a
    cz commit
  ```
