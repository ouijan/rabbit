#!venv/bin/python
import yaml
import subprocess
import argparse
import os

class Rabbit(object):
  'Command Line Hopper'

# Command Line Interface Handler
class Cli:
  'A class to handle running the command line tool & parsing command line arguments'
  def __init__(self):
    print 'Running Peon...'
    parser = argparse.ArgumentParser(description='Yaml parser.');
    parser.add_argument('filepath', metavar='filepath', help='yaml file path for peon to proccess')
    args = vars(parser.parse_args())
    inputFile = args['filepath']
    Peon().update(inputFile);
    

if __name__ == "__main__":
  Cli()