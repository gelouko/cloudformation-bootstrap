# {{cookiecutter.project_name}}

## Requirements
- [pipenv](https://pypi.org/project/pipenv/)

{% if cookiecutter.use_terraform == 'y' %}
- [terraform](https://www.terraform.io/downloads.html)
- [terragrunt](https://terragrunt.gruntwork.io/docs/getting-started/install/)
- [terraform-docs](https://github.com/segmentio/terraform-docs)
- [tflint](https://github.com/terraform-linters/tflint)
- [tfsec](https://github.com/liamg/tfsec)
{% endif %}

## Setup

Just run `pipenv run setup` to setup your repository and start creating your templates!

add the templates in their respective folders - there are some scaffold examples in the project.

You may use .json, .yaml or .yml for your cloudformation file extensions!
