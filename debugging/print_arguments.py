#!/usr/bin/python3
import sys

# Slice the list to remove the first element, then iterate directly
for arg in sys.argv[1:]:
    print(arg)