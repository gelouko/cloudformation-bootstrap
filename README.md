# Simple CloudFormation Setup

This is a simple project setup for projects containing just yaml and json files for CloudFormation.
This will make sure your CFN templates are linted and valid.

It will use the following linters (feel free to add others to your setup):
- [pre-commit](https://github.com/pre-commit/pre-commit-hooks)
- [yamllint](https://github.com/adrienverge/yamllint)
- [cfn-lint](https://github.com/aws-cloudformation/cfn-python-lint)
- [Commitizen](https://github.com/commitizen-tools/commitizen)

# TL,DR

1. Run `generate_repo.py` to generate the repo with this configuration.

2. Your developers can use `setup.py` to setup their projects locally!

3. Integrate with
    1. [Github actions](https://commitizen-tools.github.io/commitizen/tutorials/github_actions/)
    2. [Gitlab CI](https://commitizen-tools.github.io/commitizen/tutorials/gitlab_ci/)

# Setup (The main resource of this repo)

1. Requirements:
  0.1 Pipenv
  ```bash
    pip install pipenv
  ```

2. Init your project:
  ```bash
    pipenv install
    pipenv shell
  ```

3. Install the necessary dependencies:
  ```bash
    pipenv install --dev cfn-lint pre-commit yamllint Commitizen
  ```

4. Init git and Commitizen:
  ```bash
    git init && cz init
  ```

5. Create the pre-commit configuration file:
  ```bash
    touch .pre-commit-config.yaml
  ```

6. Add the cloudformation and Commitizen-specific configuration. The file should look like this:
  ```
    # See https://pre-commit.com for more information
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
  ```

7. Install the git hook scripts
  ```bash
    pre-commit install && pre-commit install --hook-type commit-msg
  ```

8. Test your current environment!
  ```bash
    git add --a
    cz commit
  ```

9. Enable pre-commit for the repository itself
  ```bash
    git config --local init.templateDir .git-template
    pre-commit init-templatedir .git-template -t pre-commit -t commit-msg
  ```
