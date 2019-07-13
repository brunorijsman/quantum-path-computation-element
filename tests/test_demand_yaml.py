"""Unit tests for module demand_yaml."""

import io
import pytest

import demand_yaml
import network_yaml
from network import Network

def test_valid_demand_file():
    """Test reading a valid demand YAML file."""
    network = network_yaml.read_network_from_yaml_file("tests/network-valid.yaml")
    _demand = demand_yaml.read_demand_from_yaml_file("tests/demand-valid.yaml", network)

def test_non_existent_demand_file():
    """Test reading a demand YAML file that does not exist."""
    network = Network()
    with pytest.raises(demand_yaml.ReadDemandYamlError):
        _demand = demand_yaml.read_demand_from_yaml_file("tests/non-existent-file.yaml", network)

def test_valid_demand_string():
    """Test reading a valid demand YAML string."""
    document = io.StringIO("paths:\n"
                           "- name: alice-to-bob\n"
                           "  end-point-1: alice\n"
                           "  end-point-2: bob\n"
                           "  bandwidth: 100\n"
                           "  fidelity: 0.95\n")
    network = network_yaml.read_network_from_yaml_file("tests/network-valid.yaml")
    _demand = demand_yaml.read_demand_from_yaml_stream(document, network)

def test_parse_bad_yaml():
    """Test parsing of an demand YAML document which is not valid YAML."""
    document = io.StringIO("paths:\n"
                           "- name: alice-to-bob\n"
                           "  This is not valid YAML\n"
                           "  end-point-2: bob\n"
                           "  bandwidth: 100\n"
                           "  fidelity: 0.95\n")
    network = network_yaml.read_network_from_yaml_file("tests/network-valid.yaml")
    with pytest.raises(demand_yaml.ReadDemandYamlError):
        _demand = demand_yaml.read_demand_from_yaml_stream(document, network)

def test_validate_bad_attribute():
    """Test validation of a demand YAML document with a bad attribute."""
    document = io.StringIO("paths:\n"
                           "- name: alice-to-bob\n"
                           "  a-bad-attribute: alice\n"
                           "  end-point-2: bob\n"
                           "  bandwidth: 100\n"
                           "  fidelity: 0.95\n")
    network = network_yaml.read_network_from_yaml_file("tests/network-valid.yaml")
    with pytest.raises(demand_yaml.ReadDemandYamlError):
        _demand = demand_yaml.read_demand_from_yaml_stream(document, network)

def test_validate_link_bad_end_point_1():
    """Test validation of a demand YAML document containing a link with a bad end-point-1."""
    document = io.StringIO("paths:\n"
                           "- name: path-with-bad-end-point-1\n"
                           "  end-point-1: non-existing-router\n"
                           "  end-point-2: bob\n"
                           "  bandwidth: 100\n"
                           "  fidelity: 0.95\n")
    network = network_yaml.read_network_from_yaml_file("tests/network-valid.yaml")
    with pytest.raises(demand_yaml.ReadDemandYamlError):
        _demand = demand_yaml.read_demand_from_yaml_stream(document, network)

def test_validate_link_bad_end_point_2():
    """Test validation of a demand YAML document containing a link with a bad end-point-2."""
    document = io.StringIO("paths:\n"
                           "- name: path-with-bad-end-point-2\n"
                           "  end-point-1: alice\n"
                           "  end-point-2: non-existing-router\n"
                           "  bandwidth: 100\n"
                           "  fidelity: 0.95\n")
    network = network_yaml.read_network_from_yaml_file("tests/network-valid.yaml")
    with pytest.raises(demand_yaml.ReadDemandYamlError):
        _demand = demand_yaml.read_demand_from_yaml_stream(document, network)

def test_validate_link_bad_bandwidth():
    """Test validation of a demand YAML document containing a link with a bad bandwidth."""
    document = io.StringIO("paths:\n"
                           "- name: alice-to-bob\n"
                           "  end-point-1: alice\n"
                           "  end-point-2: bob\n"
                           "  bandwidth: -10\n"
                           "  fidelity: 0.95\n")
    network = network_yaml.read_network_from_yaml_file("tests/network-valid.yaml")
    with pytest.raises(demand_yaml.ReadDemandYamlError):
        _demand = demand_yaml.read_demand_from_yaml_stream(document, network)
    document = io.StringIO("paths:\n"
                           "- name: alice-to-bob\n"
                           "  end-point-1: alice\n"
                           "  end-point-2: bob\n"
                           "  bandwidth: 0\n"
                           "  fidelity: 0.95\n")
    with pytest.raises(demand_yaml.ReadDemandYamlError):
        _demand = demand_yaml.read_demand_from_yaml_stream(document, network)

def test_validate_link_bad_fidelity():
    """Test validation of a demand YAML document containing a link with a bad fidelity."""
    document = io.StringIO("paths:\n"
                           "- name: alice-to-bob\n"
                           "  end-point-1: alice\n"
                           "  end-point-2: bob\n"
                           "  bandwidth: 100\n"
                           "  fidelity: -0.1\n")
    network = network_yaml.read_network_from_yaml_file("tests/network-valid.yaml")
    # TODO: Be consistent in what exception is raides
    with pytest.raises(AssertionError):
        _demand = demand_yaml.read_demand_from_yaml_stream(document, network)
    document = io.StringIO("paths:\n"
                           "- name: alice-to-bob\n"
                           "  end-point-1: alice\n"
                           "  end-point-2: bob\n"
                           "  bandwidth: 100\n"
                           "  fidelity: 0.0\n")
    with pytest.raises(AssertionError):
        _demand = demand_yaml.read_demand_from_yaml_stream(document, network)
