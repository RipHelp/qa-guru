import glob
import os
import pytest
from os import path

RESOURCES_DIR = path.abspath(
    path.join(path.dirname(__file__), '../resources')
)

TMP_MAIN = path.abspath(
    path.join(path.dirname(__file__), '../tmp')
)


@pytest.fixture(scope='function')
def test_prepare():
    if not os.path.exists(RESOURCES_DIR):
        os.makedirs(RESOURCES_DIR)

    yield

    files = glob.glob(os.path.join(RESOURCES_DIR, '*'))
    for f in files:
        os.remove(f)
