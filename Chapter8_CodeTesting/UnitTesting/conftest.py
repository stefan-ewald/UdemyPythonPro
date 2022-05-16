import sys

import pytest


@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "writecalls": 0}

    def fake_writer(s):
        buffer["stdout"] += s
        buffer["writecalls"] += 1

    monkeypatch.setattr(sys.stdout, "write", fake_writer)
    return buffer
