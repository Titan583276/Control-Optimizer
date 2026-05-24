# ------------------------------------------------------------------------------
# Project:       Control Optimizer
# Module:        __init__.py
# Description:   Initializes the svg package.
#
# Authors:       Florin Buechi, Thomas Staehli
# ------------------------------------------------------------------------------
from .svg_utils import (
    recolor_svg,
    merge_svgs,
    svg_to_icon,
    SvgLayer,
    save_svg,
    latex_to_svg,
)

__all__ = [
    # svg utils
    "recolor_svg",
    "merge_svgs",
    "svg_to_icon",
    "SvgLayer",
    "save_svg",
    "latex_to_svg",
]
