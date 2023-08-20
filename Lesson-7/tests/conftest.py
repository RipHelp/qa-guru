import glob
import os
import pytest

TMP_DIR = os.path.abspath((os.path.join(os.path.dirname(__file__), '../tmp')))


@pytest.fixture(scope='function')
def test_prepare():
    if not os.path.exists(TMP_DIR):
        os.makedirs(TMP_DIR)

    yield

    files = glob.glob(os.path.join(TMP_DIR, '*'))
    for f in files:
        os.remove(f)