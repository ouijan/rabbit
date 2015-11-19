# Rabbit Command Line Hopper
A simple yaml based proxy for command line actions

## Usage
- rabbit must be able to find a rabbit.yaml file. It will search the current directory and then 2 parent directories
- 'rabbit help' will display a list of all available rabbit commands
- All arguments provided after the rabbit 'hop' decleration will be appended to the proxied command

## Configuration
Rabbit will look for the closest rabbit.yaml file. This [yaml format](http://docs.ansible.com/YAMLSyntax.html) must contain a commands property. Thie commands property contains a list of all commands to be proxied by rabbit. A site's 'hop' property represents the rabbit arguments and the commands 'to' property defines the actual command to be run in terminal. Simple as that!

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
- Implement command proxy
  - Break into classes
    - Display: handle printing to console
      - help
      - colours
    - Command: a command object
      - matches
    - Config: Keeps track of configs
      - find
      - loadConfig
      - getConfig
  - handle multiple/compound configs
    - priority: current folder > global
  - proxying command variables in command['hop'] > command['to']
  - rewrite convertStrToArgs to walk though string generating args
    - Does it need to be an array at all? probably not
- Read home directory for rabbit.yaml and join to list of commands
  - Project commands > global commands
- Interpret multi line command 'to' arguments like a bash script
- Improve test framework
  - add py34 to tox testing
- Grouping of commands in "family" for help.
  - Namespaced with .
  - Recognise commands in a family and auto generate help for them


### Testing
Run the following command from project root directory to execute the test suite

	$ python -m unittest discover tests -v

### Required Packages
- [PyYaml](http://pyyaml.org/)

