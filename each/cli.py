import argparse
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="A command to execute.")
    args = parser.parse_args()

    for keyword in sys.stdin:
        command = args.command.format(keyword.rstrip())
        subprocess.run(command.split(" "))
