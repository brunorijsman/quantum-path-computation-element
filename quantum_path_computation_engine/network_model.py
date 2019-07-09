"""Model for the topology of a quantum network (internal representation of the YAML document)."""

import yaml
import cerberus

ROUTER_SCHEMA = {
    'name': {'required': True, 'type': 'string'},
}

LINK_SCHEMA = {
    'name': {'required': True, 'type': 'string'},
    'bandwidth':  {'type': 'integer'},               # Point-to-point capacity in Bell pairs per sec
}

TOPOLOGY_SCHEMA = {
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

class ReadTopologyModelError(Exception):
    """Exception is thrown when there is a problem reading the topology model."""

class TopologyValidator(cerberus.Validator):
    """The TopologyValidator class is used to validate the correctness of a topology YAML file."""

def read_topology_model_from_file(filename):
    """Read and parse a topology YAML file return the corresponding topology model.

    Args:
        filename (str): The name of the topology file.
    Returns:
        The topology model.
    Raises:
        ReadTopologyModelError: There was a problem reading the topology model.
    """
    try:
        file = open(filename, 'r')
    except (OSError, IOError) as err:
        message = f"Could not open topology file {filename} ({err})"
        raise ReadTopologyModelError(message)
    try:
        topology_model = yaml.safe_load(file)
    except yaml.YAMLError as err:
        message = f"Could not parse topology file {filename} ({err})"
        raise ReadTopologyModelError(message)
    file.close()   ###@@@
    validator = TopologyValidator(TOPOLOGY_SCHEMA)
    if not validator.validate(topology_model, TOPOLOGY_SCHEMA):
        message = f"Could not validate topology file {filename}"
        raise ReadTopologyModelError(message)
        #@@@
        # pretty_printer = pprint.PrettyPrinter()
        # pretty_printer.pprint(validator.errors)
    topology_model = validator.normalized(topology_model)
    return topology_model
