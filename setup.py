from setuptools import setup
from configparser import RawConfigParser
from json import loads


cfg_file: str = r"setup.cfg"
parse_tup = lambda op: (op[0], loads(op[1]))
with open(cfg_file) as cfg:
    # create parser and read the setup.cfg file
    parser = RawConfigParser()
    parser.read_file(cfg)
    opts: list = parser["setup"].items()
    # evaluated options
    val_opts: dict = dict(map(parse_tup, opts))
    
    # setup
    setup(
        **val_opts
    )

