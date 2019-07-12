"""Quantum Router."""

import collections

class Router:
    # TODO: Remove this when we have more methods
    # pylint:disable=too-few-public-methods
    """A quantum router.

    A quantum router object represents a quantum router that is part of a quantum network. Quantum
    routers are interconnected by quantum links."""

    def __init__(self, network, name):
        """Initialize a quantum router.

        Args:
            name (str): The name of quantum router; uniquely identifies the router within the
            quantum network.
        Raises:
            AssertionError if there is already a router with the same name in the network."""
        self.network = network
        self.name = name
        self._next_available_port = 0
        self.links = collections.OrderedDict()     # Link objects indexed by local port
        network.add_router(self)

    def add_link(self, link):
        """Add a link to the router. The link is attached to the next available port. The number of
        that port is returned.

        Args:
            link (Link): The link to be attached.
        Returns:
            The port to which the link was attached.
        Raises:
            AssertionError if there is already a router with the same name in the network."""
        assert self in [link.router_1, link.router_2], \
               f"Attempt to add link to router {self.name} which is not an end-point of the link"
        port = self._next_available_port
        self._next_available_port += 1
        self.links[port] = link
        return port
