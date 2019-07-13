"""Parsing of the demand YAML file."""

import yaml
import cerberus

from demand import Demand
from path import Path

PATH_SCHEMA = {
    'name': {'type': 'string', 'required': True},
    'end-point-1': {'type': 'string', 'required': True},
    'end-point-2': {'type': 'string', 'required': True},
    'bandwidth':  {'type': 'integer', 'required': True, 'min': 1},
    'fidelity':  {'type': 'float', 'required': True},
}

DEMAND_SCHEMA = {
    'paths': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': PATH_SCHEMA,
        }
    },
}

class ReadDemandYamlError(Exception):
    """Exception is thrown when there is a problem reading the demand YAML file."""

class DemandValidator(cerberus.Validator):
    """The DemandValidator class is used to validate the correctness of a demand YAML file."""

def read_demand_from_yaml_file(filename, network):
    """Read and parse a demand YAML document from a file.

    Args:
        filename (str): Filename of the file to read the demand YAML document from.
        network (Network): The network to which the demand applies.
    Returns:
        A Demand object.
    Raises:
        ReadDemandYamlError: There was a problem reading the demand model.
    """
    try:
        file = open(filename, 'r')
    except (OSError, IOError) as err:
        message = f"Could not open demand file {filename} ({err})"
        raise ReadDemandYamlError(message)
    with file:
        return read_demand_from_yaml_stream(file, network)

def read_demand_from_yaml_stream(stream, network):
    """Read and parse a demand YAML document from a stream and return the corresponding demand
    model.

    Args:
        stream: Stream to read the demand YAML document from.
        network (Network): The network to which the demand applies.
    Returns:
        A Demand object.
    Raises:
        ReadDemandYamlError: There was a problem reading the demand model.
    """
    try:
        demand_model = yaml.safe_load(stream)
    except yaml.YAMLError as err:
        message = f"Could not parse demand YAML document ({err})"
        raise ReadDemandYamlError(message)
    validator = DemandValidator(DEMAND_SCHEMA)
    if not validator.validate(demand_model, DEMAND_SCHEMA):
        message = f"Could not validate demand YAMLdocument"
        raise ReadDemandYamlError(message)
        # TODO: Better error message, reporting validator.errors using pretty printer
        # TODO: ... or more specific exceptions
    demand_model = validator.normalized(demand_model)
    return read_demand_from_parsed_yaml(demand_model, network)

def read_demand_from_parsed_yaml(demand_model, network):
    """Create a Demand object from a demand_model, i.e. from parsed YAML file.

    Args:
        demand_model: The parsed demand YAML file.
        network (Network): The network to which the demand applies.
    Returns:
        A Demand object.
    Raises:
        ReadDemandYamlError: There was a problem reading the demand model.
    """
    demand = Demand(network)
    if 'paths' in demand_model:
        for path_model in demand_model['paths']:
            _path = read_path_from_parsed_yaml(path_model, demand)
    return demand

def read_path_from_parsed_yaml(path_model, demand):
    """Create a Link object from a link_model, i.e. from parsed YAML file.

    Args:
        path_model: The parsed path YAML object.
        demand: Create the Link object in this demand.
    Returns:
        The newly created Link object.
    """
    router_1_name = path_model['end-point-1']
    if router_1_name in demand.network.routers:
        router_1 = demand.network.routers[router_1_name]
    else:
        raise ReadDemandYamlError(f"Path end-point 1 {router_1_name} must be an existing router")
    router_2_name = path_model['end-point-2']
    if router_2_name in demand.network.routers:
        router_2 = demand.network.routers[router_2_name]
    else:
        raise ReadDemandYamlError(f"Path end-point 2 {router_2_name} must be an existing router")
    return Path(demand=demand,
                name=path_model['name'],
                end_point_1=router_1,
                end_point_2=router_2,
                bandwidth=path_model['bandwidth'],
                fidelity=path_model['fidelity'])
    