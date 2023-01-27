"""Global values for scargo"""
import pkgutil
from pathlib import Path

__version__ = "1.0.0"

DESCRIPTION = "C/C++ package and software development life cycle manager based on RUST cargo idea."

SCARGO_PGK_PATH = (
    Path(pkgutil.get_loader("scargo").path).parent
    if pkgutil.get_loader("scargo").path
    else Path(Path(__file__).absolute()).parent
)
SCARGO_DEFAULT_BUILD_ENV = "docker"
SCARGO_DOCKER_ENV = "docker"

SCARGO_LOCK_FILE = "scargo.lock"
SCARGO_DEFAULT_CONFIG_FILE = "scargo.toml"
ENV_DEFAULT_NAME = ".env"