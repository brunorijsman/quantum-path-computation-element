"""Entry point for quantum path computation engine. Parse command line and run path computation."""

import argparse
import sys

import network

def parse_command_line_arguments(arguments):
    """Parse command line arguments.

    Returns: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Quantum Path Computation Engine')
    parser.add_argument("network_file", metavar="network-file", help="Network YAML file")
    arguments = parser.parse_args(arguments)
    return arguments

def main():
    """Main entry point."""
    arguments = parse_command_line_arguments(sys.argv[1:])
    _network = network.Network(arguments.network_file)

if __name__ == "__main__":   # pragma: no cover
    main()
