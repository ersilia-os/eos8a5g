# imports
import os
import csv
import sys
from molbloom import buy

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]
    
# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    smiles_list = [r[0] for r in reader]
    
# run model
# the filter stores canonical Kekule SMILES, so canonicalize (needs rdkit) or
# aromatic input never matches
outputs = [buy(smiles, canonicalize=True) for smiles in smiles_list]

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["purchasable"]) # header
    for o in outputs:
        writer.writerow([o])
