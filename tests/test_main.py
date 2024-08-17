# tests/test_cli.py
import sys
from unittest.mock import patch

import pytest

from constants import ACTIONS
from TaskTracker import catch_intro


def test_catch_intro_with_arguments():
    # Simula argumentos de línea de comandos
    test_args = ["TaskTracker.py", "add", "task1"]
    with patch.object(sys, "argv", test_args):
        result = catch_intro()
        assert result == ["add", "task1"]


def test_catch_intro_without_arguments():
    # Simula la ejecución sin argumentos de línea de comandos
    test_args = ["TaskTracker.py"]
    with patch.object(sys, "argv", test_args):
        result = catch_intro()
        assert result == []
