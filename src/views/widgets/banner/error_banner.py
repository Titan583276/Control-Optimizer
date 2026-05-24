# ------------------------------------------------------------------------------
# Project:       Control Optimizer
# Module:        error_banner.py
# Description:   Defines the ErrorBanner class.
#
# Authors:       Florin Buechi, Thomas Staehli
# ------------------------------------------------------------------------------
from .base_banner import BaseBanner


class ErrorBanner(BaseBanner):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setProperty("bannerType", "error")
