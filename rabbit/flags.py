import click
import os.path
from shutil import copyfile
from . import settings

# Needs Tests
def addAll(clickObj):
  """ Add all flags to the given clickObj """
  addInitFlag(clickObj)
  addVersionFlag(clickObj)

# Needs Tests
def addVersionFlag(clickObj):
  """ Add version flag to given clickObj """
  click.version_option(
    version=settings.VERSION,
    prog_name=settings.NAME
  )(clickObj)

# Needs Tests
def addInitFlag(clickObj):
  click.option(
    '--init',
    is_flag=True, 
    callback=create_example,
    expose_value=False,
    is_eager=True
  )(clickObj)

# Needs Tests
def create_example(ctx, param, value):
  if not value or ctx.resilient_parsing:
    return
    
  filename = settings.CONFIG_FILE;

  # Exit if file already exists
  if os.path.isfile(filename):
    msg = "%s file already exists" % filename
    click.echo(click.style(msg, fg='red'))
    ctx.exit()

  try:
    # Attempt to Copy the File
    src = settings.CONFIG_DIR + "example.yaml"
    copyfile(src, filename)
    msg = "Successfully created %s file" % filename
    click.echo(click.style(msg, fg='green'))

  except:
    # If there was an issue
    msg = "Couldn't create %s file" % filename
    click.echo(click.style(msg, fg='red'))

  ctx.exit()