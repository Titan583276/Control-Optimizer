# ------------------------------------------------------------------------------
# Project:       Control Optimizer
# Module:        validation_result.py
# Description:   Defines the ValidationResult class.
#
# Authors:       Florin Buechi, Thomas Staehli
# ------------------------------------------------------------------------------
from dataclasses import dataclass


@dataclass
class ValidationResult:
    valid: bool
    message: str | None = None
