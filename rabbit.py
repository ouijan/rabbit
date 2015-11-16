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
  'Command Line Hopper'

  def run(self, args):
    'Runs the array of arguments'
    subprocess.call(args);

  def read(self, inputFile):
    'Read the given yaml file and return it as a dict'
    stream = file(inputFile, 'r')
    value = yaml.load(stream)
    return value

  def findConfig(self):
    'finds the path to the closest config file'
    fileFound = False
    depth = 0
    while (fileFound == False and depth < config['searchDepth']):
      search = './'
      for index in range(depth):
        search += '../'
      search += config['fileName']
      if os.path.isfile(search):
        fileFound = search
      depth += depth + 1
    return fileFound

  def converStringToArgs(self, inputCall):
    preJoin = string.split(inputCall, " ")
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
    foundCommand = False
    for command in config['commands']:
      match = True
      mapArray = self.converStringToArgs(command['map'])
      if len(inputArgs) < len(mapArray):
        continue
      for index, arg in enumerate(mapArray):
        if arg != inputArgs[index]:
          match = False
      if match:
        foundCommand = command
    return foundCommand

  def proxyCommand(self, command, inputArgs):
    args = self.converStringToArgs(command['to'])
    tail = inputArgs[len(self.converStringToArgs(command['map'])):]
    args += tail
    return self.run(args)


# Command Line Interface Handler
class Cli:
  'A class to handle running the command line tool & parsing command line arguments'
  def __init__(self):
    args = sys.argv
    args.pop(0)
    yamlFile = Rabbit().findConfig()
    if yamlFile == False:
      print "Couldn't find " + config['fileName']
      exit()
    config = Rabbit().read(yamlFile)
    command = Rabbit().findCommandInConfig(args, config)
    if command == False:
      print "Couldn't find that command"
      exit()
    Rabbit().proxyCommand(command, args)    

if __name__ == "__main__":
  try:
    Cli()
  except KeyboardInterrupt:
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)