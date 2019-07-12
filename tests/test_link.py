"""Unit tests for module link."""

import pytest

from network import Network
from router import Router
from link import Link

def test_create_link():
    """Test creation of a link."""
    network = Network()
    alice = Router(network, "alice")
    bob = Router(network, "bob")
    link = Link(alice, bob, 100)
    assert link.router_1 == alice
    assert link.port_1 == 0
    assert link.router_2 == bob
    assert link.port_2 == 0
    assert link.length == 100
    assert alice.links[0] == link
    assert bob.links[0] == link

def test_create_link_bad_lenght():
    """Attempt to create a link whose length is not greater than zero."""
    network = Network()
    alice = Router(network, "alice")
    bob = Router(network, "bob")
    with pytest.raises(AssertionError):
        _link = Link(alice, bob, -100)
    with pytest.raises(AssertionError):
        _link = Link(alice, bob, 0)

def test_create_link_routers_in_different_networks():
    """Attempt to create a link whose routers are in different networks."""
    network_1 = Network()
    network_2 = Network()
    alice = Router(network_1, "alice")
    bob = Router(network_2, "bob")
    with pytest.raises(AssertionError):
        _link = Link(alice, bob, 100)
