# Rabbit Command Line Hopper
A simple yaml based proxy for command line actions

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

### Usage
- All arguments provided after the rabbit 'hop' decleration will be forwarded to the proxied command
- 'rabbit help' will display a list of all available rabbit commands

## To Do
- Implement command proxy
  - command argument 
  - evaluating variable functions eg '${docker-machine ip default}'
- 'rabbit help' should be a reserved command that lists all rabbit commands. It will display each command's description property OR their to property if a description is not set


### Testing
Run the following command from project root directory to execute the test suite

	$ python -m unittest discover tests -v

### Required Packages
- [PyYaml](http://pyyaml.org/)

