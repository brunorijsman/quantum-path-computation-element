"""Parsing of the network YAML file into a network_model (intermediate representation)."""

import yaml
import cerberus

ROUTER_SCHEMA = {
    'name': {'required': True, 'type': 'string'},
}

LINK_SCHEMA = {
    'name': {'required': True, 'type': 'string'},
    'bandwidth':  {'type': 'integer'},               # Point-to-point capacity in Bell pairs per sec
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
    """Read and parse a network YAML file return the corresponding network model.

    Args:
        filename (str): The name of the network YAML file.
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
        try:
            network_model = yaml.safe_load(file)
        except yaml.YAMLError as err:
            message = f"Could not parse network file {filename} ({err})"
            raise ReadNetworkModelError(message)
    validator = NetworkValidator(NETWORK_SCHEMA)
    if not validator.validate(network_model, NETWORK_SCHEMA):
        message = f"Could not validate network file {filename}"
        raise ReadNetworkModelError(message)
        #@@@
        # pretty_printer = pprint.PrettyPrinter()
        # pretty_printer.pprint(validator.errors)
    network_model = validator.normalized(network_model)
    return network_model
