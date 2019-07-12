"""Quantum path."""

class Path:
    # TODO: Remove this when we have more methods
    # pylint:disable=too-few-public-methods
    """A quantum path.

    A quantum path is an association between two application end-points over which qubits are
    teleported. The path produces end-to-end Bell pairs at the rate and fidelity requested by the
    application."""

    def __init__(self, network, name):
        self.network = network
        self.name = name
