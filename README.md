# Rabbit Command Line Hopper
Rabbit is a simple yaml based tool for command line actions. It will read a rabbit.yaml configuration file from the current directory and provide a list available commands.

## Installation
You will need to have Python and Pip [installed](http://python-packaging-user-guide.readthedocs.org/en/latest/installing/#requirements-for-installing-packages) then run the following command in your cli.
    
    $ pip install rabbit

## Usage
- Enter 'rabbit' or 'rab' in your command line
- Rabbit must be able to find a rabbit.yaml file in the current directory.
- 'rabbit --help' will display a list of all available rabbit commands

## Configuration
Rabbit will look for the closest rabbit.yaml file. This [yaml](http://docs.ansible.com/YAMLSyntax.html) file must contain a commands property. The commands property is a list of all commands to be proxied by rabbit. Simple as that!

```yaml
commands:
  - hop: npm install
    to: docker run -it --rm node npm install
    description: Runs 'npm install' on the current directory
  - hop: run node
    to: echo "Run Node"
    description: echos 'run node' to the command line
```

### Command 
- A command's 'hop' property represents the rabbit command to be entered.
- A command's 'to' property defines the actual command to be run in terminal.  
- All arguments provided after the rabbit 'hop' decleration will be appended to the proxied command.
- Commands that share a similar hop will be grouped for convinience.

### [Contributing](CONTRIBUTING.md)