[![Build Status](https://travis-ci.org/brunorijsman/quantum-path-computation-element.svg?branch=master)](https://travis-ci.org/brunorijsman/quantum-path-computation-element)   [![Code Coverage](https://codecov.io/gh/brunorijsman/quantum-path-computation-element/branch/master/graph/badge.svg)](https://codecov.io/gh/brunorijsman/quantum-path-computation-element)

# Quantum Path Computation Element

## Summary of the functionality

The Quantum Path Computation Element (QPCE) computes the route for quantum paths on a quantum
network. 

The inputs are:

 * A _network_ file that describes the topology of the quantum network as well as the resources
   that are available in the quantum network.

 * A _demand_ file that describes the traffic demand and other constrains for the end-to-end
   quantum communication paths that the quantum applications wish to establish.

 * A _technology_ file that describes the attributes of the specific technology that is used
   to implement the quantum network (e.g. nitrogen-vacancy centers versus ion traps)

 The output is:

 * A _route_ file that describes the computed route for each path, or an indication that no
   feasible route for the path could be determined.

The output of the Quantum Path Computation Element (i.e. the computed routes) can be fed into a
Quantum Path Signaling Element that installs the paths into the Quantum Forwarding Plane (which
will be simulated using NetSquid until the first real quantum network hardware is built).

## Information in the _network_ file

The _network_ input file describes the topology of the quantum network as well as the resources
that are available in the quantum network.

It contains the following information:

 * A list of quantum routers.

 * A list of links that interconnect the quantum routers.

For each quantum router, the following attributes can be specified:

 * The name of the quantum router.

 * [TODO] Additional attributes, such as the number of memory qubits etc.

For each link, the following attributes can be specified:

 * The names of the two quantum routers that are connected by the link.

 * [TODO] Whether the link is a quantum link, or a classical link, or both.

 * [TODO] Additional attributes, such as the point-to-point capacity of the link in Bell Pairs
   per second, or attributes that allow the calculation of the capacity (e.g. length in km, etc.)

The _network_ file can be manually constructed or it can be dynamically constructed using, for
example, the following automatic discovery mechanisms:

 * Existing link-state routing protocols such as Open Shortest Path First (OSPF) or Intermediate
   System to Intermediate System (ISIS) can be used to dynamically discover the topology of the
   network, i.e. which quantum routers are present and which links interconnect them.

 * If the classical topology is different from the quantum topology (i.e. if some links are used
   for classical messages only and other links are used for qubits only) then existing
   Multi-Topology (MT) extensions to OSPF and ISIS could be used or generalized to discover the
   classical and quantum topology separately.

 * The Traffic Engineering (TE) extensions to OSPF and ISIS can be generalized to discover the
   available resources and attributes of routers and links that are unique to quantum networking,
   such as for example the number of memory qubits on a router. A step in this direction has already
   been taken in the IETF Internet Draft "Advertising Entanglement
   Capabilities in Quantum Networks" ([draft-kaws-qirg-advent](https://datatracker.ietf.org/doc/draft-kaws-qirg-advent/))

## Information in the _demand_ file

The _demand_ that describes the traffic demand and other constrains for the end-to-end quantum
communication paths that the quantum applications wish to establish.

It contains the following information:

 * A list of requested quantum paths.

 * A list of constraints.

The service provided by a quantum path from point A to point Z is to generate pairs of bi-partite
entangled Bell pairs at points A and Z. These Bell pairs are consumed by quantum application
end-points running at points A and Z. The Bell pairs can be consumed directly, e.g. for
Quantum Key Distribution (QKD). Or the Bell pairs can be consumed to teleport qubits with an
arbitrary state for more general distributed quantum applications.

The application is able to request that these end-to-end entangled Bell pairs are
generated at a specific rate, e.g. 10 Bell Pairs Per Second (BPPS). The job of the quantum path
computation element is to compute the route (e.g. A-B-C-D-Z) in such a manner that all paths are
able to provide the requested "bandwidth" (in end-to-end BPPS) and also satisfy the other
constraints.

The quantum path computation element endeavors to compute the optimal set of path routes in the
sense that the total amount of resources consumed on the network is minimized.

We currently only support point-to-point quantum paths that generate bi-partite entangled bell
pairs. Support for multipoint quantum paths to generate multi-partite entangled qubits (e.g. in
the GHZ or W state) may be added later.

For each quantum path, the following attributes can be specified:

 * The two routers (A and Z) at the end-points of the quantum paths. All paths are
   bi-directional, in the sense that Bell pairs are always produced in pairs, where one qubit
   appears at router A and the other qubit appears at router Z. Thus, so there is no concept of
   source (ingress) router or destination (egress) router for a quantum path.

 * The requested bandwidth for the quantum path expressed in end-to-end Bell Pairs Per Second
   (BPPS).
 
 * The requested fidelity for the produced Bell pairs.

 * [TODO] More.

For each constraint, the following attributes can be specified:

 * [TODO].



## Information in the _technology_ file

[TODO]