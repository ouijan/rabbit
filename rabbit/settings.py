import sys

# Settings
NAME = "rabbit"
CONFIG_FILE = NAME + ".yaml"
CONFIG_DIR = "etc/rabbit"

# Variable Refinement
CONFIG_DIR = sys.prefix + "/" + CONFIG_DIR + "/"
