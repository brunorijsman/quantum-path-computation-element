"""Topology of a quantum network."""

import pprint
import sys

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

class NetworkValidator(cerberus.Validator):
    """The TopologyValidator class is used to validate the correctness of a topology YAML file."""

class Network:
    """A quantum network.

    A quantum network object describes the topology and available resources in a quantum network. It
    consists of quantum routers and quantum links."""

    def __init__(self) -> None:
        self.routers = []
        self.links = []

    def read_from_file(self, filename):
        """Read and parse a topology file and store it in this topology object.

        Args:
            filename (str): The name of the topology file.
        Returns:
            None
        """
        try:
            file = open(filename, 'r')
        except (OSError, IOError) as err:
            print(f"Could not open topology file {filename} ({err})", file=sys.stderr)
            sys.exit(1)
        try:
            topology_model = yaml.safe_load(file)
        except yaml.YAMLError as err:
            print(f"Could not parse topology file {filename} ({err})", file=sys.stderr)
            file.close()
            sys.exit(1)
        file.close()
        validator = NetworkValidator(NETWORK_SCHEMA)
        if not validator.validate(topology_model, NETWORK_SCHEMA):
            print(f"Could not validate topology file {filename}", file=sys.stderr)
            pretty_printer = pprint.PrettyPrinter()
            pretty_printer.pprint(validator.errors)
            exit(1)
        topology_model = validator.normalized(topology_model)
        self.read_from_model(topology_model)

    def read_from_model(self, model):
        """Read this topology object from a topology YAML model.

        Args:
            model (yaml model): The YAML model of the topology.
        Returns:
            None
        """
        if 'routers' in model:
            for router_model in model['routers']:
                router = Router(model=router_model)
                self.routers.append(router)
        if 'links' in model:
            for link_model in model['links']:
                link = Router(model=link_model)
                self.links.append(link)

class Router:
    # TODO: Remove this when we have more methods
    # pylint:disable=too-few-public-methods
    """A quantum router.

    A quantum router object represents a quantum router that is part of a quantum network. Quantum
    routers are interconnected by quantum links."""

    def __init__(self, model):
        self.read_from_model(model)

    def read_from_model(self, model):
        """Read this router object from a router YAML model.

        Args:
            model (yaml model): The YAML model of the router.
        Returns:
            None
        """
        # TODO: Implement this

class Link:
    # TODO: Remove this when we have more methods
    # pylint:disable=too-few-public-methods
    """A quantum link.

    A quantum link object represents a physical quantum link between a pair of quantum routers."""

    def __init__(self, model):
        self.read_from_model(model)

    def read_from_model(self, model):
        """Read this router object from a router YAML model.

        Args:
            model (yaml model): The YAML model of the router.
        Returns:
            None
        """
        # TODO: Implement this
