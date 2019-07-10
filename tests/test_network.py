"""Unit tests for module network."""

import network

def test_valid_network_file():
    """Test reading a valid network YAML file."""
    _net = network.Network("tests/network-valid.yaml")
