"""The demand for a quantum network: the requested paths and constraints."""

import collections

class Demand:
    # TODO: Remove this when we have more methods
    # pylint:disable=too-few-public-methods
    """The quantum demand.

    The quantum demand describes the set of end-to-end paths requested by the applications and the
    constrains on the paths (e.g. bandwidth) and on the network as a whole."""

    def __init__(self, network):
        """Initialize a demand.

        Args:
            path(Path): The quantum path to be added.
            network(Network): The network to which the demand applies.
        """
        self.network = network
        self.paths = collections.OrderedDict()   # Path objects indexed by name

    def add_path(self, path):
        """Add a quantum path to this quantum network.

        Args:
            path(Path): The quantum path to be added.
        Returns:
            None
        """
        assert path.name not in self.paths, f"Network already contains a path with name {path.name}"
        assert path.end_point_1.name in self.network.routers, \
            f"End-point 1 {path.end_point_1.name} must be a router in the network"
        assert path.end_point_2.name in self.network.routers, \
            f"End-point 2 {path.end_point_2.name} must be a router in the network"
        self.paths[path.name] = path
