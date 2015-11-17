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
  - proxying command variables
  - rewrite convertStrToArgs to walk though string generating args
  - Revisit env parsing
    - Look into parsing environmental vars to the subproccess.call()
- Investigate python pbr for setup.py generation etc
- Improve test framework


### Testing
Run the following command from project root directory to execute the test suite

	$ python -m unittest discover tests -v

### Required Packages
- [PyYaml](http://pyyaml.org/)

