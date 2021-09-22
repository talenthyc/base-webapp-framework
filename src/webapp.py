"""
Entry point for the application
"""

# pylint: disable=unused-import
from . import app  # For application discovery by the 'flask' command.
from . import views  # For import side-effects of setting up routes.
