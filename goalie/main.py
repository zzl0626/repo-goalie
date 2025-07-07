import typer
import logging
from goalie.cli.commands import greet, farewell

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("goalie.main")

app = typer.Typer(help="CLI for Repo Goalie")

app.command(name="greet")(greet)
app.command(name="farewell")(farewell)


def main():
    """
    Main entry point for the CLI application.
    """
    logger.info("Starting Repo Goalie CLI")
    app()
    logger.info("Repo Goalie CLI finished execution")

if __name__ == "__main__":
    main()