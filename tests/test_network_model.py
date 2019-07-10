"""Unit tests for module network_model."""

import io
import pytest

import network_model

def test_valid_network_file():
    """Test reading a valid network YAML file."""
    _model = network_model.read_network_model_from_file("tests/network-valid.yaml")

def test_non_existent_network_file():
    """Test reading a network YAML file that does not exist."""
    with pytest.raises(network_model.ReadNetworkModelError):
        _model = network_model.read_network_model_from_file("tests/non-existent-file.yaml")

def test_valid_network_string():
    """Test reading a valid network YAML string."""
    document = io.StringIO("routers:\n"
                           "  - name: alice\n"
                           "  - name: bob\n"
                           "links:\n"
                           "  - from: alice\n"
                           "    to: bob\n")
    _model = network_model.read_network_model_from_stream(document)

def test_parse_bad_yaml():
    """Test parsing of an network YAML document which is not valid YAML."""
    document = io.StringIO("routers:\n"
                           "  - name: alice\n"
                           "  - name: bob\n"
                           "this is not valid YAML\n")
    with pytest.raises(network_model.ReadNetworkModelError):
        _model = network_model.read_network_model_from_stream(document)


def test_validate_bad_attribute():
    """Test validation of a network YAML document with a bad attribute."""
    document = io.StringIO("routers:\n"
                           "  - name: alice\n"
                           "  - name: bob\n"
                           "links:\n"
                           "  - from: alice\n"
                           "    to: bob\n"
                           "    nonsense: 300\n")
    with pytest.raises(network_model.ReadNetworkModelError):
        _model = network_model.read_network_model_from_stream(document)
