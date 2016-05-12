import sys

# Settings
NAME = "rabbit"
VERSION = "v1.1.31"
CONFIG_FILE = NAME + ".yaml"
CONFIG_DIR = "etc/rabbit"

# Variable Refinement
CONFIG_DIR = sys.prefix + "/" + CONFIG_DIR + "/"