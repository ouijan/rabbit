#!.env/bin/python
from models.app import *
import click


@click.command()
def main():
  """
  Main entrypoint to the application
  """
  app = App()
  click.echo('Hi There')
  

# Handle running the script directly
if __name__ == '__main__':
  main()