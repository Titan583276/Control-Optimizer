# ------------------------------------------------------------------------------
# Project:       Control Optimizer
# Module:        navigation.py
# Description:   Defines the NavLabels class.
#
# Authors:       Florin Buechi, Thomas Staehli
# ------------------------------------------------------------------------------
from dataclasses import dataclass
from enum import Enum

class NavLabels(Enum):
    PLANT = "Plant"
    EXCITATION_FUNCTION = "Excitation Function"
    CONTROLLER = "Controller"
    PSO_PARAMETER = "PSO Parameter"
    EVALUATION = "Evaluation"
    SIMULATION = "Simulation"
    DATA_MANAGEMENT = "Data Management"
    HELP = "Help"
    SETTINGS = "Settings"


@dataclass
class NavItem:
    key: NavLabels
    icon: str
    bottom: bool = False
