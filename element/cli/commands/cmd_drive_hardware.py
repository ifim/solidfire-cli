#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#

import click

from element.cli import utils as cli_utils
from element.cli.cli import pass_context
from element.solidfire_element_api import SolidFireRequestException
from element import utils
import jsonpickle
import json

@click.group()
@pass_context
def cli(ctx):
    """Account methods."""
    ctx.sfapi = ctx.client

@cli.command('list', short_help="ListDriveHardware")
@click.argument('force', type=bool, required=True)
@pass_context
def list(ctx, force):
    """ListDriveHardware returns all the drives connected to a node. Use this method on the cluster to return drive hardware information for all the drives on all nodes."""
    ListDriveHardwareResult = ctx.element.list_drive_hardware(force=force)
    print(json.dumps(json.loads(jsonpickle.encode(ListDriveHardwareResult)),indent=4))

