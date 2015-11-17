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

  def run(self, args):
    """Runs the array of arguments"""
    subprocess.call(args);

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
    preJoin = inputCall.split()
    args = []
    trackingString = False
    thisArg = ''
    for item in preJoin:
      # If tracking an argument
      if trackingString:
        thisArg = " ".join((thisArg, item))
        # If string ends with "
        if item[-1:] == '"' or item[-1:] == "'":
          args.append(thisArg)
          trackingString = False
      # If not tracking argument
      else:
        # If string begins with "
        if item[:1] == '"' or item[:1] == "'":
          trackingString = True
          thisArg = item
        else:
          args.append(item)
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

  def injectEnvVariables(self, commandArgs):
    """handles injecting environmental variables to the arguement"""
    newArgs = []
    for arg in commandArgs:
      try:
        varStart = arg.index("$") + 1
        varEnd = arg.find(" ", varStart) + 1
        if varEnd <= 0: varEnd = len(arg)
        find = arg[varStart:varEnd]
        injected = os.environ.get(find)
        newArg = arg.replace(find, injected)
        newArg = newArg.replace("$", "", 1)
        newArgs.append(newArg)
      except:
        newArgs.append(arg)
        continue
    return newArgs

  def proxyCommand(self, command, inputArgs):
    """handles editing and running the command"""
    args = self.converStringToArgs(command['to'])
    tail = inputArgs[len(self.converStringToArgs(command['hop'])):]
    args += tail
    args = self.injectEnvVariables(args)
    return self.run(args)


# Command Line Interface Handler
class Cli:
  """A class to handle running the command line tool & parsing command line arguments"""
  def __init__(self):
    args = sys.argv[1:]
    yamlFile = Rabbit().findConfig()
    if not yamlFile:
      print "Couldn't find " + config['fileName']
      exit()
    config = Rabbit().read(yamlFile)
    command = Rabbit().findCommandInConfig(args, config)
    if not command:
      print "Couldn't find that command"
      exit()
    Rabbit().proxyCommand(command, args)    

if __name__ == "__main__":
  try:
    Cli()
  except KeyboardInterrupt:
    exit()