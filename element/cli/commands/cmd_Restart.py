#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#

import click

from element.cli import utils as cli_utils
from element.cli import parser
from element.cli.cli import pass_context
from element.solidfire_element_api import SolidFireRequestException
from element import utils
import jsonpickle
import simplejson
from uuid import UUID


@click.group()
@pass_context
def cli(ctx):
    """ResetNode RestartNetworking RestartServices Shutdown """
    ctx.sfapi = ctx.client

@cli.command('ResetNode', short_help="ResetNode")
@click.option('--build',
              type=str,
              required=True,
              help="""Used to specify the URL to a remote Element software image to which the node will be reset. """)
@click.option('--force',
              type=bool,
              required=True,
              help="""The force parameter must be included in order to successfully reset the node. """)
@click.option('--option',
              type=str,
              required=True,
              help="""Used to enter specifications for running the reset operation. """)
@pass_context
def ResetNode(ctx,
           build,
           force,
           option):
    """Allows you to reset a node to the SolidFire factory settings. All data will be deleted from the node when you call this method. A node participating in a cluster cannot be reset."""



    ResetNodeResult = ctx.element.reset_node(build=build, force=force, option=option)
    cli_utils.print_result(ResetNodeResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('RestartNetworking', short_help="RestartNetworking")
@click.option('--force',
              type=bool,
              required=True,
              help="""The "force" parameter must be included on this method to successfully restart the networking. """)
@pass_context
def RestartNetworking(ctx,
           force):
    """The RestartNetworking API method is used to restart the networking services on a node.WARNING! This method restarts all networking services on a node, causing temporary loss of networking connectivity. Exercise caution when using this method."""



    dict = ctx.element.restart_networking(force=force)
    cli_utils.print_result(dict, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('RestartServices', short_help="RestartServices")
@click.option('--force',
              type=bool,
              required=True,
              help="""The "force" parameter must be included on this method to successfully restart services on a node.    """)
@click.option('--service',
              type=str,
              required=False,
              help="""Service name to be restarted. """)
@click.option('--action',
              type=str,
              required=False,
              help="""Action to perform on the service (start, stop, restart). """)
@pass_context
def RestartServices(ctx,
           force,
           service = None,
           action = None):
    """The RestartServices API method is used to restart the  Element services on a node.Caution: This method causes temporary node services interruption. Exercise caution when using this method."""



    dict = ctx.element.restart_services(force=force, service=service, action=action)
    cli_utils.print_result(dict, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Shutdown', short_help="Shutdown")
@click.option('--option',
              type=str,
              required=True,
              help="""Action to take for the node shutdown:restart: Restarts the node.halt: Performs full power-off of the node. """)
@pass_context
def Shutdown(ctx,
           option):
    """The Shutdown API method enables you to restart or shutdown a node that has not yet been added to a cluster. To use this method, login in to the MIP for the pending node and enter the &quot;shutdown&quot; method with either the &quot;restart&quot; or &quot;halt&quot; options in the following table."""



    ShutdownResult = ctx.element.shutdown(option=option)
    cli_utils.print_result(ShutdownResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

