"""Entry point for quantum path computation engine. Parse command line and run path computation."""

import argparse
import sys

import network_yaml

def parse_command_line_arguments(command_line_arguments):
    """Parse command line arguments.

    Returns: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Quantum Path Computation Engine')
    parser.add_argument("network_file", metavar="network-file", help="Network YAML file")
    parsed_arguments = parser.parse_args(command_line_arguments)
    return parsed_arguments

def main(command_line_arguments):
    """Main entry point."""
    # TODO: Catch exception and report error
    parsed_arguments = parse_command_line_arguments(command_line_arguments)
    _network = network_yaml.read_network_from_yaml_file(parsed_arguments.network_file)
    return 0

if __name__ == "__main__":   # pragma: no cover
    sys.exit(main(sys.argv[1:]))
