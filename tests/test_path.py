"""Unit tests for module path."""

from demand import Demand
from network import Network
from path import Path
from router import Router

def test_create_path():
    """Test creation of a path."""
    network = Network()
    demand = Demand(network)
    alice = Router(network, "alice")
    bob = Router(network, "bob")
    _path = Path(demand=demand,
                 name="alice-to-bob",
                 end_point_1=alice,
                 end_point_2=bob,
                 bandwidth=10,
                 fidelity=0.95)
