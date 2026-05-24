# ------------------------------------------------------------------------------
# Project:       Control Optimizer
# Module:        info_banner.py
# Description:   Defines the InfoBanner class.
#
# Authors:       Florin Buechi, Thomas Staehli
# ------------------------------------------------------------------------------
from .base_banner import BaseBanner


class InfoBanner(BaseBanner):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setProperty("bannerType", "info")
