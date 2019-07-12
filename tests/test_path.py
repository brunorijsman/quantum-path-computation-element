"""Unit tests for module path."""

from network import Network
from path import Path
from router import Router

def test_create_path():
    """Test creation of a path."""
    network = Network()
    alice = Router(network, "alice")
    bob = Router(network, "bob")
    _path = Path(alice, bob, "alice-to-bob")
