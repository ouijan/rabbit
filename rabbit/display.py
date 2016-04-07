import click

def welcome():
	welcome = click.style('Rabbit', fg='cyan')
	welcome += click.style(' - Command Line Hopper', fg='cyan')
	click.echo(welcome)