# Rabbit Command Line Hopper
A simple yaml based proxy for command line actions

## Configuration
Rabbit will look for the closest rabbit.yaml file. This [yaml format](http://docs.ansible.com/YAMLSyntax.html) must contain a commands property. Thie commands property contains a list of all commands to be proxied by rabbit. A site's 'map' property represents the rabbit arguments and the commands 'to' property defines the actual command to be run in terminal. Simple as that!

```yaml
commands:
  - map: npm install
    to: docker run -it --rm node npm install
    description: Runs 'npm install' on the current directory
  - map: run node
    to: echo "Run Node"
    description: echos 'run node' to the command line
```

## Usage
- All arguments provided after the rabbit 'map' decleration will be forwarded to the proxied command
- 'rabbit help' will display a list of all available rabbit commands

### To Do
- Implement ymal reading
- Implement command proxy
- 'rabbit help' should be a reserved command that lists all rabbit commands. It will display each command's description property OR their to property if a description is not set

## Required Packages
- [PyYaml](http://pyyaml.org/)

