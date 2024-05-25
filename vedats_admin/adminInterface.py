from BaseModel import *

@click.group()
def poem_intf():
    """A basic command line admin interface."""
    pass

@poem_intf.command()
@click.argument('poem')
@click.option('--poet', prompt="poet name", help="Input the poet name, \nif you don't code will still run, \nif the poet doens't exit it will created and put into database")
def add_poem(poet, poem):
    click.echo(f'poet: {poet}\npoem: {poem}') # comment out later
    message = Poem.add(poem, poet) # this should handle poet add as well 
    click.echo(message)
    """add poem"""
    #this should run the function to add the poem name into the database
    pass

if __name__ == '__main__':
    poem_intf()
