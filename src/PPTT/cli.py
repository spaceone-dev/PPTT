import sys
from os.path import dirname

import click


@click.group()
def cli():
    pass


@click.command("run", short_help="Run a development server.")
@click.argument('file', type=click.Path(exists=True, resolve_path=True), default="app.py")
@click.option("--host", "-h", default="127.0.0.1", help="The interface to bind to.")
@click.option("--port", "-p", default='50051', help="The port to bind to.")
@click.option('--worker', '-w', default=10, type=int)
# @click.option(
#     "--reload/--no-reload",
#     default=None,
#     help="Enable or disable the reloader. By default the reloader "
#          "is active if debug is enabled.",
# )
@click.option(
    "--debug",
    default=False,
    help="Server Debug Mode",
)
def run_command(file, host, port, worker, debug):
    sys.path.append(dirname(file))
    import importlib.util

    spec = importlib.util.spec_from_file_location("app", file)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)

    from .server import Server
    Server(host, port, worker).run()


cli.add_command(run_command)

if __name__ == '__main__':
    cli()
