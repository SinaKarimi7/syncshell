#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# syncshell.py.__main__: execute main function directly
__author__ = "Masoud Ghorbani <msud.ghorbani@gmail.com>"

from fire import Fire
from cli import Application

def main():
    Fire(Application)

if __name__ == "__main__":
    main()
