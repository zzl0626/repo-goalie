import typer

app = typer.Typer()

@app.command()
def greet(
    name: str = typer.Option(
        ...,
        "--name",
        "-n",
        help="The name of the person to greet"
    ), 
    formal: bool = typer.Option(
        False,
        "--formal",
        "-f",
        help="Use a formal greeting"    
    )
):
    """
    Say hello to someone.
    """
    if formal:
        typer.echo(f"Good day, {name}.")
    else:
        typer.echo(f"Hey {name}!")

