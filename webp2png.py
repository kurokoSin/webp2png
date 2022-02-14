#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click 
from   _main import Webp2Png

@click.command()
@click.argument('zip_path', type=click.Path(exists=True))
def cmd(zip_path):
    Webp2Png.controller(zip_path)

if __name__ == '__main__':
    cmd()


