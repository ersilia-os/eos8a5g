# MolBloom to check purchasability of a molecule
## Model identifiers
- Slug: molbloom
- Ersilia ID: eos8a5g
- Tags: Purchasable, ZINC, Commercial

# Model description
A molecular Bloom filter is used to query the ZINC20 database. ZINC20 is an ultra-large library of chemical compounds, including, among many other commercial libraries, the Enamine REAL collection.
- Input: Single Compound (SMILES)
- Output: Purchasable. It returns a boolean (True/False) suggesting whether the molecule is commercially available or not.
- Model type: Classification
- Training set: ZINC20 dataset (https://zinc20.docking.org)
- Mode of training: Pretrained

# Source code
Cite the source publication.
- Code: https://github.com/whitead/molbloom
- Checkpoints: N/A

# License
State the licences used which are GPL v3 license used by Ersilia and the license used by the source code, if any exists. Use [this guide]() on how to license new models to be incorporated into Ersilia's model hub 

# History 
- The model was incorporated into Ersilia on 11/01/2022

# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
