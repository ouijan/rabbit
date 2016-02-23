#!.env/bin/python
from models.App import *
import click


@click.command()
def main():
  """Main entrypoint to the application"""
  app = App()
  print(app.config.get('commands', 'Fuck it'))
  click.echo('Hi There')
  

# Handle running the script directly
if __name__ == '__main__':
  main()