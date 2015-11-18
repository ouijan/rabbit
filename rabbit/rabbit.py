#!.env/bin/python
import yaml
import subprocess
import os
import sys
import string

config = {
  'fileName': 'rabbit.yaml',
  'searchDepth': 3,
}

class Rabbit(object):
  """Command Line Hopper"""

  def run(self, command):
    """Runs the string of command"""
    subprocess.call(command, shell=True);

  def read(self, inputFile):
    """Read the given yaml file and return it as a dict"""
    stream = file(inputFile, 'r')
    value = yaml.load(stream)
    return value

  def findConfig(self):
    """searches for the config file based on the current working directory"""
    fileFound = False
    depth = 0
    while (fileFound == False and depth < config['searchDepth']):
      search = './'
      for index in range(depth):
        search += '../'
      search += config['fileName']
      if os.path.isfile(search):
        fileFound = search
      depth += 1
    return fileFound

  def converStringToArgs(self, inputCall):
    """Converts a string command into the required list of args"""
    # print inputCall
    args = []
    current = ""
    trackingString = False
    escaped = False
    for char in inputCall:

      if not trackingString:

        # Add to args
        if char.isspace():
          args.append(current)
          current = ""
          continue

        # start tracking string
        if char == '"' or char == "'":
          trackingString = char

        current += char

      else:

        # handle escaped chars
        if "\\" + char == "\\":
          print 'escape found'
          escaped = True

        # stop tracking a string
        if not escaped and char == trackingString:
          trackingString = False

        current += char

    args.append(current)
    return args

  def findCommandInConfig(self, inputArgs, config):
    """searches for the command for the given args in the config"""
    for command in config['commands']:
      match = True
      mapArray = self.converStringToArgs(command['hop'])
      if len(inputArgs) < len(mapArray):
        continue
      for index, arg in enumerate(mapArray):
        if arg != inputArgs[index]:
          match = False
      if match:
        return command
    return False

  def proxyCommand(self, command, inputArgs):
    """handles editing and running the command"""
    args = self.converStringToArgs(command['to'])
    tail = inputArgs[len(self.converStringToArgs(command['hop'])):]
    args += tail
    args = " ".join(args)
    return self.run(args)

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
    args = sys.argv[1:]
    yamlFile = Rabbit().findConfig()
    if not yamlFile:
      print "Couldn't find " + config['fileName']
      exit()
    config = Rabbit().read(yamlFile)
    if len(args) == 0 or args[0] == "help":
      Rabbit().displayHelp(config)
      exit()
    command = Rabbit().findCommandInConfig(args, config)
    if not command:
      print "Couldn't find that command. Try 'rabbit help'"
      exit()    
    Rabbit().proxyCommand(command, args)

  except KeyboardInterrupt:
    exit()

if __name__ == "__main__":
  main()