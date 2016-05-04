import click
from . import app

def main():
  """Main entrypoint to the application"""
  myApp = app.App()
  myApp.run()

# Handle running the script directly
if __name__ == '__main__':
  main()
