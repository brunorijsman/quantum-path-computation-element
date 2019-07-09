"""Entry point for quantum path computation engine. Parse command line and run path computation."""

import argparse

from network import Network

def parse_command_line_arguments():
    """Parse command line arguments.

    Returns: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Quantum Path Computation Engine')
    parser.add_argument("network-file", help="Network YAML file")
    arguments = parser.parse_args()
    return arguments

def main():
    """Main entry point."""
    arguments = parse_command_line_arguments()
    _network = Network(arguments.network_file)

if __name__ == "__main__":
    main()
