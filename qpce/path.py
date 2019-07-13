"""Quantum path."""

class Path:
    # TODO: Remove this when we have more methods
    # pylint:disable=too-few-public-methods
    """A quantum path.

    A quantum path is an association between two application end-points over which qubits are
    teleported. The path produces end-to-end Bell pairs at the rate and fidelity requested by the
    application."""

    def __init__(self, demand, name, end_point_1, end_point_2, bandwidth, fidelity):
        """Initialize a quantum path.

        Args:
            demand (Demand): The demand object to which the path is added.
            name (str): Name of the path.
            end_point_1 (Router): The first end-point router of the path.
            end_point_2 (Router): The second end-point router of the path.
            bandwidth (int): Requested bandwidth in end-to-end Bell pairs per second.
            fidelity (float): Requested fidelity of the generated end-to-end Bell pairs.

        Currently, the end points must be routers. In the future we may add support for host
        end-points.
        """
        assert end_point_1.network == end_point_2.network, "End-points are not in the same network"
        assert bandwidth > 0, "Requested end-to-end bandwidth must be > 0"
        assert fidelity > 0.0, "Requested end-to-end fidelity must be > 0.0"
        self.name = name
        self.end_point_1 = end_point_1
        self.end_point_2 = end_point_2
        self.bandwidth = bandwidth
        self.fidelity = fidelity
        demand.add_path(self)
