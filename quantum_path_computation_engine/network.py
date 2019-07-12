"""A quantum network consisting of quantum routers and links."""

import collections

class Network:
    # TODO: Remove this when we have more methods
    # pylint:disable=too-few-public-methods
    """A quantum network.

    A quantum network object describes the topology and available resources in a quantum network. It
    consists of quantum routers and quantum links."""

    def __init__(self):
        self.routers = collections.OrderedDict()   # Router objects indexed by name

    def create_router(self, name):
        """Create a new quantum router in the quantum network.

        Args:
            name: The name of the new quantum router.
        Returns:
            The newly created router object.
        Raises:
            AssertionError if there is already a router with the same name in the network."""
        assert name not in self.routers, f"Network already contains a router with name {name}"
        router = Router(name=name)
        self.routers[name] = router
        return router

    def create_link(self, from_router_name, to_router_name, length):
        """Create a new link in the quantum network.

        Args:
            from_router_name: The name of the first router that the link is connected to.
            to_router_name: The name of the second router that the link is connectd to. Links are
                bi-directional, so 'from' and 'to' can be reversed without consequence. It is legal
                to create a link between a router and itself; i.e. 'from' and 'to' are allowed to
                be the same router.
            length: The length of the link in meters.
        Returns:
            The newly created link object.
        Raises:
            AssertionError if:
            - Router from_router_name is not present in the network.
            - Router to_router_name is not present in the network.
            - The length is not > 0."""
        assert from_router_name  in self.routers, \
               f"Router {from_router_name} is not present in the network"
        assert to_router_name  in self.routers, \
               f"Router {to_router_name} is not present in the network"
        assert length > 0, \
               f"Link from {from_router_name} to {to_router_name} has length <= 0."
        from_router = self.routers[from_router_name]
        to_router = self.routers[to_router_name]
        link = Link(from_router, to_router, length)
        return link

class Router:
    # TODO: Remove this when we have more methods
    # pylint:disable=too-few-public-methods
    """A quantum router.

    A quantum router object represents a quantum router that is part of a quantum network. Quantum
    routers are interconnected by quantum links."""

    def __init__(self, name):
        """Initialize a quantum router.

        Args:
            name (str): The name of quantum router; uniquely identifies the router within the
            quantum network."""
        self.name = name
        self._next_port = 0
        self.links = collections.OrderedDict()     # Link objects indexed by local port

    def attach_link(self, link):
        """Attach a link to the router. The link is attached to the next available port.

        Args:
            link (Link): The link to be attached.
        Returns:
            The port to which the link was attached."""
        port = self._next_port
        self._next_port += 1
        self.links[port] = link
        return port

class Link:
    # TODO: Remove this when we have more methods
    # pylint:disable=too-few-public-methods
    """A quantum link.

    A quantum link object represents a physical quantum link between a pair of quantum routers."""

    def __init__(self, from_router, to_router, length):
        """Initialize a link.

        Args:
            from_router (Router): The first router object that the link is connected to.
            to_router (Router): The second router object that the link is connected to. Links are
                bi-directional, so 'from' and 'to' can be reversed without consequence. It is legal
                to create a link between a router and itself; i.e. 'from' and 'to' are allowed to
                be the same router.
            length (int): Length of the link in meters. Must be >=0."""
        self.from_router = from_router
        self.to_router = to_router
        self.length = length
        self.from_port = from_router.attach_link(self)
        self.to_port = to_router.attach_link(self)
