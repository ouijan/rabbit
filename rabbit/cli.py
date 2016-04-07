import click
import display
from app import *



def main():
  """Main entrypoint to the application"""
  app = App()
  app.run()

  
# Handle running the script directly
if __name__ == '__main__':
  main()
