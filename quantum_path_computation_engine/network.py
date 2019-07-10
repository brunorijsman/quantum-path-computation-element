"""Internal representation of a quantum network."""

import network_model

class Network:
    """A quantum network.

    A quantum network object describes the topology and available resources in a quantum network. It
    consists of quantum routers and quantum links."""

    def __init__(self, network_filename):
        self.routers = []
        self.links = []
        ###@@@ handle exceptions
        self.read_from_file(network_filename)

    def read_from_file(self, filename):
        """Read and parse a network YAML file and store it in this network object.

        Args:
            filename (str): The name of the network YAML file.
        Returns:
            None
        """
        ###@@@ handle exceptions
        model = network_model.read_network_model_from_file(filename)
        self.read_from_model(model)

    def read_from_model(self, model):
        """Store the contents of a network model (i.e. a parsed network YAML file) into this network
        object.

        Args:
            model: The network model (i.e. the parsed YAML network file)
        Returns:
            None
        """
        if 'routers' in model:
            for router_model in model['routers']:
                router = Router(model=router_model)
                self.routers.append(router)
        if 'links' in model:
            for link_model in model['links']:
                link = Link(model=link_model)
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
