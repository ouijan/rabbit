#!.env/bin/python
import sys
from os.path import expanduser
from command import Command
from config import Config

def displayHelp(self, config):
  """translates config into help and prints it"""
  print "\033[1m\033[4m\033[32mRabbit Command Line Hopper \033[0m"
  for command in config['commands']:
    default = "runs '" + command['to'] + "'"
    description = command.get('description', default)
    print "\033[1m\033[36m%-20s \033[0m %-10s" % (command['hop'], description)
      
def main():
  """Main entrypoint to the application"""
  try:
    
    # Get input arguments
    args = sys.argv[1:]

    config = Config()
    globalConfig = expanduser("~") + "/" + config.fileName

    # config.load(globalConfig)
    # config.load(globalConfig)

    # Show Help
    if len(args) == 0 or args[0] == "help":
      displayHelp(config)
      exit()

    # Find the command
    
    # Run the command

    

  # Handle Keyboard Interrupt
  except KeyboardInterrupt:
    exit()

# Handle running the script directly
if __name__ == "__main__":
  main()