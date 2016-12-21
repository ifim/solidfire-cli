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

@cli.command('modify', short_help="ModifyClusterFullThreshold")
@click.argument('stage2_aware_threshold', type=int, required=False)
@click.argument('stage3_block_threshold_percent', type=int, required=False)
@click.argument('max_metadata_over_provision_factor', type=int, required=False)
@pass_context
def modify(ctx, stage2_aware_threshold = None, stage3_block_threshold_percent = None, max_metadata_over_provision_factor = None):
    """ModifyClusterFullThreshold is used to change the level at which an event is generated when the storage cluster approaches the capacity utilization requested. The number entered in this setting is used to indicate the number of node failures the system is required to recover from. For example, on a 10 node cluster, if you want to be alerted when the system cannot recover from 3 nodes failures, enter the value of &quot;3&quot;. When this number is reached, a message alert is sent to the Event Log in the Cluster Management Console."""
    ModifyClusterFullThresholdResult = ctx.element.modify_cluster_full_threshold(stage2_aware_threshold=stage2_aware_threshold, stage3_block_threshold_percent=stage3_block_threshold_percent, max_metadata_over_provision_factor=max_metadata_over_provision_factor)
    print(json.dumps(json.loads(jsonpickle.encode(ModifyClusterFullThresholdResult)),indent=4))

