# ------------------------------------------------------------------------------
# Project:       Control Optimizer
# Module:        function_model.py
# Description:   Defines the FunctionModel class.
#
# Authors:       Florin Buechi, Thomas Staehli
# ------------------------------------------------------------------------------
from dataclasses import dataclass

from app_domain.functions import BaseFunction


@dataclass
class FunctionModel:
    selected_function: BaseFunction
