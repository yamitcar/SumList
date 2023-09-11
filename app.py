import cProfile

from src.adapters.cli import Cli

app = Cli()

cProfile.run("app.start()")
