import yaml
from pathlib import Path

# Config file is located in the top-level `config` directory
CONFIG_PATH = Path("config/config.yaml")


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)
