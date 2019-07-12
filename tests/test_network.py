"""Unit tests for module network."""

import pytest
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

def test_create_link_bad_from_router():
    """Attempt to create a link whose from_router does not exist."""
    net = network.Network()
    _bob = net.create_router("bob")
    with pytest.raises(AssertionError):
        _link = net.create_link("ava", "bob", 100)

def test_create_link_bad_to_router():
    """Attempt to create a link whose to_router does not exist."""
    net = network.Network()
    _alice = net.create_router("alice")
    with pytest.raises(AssertionError):
        _link = net.create_link("alice", "bart", 100)

def test_create_link_bad_lenght():
    """Attempt to create a link whose length is not greater than zero."""
    net = network.Network()
    _alice = net.create_router("alice")
    _bob = net.create_router("bob")
    with pytest.raises(AssertionError):
        _link = net.create_link("alice", "bob", -100)
    with pytest.raises(AssertionError):
        _link = net.create_link("alice", "bob", 0)
