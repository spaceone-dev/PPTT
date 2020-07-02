import json
from pprint import pprint

import click

from .parser import parser
from .ppt import make_ppt
from .schema import PPTTemplate


@click.group()
def cli():
    pass


@click.command("make_schema", short_help="Run a development server.")
@click.argument('file', type=click.Path(exists=True, resolve_path=True))
@click.option("--output", "-o", help="save the output to file", type=click.Path(exists=False, resolve_path=True))
@click.option('--verify', default=True, type=bool)
def make_schema(file, verify, output=None, ):
    template = parser(file)
    dump = PPTTemplate().dump(template)
    pprint(dump)
    if output:
        with open(output, mode='w')as fp:
            fp.write(json.dumps(dump, indent=2))


@click.command("make_ppt", short_help="Run a development server.")
@click.argument('master_file', type=click.Path(exists=True, resolve_path=True))
@click.argument('target_file', type=click.Path(exists=False, resolve_path=True))
@click.option("--input", "-i", help="input data", type=click.Path(exists=True, resolve_path=True))
def make_ppt_command(master_file, target_file, input):
    with open(input, mode='r') as fp:
        pages = json.load(fp)
    make_ppt(master_file, target_file, pages)


cli.add_command(make_schema)
cli.add_command(make_ppt_command)
if __name__ == '__main__':
    cli()
