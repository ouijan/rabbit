import click
import os.path
from shutil import copyfile
from . import settings
from . import display

# Needs Tests
def addAll(app):
  """ 
  Add all flags to the given clickObj 
  """
  addInitFlag(app)
  addVersionFlag(app)

# Needs Tests
def addVersionFlag(app):
  """ 
  Add version flag to given clickObj 
  """
  click.version_option(
    version=app.version,
    prog_name=settings.NAME
  )(app.baseGroup.clickObj)

# Needs Tests
def addInitFlag(app):
  """ 
  Add init flag to given clickObj: 
  calls create_example 
  """
  click.option(
    '--init',
    is_flag=True, 
    callback=create_example,
    expose_value=False,
    is_eager=True
  )(app.baseGroup.clickObj)

# Needs Tests
def create_example(ctx, param, value):
  """
  Creates an example rabbit.yaml flie.
  Copies it from the rabbit storage path:
    etc/rabbit/example.yaml
  """
  if not value or ctx.resilient_parsing:
    return

  filename = settings.CONFIG_FILE;

  # Exit if file already exists
  if os.path.isfile(filename):
    display.error("%s file already exists" % filename)
    ctx.exit()

  try:
    # Attempt to Copy the File
    src = settings.CONFIG_DIR + "example.yaml"
    copyfile(src, filename)
    display.success("Successfully created %s file" % filename)

  except:
    # If there was an issue
    display.error("Couldn't create %s file" % filename)
    

  ctx.exit()