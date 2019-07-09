[![Build Status](https://travis-ci.org/brunorijsman/quantum-path-computation-engine.svg?branch=master)](https://travis-ci.org/brunorijsman/quantum-path-computation-engine)   [![Code Coverage](https://codecov.io/gh/brunorijsman/quantum-path-computation-engine/branch/master/graph/badge.svg)](https://codecov.io/gh/brunorijsman/quantum-path-computation-engine)

# Quantum Path Computation Engine

## Summary of the functionality

The Quantum Path Computation Engine (QPCE) computes the route for quantum traffic paths on a
quantum network. 

The inputs are:

 * A _network_ file that describes the topology of the quantum network as well as the resources
   that are available in the quantum network.

 * [TODO] A _demand_ file that describes the traffic demand and other constrains for the end-to-end
   quantum communication paths that the quantum applications wish to establish.

 * [TODO] A _technology_ file that describes the attributes of the specific technology that is used
   to implement the quantum network (e.g. nitrogen-vacancy centers versus ion traps)

 The output is:

 * [TODO] A _route_ file that describes the computed route for each path, or an indication that no
   feasible route for the path could be determined.

The output of the Quantum Path Computation Element (i.e. the computed routes) can be fed into a
Quantum Path Signaling Element that installs the paths into the Quantum Forwarding Plane (which
will be simulated using NetSquid until the first real quantum network hardware is built).

## Information in the _network_ file

The _network_ input file describes the topology of the quantum network as well as the resources
that are available in the quantum network.

It contains the following information:

 * A list of quantum routers.

 * A list of quantum and classical links that interconnect the quantum routers.

For each quantum router, the following attributes can be specified:

 * The name of the quantum router.

 * [TODO] Additional attributes, such as the number of memory qubits etc.

For each link, the following attributes can be specified:

 * The names of the two quantum routers that are connected by the link.

 * [TODO] Whether the link is a quantum link, or a classical link, or both.

 * [TODO] Additional attributes, such as the point-to-point capacity of the link in Bell Pairs
   per second, or attributes that allow the calculation of the capacity (e.g. length in km, etc.)

## Information in the _demand_ file

[TODO]

## Information in the _technology_ file

[TODO]