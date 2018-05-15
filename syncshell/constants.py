#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# constants.py: contain syncshell's consts
import os
from pathlib import Path
import re

# Metainfo
APP_NAME = 'syncshell'

# Log
LOG = {
    'level': 'INFO',
    'format': '↳ %(levelname)s - %(message)s'
}

# Paths
APP_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))  # noqa
CONFIG_FILENAME = '.syncshell.ini'
CONFIG_PATH_TEMPLATE = '{}/{}'.format(APP_ROOT_DIR, CONFIG_FILENAME)
CONFIG_PATH = '{}/{}'.format(Path.home(), CONFIG_FILENAME)

# String Colors
DEFAULT = '\033[39m'
WHITE = '\033[97m'

# String Attr
NORMAL = '\033[0m'
BOLD = '\033[1m'

# Shell
SHELL_PATH = os.readlink('/proc/{}/exe'.format(os.getppid()))
SHELL = re.search(r"([^/]*$)", SHELL_PATH).group()

# History
HISTORY_PATH = {
    'bash': '.bash_history',
    'zsh': '.zsh_history',
}
