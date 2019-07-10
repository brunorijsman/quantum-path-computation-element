"""Parsing of the network YAML file into a network_model (intermediate representation)."""

import yaml
import cerberus

ROUTER_SCHEMA = {
    'name': {'required': True, 'type': 'string'},
}

LINK_SCHEMA = {
    'from': {'required': True, 'type': 'string'},
    'to': {'required': True, 'type': 'string'},
    'length':  {'type': 'integer', 'min': 1},  # Physical length of the link in meters
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

class ReadNetworkModelError(Exception):
    """Exception is thrown when there is a problem reading the network model."""

class NetworkValidator(cerberus.Validator):
    """The NetworkValidator class is used to validate the correctness of a network YAML file."""

def read_network_model_from_file(filename):
    """Read and parse a network YAML document from a file and return the corresponding network
    model.

    Args:
        Filename: Filename of the file to read the network YAML document from.
    Returns:
        The network model (intermediate representation).
    Raises:
        ReadNetworkModelError: There was a problem reading the network model.
    """
    try:
        file = open(filename, 'r')
    except (OSError, IOError) as err:
        message = f"Could not open network file {filename} ({err})"
        raise ReadNetworkModelError(message)
    with file:
        return read_network_model_from_stream(file)

def read_network_model_from_stream(stream):
    """Read and parse a network YAML document from a stream and return the corresponding network
    model.

    Args:
        stream: Stream to read the network YAML document from.
    Returns:
        The network model (intermediate representation).
    Raises:
        ReadNetworkModelError: There was a problem reading the network model.
    """
    try:
        network_model = yaml.safe_load(stream)
    except yaml.YAMLError as err:
        message = f"Could not parse network YAML document ({err})"
        raise ReadNetworkModelError(message)
    validator = NetworkValidator(NETWORK_SCHEMA)
    if not validator.validate(network_model, NETWORK_SCHEMA):
        message = f"Could not validate network YAMLdocument"
        raise ReadNetworkModelError(message)
        # TODO: Better error message
        # pretty_printer = pprint.PrettyPrinter()
        # pretty_printer.pprint(validator.errors)
    network_model = validator.normalized(network_model)
    return network_model
