"""Unit tests for module __main__."""

import pytest

from qpce.__main__ import parse_command_line_arguments
from qpce.__main__ import main

def test_no_arguments(capsys):
    """Test absence of command line arguments."""
    command_line_arguments = []
    with pytest.raises(SystemExit):
        _parsed_arguments = parse_command_line_arguments(command_line_arguments)
    captured = capsys.readouterr()
    assert "error: the following arguments are required: network-file" in captured.err

def test_help_argument(capsys):
    """Test the --help command line argument."""
    for command_line_arguments in [['--help'], ['-h']]:
        with pytest.raises(SystemExit):
            _parsed_arguments = parse_command_line_arguments(command_line_arguments)
        captured = capsys.readouterr()
        assert "usage:" in captured.out

def test_network_argument():
    """Test the --help command line argument."""
    command_line_arguments = ['network-valid.yaml']
    parsed_arguments = parse_command_line_arguments(command_line_arguments)
    assert parsed_arguments.network_file == 'network-valid.yaml'

def test_main():
    """Test main entry point function."""
    command_line_arguments = ['tests/network-valid.yaml']
    main(command_line_arguments)
