"""Quantum link."""

class Link:
    # TODO: Remove this when we have more methods
    # pylint:disable=too-few-public-methods
    """A link.

    A link object represents a physical link between a pair of quantum routers.

    The current implementation assumes that every link is both a quantum link (can exchange qubits)
    as well as a classical link (can exchange classical messages). In other words, at this point
    we assume that the quantum topology and the classical topology are the same."""

    def __init__(self, router_1, router_2, length):
        """Initialize a link.

        Args:
            router_1 (Router): The first router object that the link is connected to.
            router_2 (Router): The second router object that the link is connected to.
            length (int): Length of the link in meters. Must be >=0.

        Links are bi-directional, so router_1 and router_2 can be reversed without consequence.

        It is legal to create a link between a router and itself; i.e. router_1 and router_2 are
        allowed to be the same router. In this case, the link will be connected from one port on the
        router to another port on the same router.
        """
        assert length > 0, f"Invalid length {length} for link, must be > 0."
        assert router_1.network == router_2.network, \
               "Routers of the link are not in the same network"
        self.router_1 = router_1
        self.router_2 = router_2
        self.length = length
        self.port_1 = router_1.add_link(self)
        self.port_2 = router_2.add_link(self)
