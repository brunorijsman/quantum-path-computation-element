"""Unit tests for module network."""

import network

def test_create_router():
    """Test creation of a router."""
    net = network.Network()
    _alice = net.create_router("alice")

def test_create_link():
    """Test creation of a link."""
    net = network.Network()
    alice = net.create_router("alice")
    bob = net.create_router("bob")
    link = net.create_link("alice", "bob", 100)
    assert link.from_router == alice
    assert link.from_port == 0
    assert link.to_router == bob
    assert link.to_port == 0
    assert link.length == 100
    assert net.routers["alice"] == alice
    assert net.routers["bob"] == bob
    assert alice.links[0] == link
    assert bob.links[0] == link
