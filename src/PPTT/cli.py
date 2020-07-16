import json
import os

import click

from .ppt import make_ppt
from .replace.stub import make_stub
from .type import InputData


@click.group()
def cli():
    pass


def get_input_file(input_file_path: str) -> InputData:
    with open(input_file_path, mode='r') as fp:
        raw = json.load(fp)
        if isinstance(raw, list):
            result = {"pages": raw}
        else:
            result = raw
    return result


@click.command("make_ppt", short_help="Run a development server.")
@click.argument('master_file', type=click.Path(exists=True, resolve_path=True))
@click.argument('target_file', type=click.Path(exists=False, resolve_path=True))
@click.option('--mode', '-m', default='replace', help='how to make ppt? replace,template')
@click.option("--input", "-i", help="input data", type=click.Path(exists=True, resolve_path=True))
def make_ppt_command(master_file, target_file, mode, input):
    input_data = get_input_file(input)
    try:
        make_ppt(master_file, target_file, mode=mode, **input_data)
        print(f'make ppt success! check {target_file}')
    except Exception as e:
        print('fail to make ppt')
        print(e)


@click.command("make_stub", short_help="Run a development server.")
@click.argument('master_file', type=click.Path(exists=True, resolve_path=True))
@click.option('--mode', '-m', default='replace', help='how to make ppt? replace,template')
@click.option('--output', '-o', type=click.Path(exists=False, resolve_path=True))
def make_stub_command(master_file, mode, output=''):
    output_path = output or os.path.join(os.path.dirname(master_file), 'slide_stubs.py')
    if mode == 'replace':
        make_stub(master_file, output_path)
    else:
        raise NotImplementedError('un support mode')


cli.add_command(make_ppt_command)
cli.add_command(make_stub_command)
if __name__ == '__main__':
    cli()
