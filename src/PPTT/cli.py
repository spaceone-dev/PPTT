import json
import os
from pprint import pprint

import click
from pptx import Presentation

from .parser import parser
from .ppt import make_ppt
from .schema import PPTTemplate
from .stub import PPTTemplateStub


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


@click.command("make_stub", short_help="Run a development server.")
@click.argument('master_file', type=click.Path(exists=True, resolve_path=True))
@click.option('--output', '-o', type=click.Path(exists=False, resolve_path=True))
def make_stub_command(master_file, output=''):
    master_ppt = Presentation(master_file)
    template = PPTTemplateStub.load_by_pptx(master_ppt)
    output_path = output or os.path.join(os.path.dirname(master_file), 'slide_stubs.py')
    template.to_file(output_path)


cli.add_command(make_schema)
cli.add_command(make_ppt_command)
cli.add_command(make_stub_command)
if __name__ == '__main__':
    cli()
