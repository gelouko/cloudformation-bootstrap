from sys import exit

bool_variables = {
  'use_cloudformation': '{{ cookiecutter.use_cloudformation }}',
  'use_terraform': '{{ cookiecutter.use_terraform }}'
}

def is_cli_bool(value):
  return value == 'y' or value == 'n'

for key, value in bool_variables.items():
  if not is_cli_bool(value):
    print(f'{key} must be one of "y" or "n"')
    exit(1)
