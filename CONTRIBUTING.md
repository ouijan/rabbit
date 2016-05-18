# Contributing

# To Do
- Group and Command Classes should share a parent that:
    - adds flags
    - handles click object
    - has fire call which is overriden
- Command variables in command['hop'] > command['to']
- Interpret multi line command 'to' arguments like a bash script
- Parse through all options to proxied command
- Adding group descriptions
- Currently only searches current directory. Should  look recursively at least 2 times.
- Testing:
  - Flags
    - addAll
    - addVersionFlag
    - addInitFlag
    - create_example
  - Group
    - __init__ (children, name, clickObj)
    - getClickObject
    - fire
    - add
    - resolveGroup
    - resolveGroups
  - App
    - getVersion

### Testing
Run the following command from project root directory to execute the test suite
This is best done from within your virtualenv

    $ tox

### Install
Run the following command from project root directory to execute the install script
This should be done from within your virtualenv
  
    $ python setup.py build && python setup.py install

### Updating Pip
This can be done by following [this guide](http://peterdowns.com/posts/first-time-with-pypi.html). Basicly ensure you are in the master branch and it has been version tagged then run:
  
    $ python setup.py sdist upload -r pypi
