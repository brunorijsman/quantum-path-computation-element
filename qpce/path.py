"""Quantum path."""

class Path:
    # TODO: Remove this when we have more methods
    # pylint:disable=too-few-public-methods
    """A quantum path.

    A quantum path is an association between two application end-points over which qubits are
    teleported. The path produces end-to-end Bell pairs at the rate and fidelity requested by the
    application."""

    def __init__(self, end_point_1, end_point_2, name):
        """Initialize a quantum path.

        Args:
            end_point_1 (Router): The first end-point router of the path.
            end_point_2 (Router): The second end-point router of the path.
            name (str): Name of the path.
        Raises:
            AssertionError end-points are not in the same network

        Currently, the end points must be routers. In the future we may add support for host
        end-points."""
        assert end_point_1.network == end_point_2.network, \
               "End-points of the path are not in the same network"
        self.end_point_1 = end_point_1
        self.end_point_2 = end_point_2
        self.name = name
