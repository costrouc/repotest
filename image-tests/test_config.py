import sys
import shutil


def test_path():
    # assume that python path
    assert sys.prefix == '/srv/conda/envs/notebook'


def test_conda():
    assert shutil.which('conda') is not None
