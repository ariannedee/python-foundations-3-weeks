"""
Creating command line applications using the click library
Install using $ pip install click
"""
import click


@click.command()
@click.argument('num', default=1)         # integer
@click.option('--shout', is_flag=True)    # boolean
@click.option('--name', prompt='Your name', help='The person to greet.')  # user input
def hello(num, name, shout):
    greeting = f'Hello {name}'
    if shout:
        greeting = greeting.upper()
    for i in range(num):
        print(greeting)


hello()
