# ------------------------------------------------------------------------------
# Project:       Control Optimizer
# Module:        settings.py
# Description:   Defines the LanguageType class.
#
# Authors:       Florin Buechi, Thomas Staehli
# ------------------------------------------------------------------------------
from enum import Enum


class LanguageType(Enum):
    ENGLISH = "en"
    GERMAN = "de"


class ThemeType(Enum):
    DARK = "dark"
    LIGHT = "light"
