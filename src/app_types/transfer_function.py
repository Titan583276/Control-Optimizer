# ------------------------------------------------------------------------------
# Project:       Control Optimizer
# Module:        transfer_function.py
# Description:   Defines the TransferFunctions class.
#
# Authors:       Florin Buechi, Thomas Staehli
# ------------------------------------------------------------------------------
from dataclasses import dataclass


@dataclass
class TransferFunctions:
    plant: str
    controller: str
    open_loop: str
    closed_loop: str
    sensitivity: str