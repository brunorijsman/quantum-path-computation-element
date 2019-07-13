"""Unit tests for module network_yaml."""

import io
import pytest

import network_yaml

def test_valid_network_file():
    """Test reading a valid network YAML file."""
    _network = network_yaml.read_network_from_yaml_file("tests/network-valid.yaml")

def test_non_existent_network_file():
    """Test reading a network YAML file that does not exist."""
    with pytest.raises(network_yaml.ReadNetworkYamlError):
        _network = network_yaml.read_network_from_yaml_file("tests/non-existent-file.yaml")

def test_valid_network_string():
    """Test reading a valid network YAML string."""
    document = io.StringIO("routers:\n"
                           "  - name: alice\n"
                           "  - name: bob\n"
                           "links:\n"
                           "  - router-1: alice\n"
                           "    router-2: bob\n"
                           "    length: 10\n")
    _network = network_yaml.read_network_from_yaml_stream(document)

def test_parse_bad_yaml():
    """Test parsing of an network YAML document which is not valid YAML."""
    document = io.StringIO("routers:\n"
                           "  - name: alice\n"
                           "  - name: bob\n"
                           "this is not valid YAML\n")
    with pytest.raises(network_yaml.ReadNetworkYamlError):
        _network = network_yaml.read_network_from_yaml_stream(document)

def test_validate_bad_attribute():
    """Test validation of a network YAML document with a bad attribute."""
    document = io.StringIO("routers:\n"
                           "  - name: alice\n"
                           "  - name: bob\n"
                           "links:\n"
                           "  - router-1: alice\n"
                           "    router-2: bob\n"
                           "    nonsense: 300\n")
    with pytest.raises(network_yaml.ReadNetworkYamlError):
        _network = network_yaml.read_network_from_yaml_stream(document)

def test_validate_link_bad_router_1():
    """Test validation of a network YAML document containing a link with a bad router-1."""
    document = io.StringIO("routers:\n"
                           "  - name: alice\n"
                           "  - name: bob\n"
                           "links:\n"
                           "  - router-1: ava\n"
                           "    router-2: bob\n"
                           "    length: 300\n")
    with pytest.raises(network_yaml.ReadNetworkYamlError):
        _network = network_yaml.read_network_from_yaml_stream(document)

def test_validate_link_bad_router_2():
    """Test validation of a network YAML document containing a link with a bad router-2."""
    document = io.StringIO("routers:\n"
                           "  - name: alice\n"
                           "  - name: bob\n"
                           "links:\n"
                           "  - router-1: alice\n"
                           "    router-2: bart\n"
                           "    length: 300\n")
    with pytest.raises(network_yaml.ReadNetworkYamlError):
        _network = network_yaml.read_network_from_yaml_stream(document)

def test_validate_link_bad_lenght():
    """Test validation of a network YAML document containing a link with a bad length."""
    document = io.StringIO("routers:\n"
                           "  - name: alice\n"
                           "  - name: bob\n"
                           "links:\n"
                           "  - router-1: alice\n"
                           "    router-2: bob\n"
                           "    length: -100\n")
    with pytest.raises(network_yaml.ReadNetworkYamlError):
        _network = network_yaml.read_network_from_yaml_stream(document)
