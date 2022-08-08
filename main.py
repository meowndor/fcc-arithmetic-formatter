# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger


print(arithmetic_arranger(
    ["3801 - 2", "3345 + 4h9"]))


# Run unit tests automatically
main(['-vv'])
