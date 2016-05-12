import click

def welcome():
	""" display a generic welcome message """
	welcome = click.style('Rabbit', fg='cyan')
	welcome += click.style(' - Command Line Hopper', fg='cyan')
	click.echo(welcome)

def error(message):
	""" display a red error message """
	echo(message, 'red')

def success(message):
	""" display a green success message """
	echo(message, 'green')

def echo(message, color):
	""" display a message of the given colour """
	styled = click.style(message, fg=color)
	click.echo(styled)	