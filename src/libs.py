import argparse
import os
import subprocess
import scapy.all as scapy
import sys
import pandas
from time import sleep

ANSI = {
        'RED' : '\033[;31m',
        'GREEN': '\033[;32m',
        'BLUE': '\033[;34m',
        'PURPLE': '\033[0;35m',
        'LIGHT_RED': '\033[1;31m',
        'LIGHT_GREEN': '\033[1;32m',
        'LIGHT_BLUE': '\033[1;34m',
        'YELLOW': '\033[1;33m',
        'BOLD': '\033[1m',
        'END': '\033[0m',
        }

