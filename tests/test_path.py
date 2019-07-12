"""Unit tests for module path."""

from network import Network
from path import Path

def test_create_path():
    """Test creation of a path."""
    network = Network()
    _path = Path(network, "my-path")
