"""Unit tests for module network_model."""

import network_model

def test_valid_network_file():
    """Test reading a valid network YAML file."""
    _model = network_model.read_network_model_from_file("tests/network-valid.yaml")
