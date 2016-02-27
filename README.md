# Rabbit Command Line Hopper
A simple yaml based proxy for command line actions

## Usage
- rabbit must be able to find a rabbit.yaml file. It will search the current directory and then 2 parent directories
- 'rabbit help' will display a list of all available rabbit commands
- All arguments provided after the rabbit 'hop' decleration will be appended to the proxied command

## Configuration
Rabbit will look for the closest rabbit.yaml file. This [yaml](http://docs.ansible.com/YAMLSyntax.html) file must contain a commands property. The commands property is a list of all commands to be proxied by rabbit. A command's 'hop' property represents the rabbit arguments and the command's 'to' property defines the actual command to be run in terminal. Simple as that!

```yaml
commands:
  - hop: npm install
    to: docker run -it --rm node npm install
    description: Runs 'npm install' on the current directory
  - hop: run node
    to: echo "Run Node"
    description: echos 'run node' to the command line
```

## To Do
- Command variables in command['hop'] > command['to']
- Interpret multi line command 'to' arguments like a bash script
- Parse through all options to proxied command
- Adding group descriptions
- Improve test framework
  - Group
  - Command


### Testing
Run the following command from project root directory to execute the test suite
This is best done from within your virtualenv
  $ tox

### Install
Run the following command from project root directory to execute the install script
This is best done from within your virtualenv
  $  python setup.py build && python setup.py install

### Required Packages
- [Click](http://pyyaml.org/)
- [PyYaml](http://click.pocoo.org/)


