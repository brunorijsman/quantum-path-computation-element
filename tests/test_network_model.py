"""Unit tests for module network_model."""

import pytest

import network_model

def test_valid_network_file():
    """Test reading a valid network YAML file."""
    _model = network_model.read_network_model_from_file("tests/network-valid.yaml")

def test_non_existent_network_file():
    """Test reading a network YAML file that does not exist."""
    with pytest.raises(network_model.ReadNetworkModelError):
        _model = network_model.read_network_model_from_file("tests/non-existent-file.yaml")
