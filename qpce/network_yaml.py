"""Parsing of the network YAML file."""

import yaml
import cerberus

from link import Link
from network import Network
from router import Router

ROUTER_SCHEMA = {
    'name': {'type': 'string', 'required': True},
}

LINK_SCHEMA = {
    'router-1': {'type': 'string', 'required': True},
    'router-2': {'type': 'string', 'required': True},
    'length':  {'type': 'integer', 'required': True, 'min': 1},
}

NETWORK_SCHEMA = {
    'routers': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': ROUTER_SCHEMA,
        }
    },
    'links': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': LINK_SCHEMA,
        }
    },
}

class ReadNetworkYamlError(Exception):
    """Exception is thrown when there is a problem reading the network YAML file."""

class NetworkValidator(cerberus.Validator):
    """The NetworkValidator class is used to validate the correctness of a network YAML file."""

def read_network_from_yaml_file(filename):
    """Read and parse a network YAML document from a file.

    Args:
        Filename: Filename of the file to read the network YAML document from.
    Returns:
        A Network object.
    Raises:
        ReadNetworkYamlError: There was a problem reading the network model.
    """
    try:
        file = open(filename, 'r')
    except (OSError, IOError) as err:
        message = f"Could not open network file {filename} ({err})"
        raise ReadNetworkYamlError(message)
    with file:
        return read_network_from_yaml_stream(file)

def read_network_from_yaml_stream(stream):
    """Read and parse a network YAML document from a stream and return the corresponding network
    model.

    Args:
        stream: Stream to read the network YAML document from.
    Returns:
        A Network object.
    Raises:
        ReadNetworkYamlError: There was a problem reading the network model.
    """
    try:
        network_model = yaml.safe_load(stream)
    except yaml.YAMLError as err:
        message = f"Could not parse network YAML document ({err})"
        raise ReadNetworkYamlError(message)
    validator = NetworkValidator(NETWORK_SCHEMA)
    if not validator.validate(network_model, NETWORK_SCHEMA):
        message = f"Could not validate network YAMLdocument"
        raise ReadNetworkYamlError(message)
        # TODO: Better error message, reporting validator.errors using pretty printer
    network_model = validator.normalized(network_model)
    return read_network_from_parsed_yaml(network_model)

def read_network_from_parsed_yaml(network_model):
    """Create a Network object from a network_model, i.e. from parsed YAML file.

    Args:
        network_model: The parsed network YAML file.
    Returns:
        A Network object.
    Raises:
        ReadNetworkYamlError: There was a problem reading the network model.
    """
    network = Network()
    if 'routers' in network_model:
        for router_model in network_model['routers']:
            _router = read_router_from_parsed_yaml(router_model, network)
    if 'links' in network_model:
        for link_model in network_model['links']:
            _link = read_link_from_parsed_yaml(link_model, network)
    return network

def read_router_from_parsed_yaml(router_model, network):
    """Create a Router object from a router_model, i.e. from parsed YAML file.

    Args:
        router_model: The parsed router YAML object.
        network: Create the Router object in this network.
    Returns:
        The newly created Router object.
    """
    return Router(network=network, name=router_model['name'])

def read_link_from_parsed_yaml(link_model, network):
    """Create a Link object from a link_model, i.e. from parsed YAML file.

    Args:
        link_model: The parsed link YAML object.
        network: Create the Link object in this network.
    Returns:
        The newly created Link object.
    """
    router_1_name = link_model['router-1']
    if router_1_name in network.routers:
        router_1 = network.routers[router_1_name]
    else:
        raise ReadNetworkYamlError(f"Link has non-existent router-1 {router_1_name}")
    router_2_name = link_model['router-2']
    if router_2_name in network.routers:
        router_2 = network.routers[router_2_name]
    else:
        raise ReadNetworkYamlError(f"Link has non-existent router-2 {router_2_name}")
    return Link(router_1=router_1,
                router_2=router_2,
                length=link_model['length'])
