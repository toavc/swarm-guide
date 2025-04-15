# conf.py
import os
import sys

# Minimal required Sphinx settings
project = 'Swarm Guide' # Your project name
copyright = '2025'
author = 'SWARM'

# Required Sphinx stubs
extensions = []
master_doc = 'index' # Must point to the index.rst file (without extension)
language = 'en' # Set to English as requested
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The theme doesn't matter as its output will be overwritten,
# but Sphinx requires one to be specified. 'alabaster' is lightweight.
html_theme = 'alabaster'

# Ensure html_static_path does NOT point to your _static_html directory
# html_static_path = ['_static'] # Standard Sphinx value, can be left or commented out

# DO NOT USE THESE SETTINGS FOR YOUR MAIN FILES:
# html_extra_path = ['../_static_html'] # Commented out or removed
# html_additional_pages = {} # Commented out or removed