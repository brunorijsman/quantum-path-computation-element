"""Unit tests for module path."""

from network import Network
from path import Path
from router import Router

def test_create_path():
    """Test creation of a path."""
    network = Network()
    alice = Router(network, "alice")
    bob = Router(network, "bob")
    _path = Path(end_point_1=alice,
                 end_point_2=bob,
                 name="alice-to-bob",
                 bandwidth=10,
                 fidelity=0.95)
