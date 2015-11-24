#!.env/bin/python
import sys
from os.path import expanduser
from command import Command
from config import Config
      
def main():
  """Main entrypoint to the application"""
  try:
    
    # Get input arguments
    args = sys.argv[1:]
    givenCommand = " ".join(args)

    # Load config
    config = Config()
    # Global
    globalConfig = config.read(expanduser("~") + "/" + config.fileName)
    config.load(globalConfig)
    # Local
    localConfig = config.read(config.find())
    config.load(localConfig)

    # Show Help
    if len(args) == 0 or args[0] == "help":
      config.displayHelp()
      exit()

    # Find the command
    command = config.findCommand(givenCommand)
    if command is None:
      print "Couldn't fond that command"
      config.displayHelp()
      exit()

    # Run the command
    command.run(givenCommand)

  # Handle Keyboard Interrupt
  except KeyboardInterrupt:
    exit()

# Handle running the script directly
if __name__ == "__main__":
  main()