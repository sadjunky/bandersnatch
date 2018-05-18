"""
Module containing classes to access the bandersnatch configuration file
"""
import pkg_resources
from configparser import ConfigParser


class Singleton(type):  # pragma: no cover
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls
            ).__call__(*args, **kwargs)
        return cls._instances[cls]


class BandersnatchConfig(metaclass=Singleton):
    def __init__(self, config_file=None):
        """
        Bandersnatch configuration class singleton

        This class is a singleton that parses the configuration once at the
        start time.

        Parameters
        ==========
        config_file: str, optional
            Path to the configuration file to use
        """
        self.default_config_file = pkg_resources.resource_filename(
            'bandersnatch', 'default.conf'
        )
        self.config_file = config_file
        self.load_configuration()

    def load_configuration(self):
        """
        Read the configuration from the configuration files
        """
        config_files = [self.default_config_file]
        if self.config_file:
            config_files.append(self.config_file)
        self.config = ConfigParser()
        self.config.read(config_files)
