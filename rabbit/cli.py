import click
import rabbit.display
from rabbit.app import *



def main():
  """Main entrypoint to the application"""
  app = App()
  app.run()

  
# Handle running the script directly
if __name__ == '__main__':
  main()
