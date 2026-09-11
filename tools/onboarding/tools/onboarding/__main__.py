import sys

# Absolute import: Bazel's py_binary stub runs this file as a top-level
# script, so `__package__` is empty and relative imports fail.
from tools.onboarding.cli import cli

if __name__ == "__main__":
    cli(sys.argv[1:])
