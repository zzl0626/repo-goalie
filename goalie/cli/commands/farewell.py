import typer

app = typer.Typer()

@app.command()
def farewell(
    name: str = typer.Option(
        ...,
        "--name",
        "-n",
        help="The name of the person to bid farewell to"
    ), 
    formal: bool = typer.Option(
        False,
        "--formal",
        "-f",
        help="Use a formal farewell"  
    )
):
    """
    Say goodbye to someone.
    """
    if formal:
        typer.echo(f"Good Bye {name}.")
    else:
        typer.echo(f"Bye {name}!")

