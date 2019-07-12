"""Quantum network."""

import collections

class Network:
    # TODO: Remove this when we have more methods
    # pylint:disable=too-few-public-methods
    """A quantum network.

    A quantum network object describes the topology and available resources in a quantum network. It
    consists of quantum routers and quantum links."""

    def __init__(self):
        self.routers = collections.OrderedDict()   # Router objects indexed by name

    def add_router(self, router):
        """Add a quantum router to this quantum network.

        Args:
            router(Router): The quantum router to be added.
        Returns:
            None
        """
        assert router.name not in self.routers, \
               f"Network already contains a router with name {router.name}"
        self.routers[router.name] = router
