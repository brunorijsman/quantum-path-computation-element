"""Unit tests for module router."""

from network import Network
from router import Router

def test_create_router():
    """Test creation of a router."""
    network = Network()
    _router = Router(network, "router-name")
