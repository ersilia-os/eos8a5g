# MolBloom: molecule purchasability in ZINC20

This model uses a Bloom filter to query the ZINC20 database to identify if a molecule is purchasable. A bloom filter is a space-efficient probabilistic data structure to identify whether an element is in a given set. Due to the nature of bloom filters, false negatives are not possible (i.e if the model returns False, the molecule is not purchasable). As stated by the author, if the model returns True the molecule is purchasable with an error rate of 0.0003 (according to the ZINC20 catalog).

This model was incorporated on 2022-11-02.

## Information
### Identifiers
- **Ersilia Identifier:** `eos8a5g`
- **Slug:** `molbloom`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `ZINC`, `Compound generation`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** It returns a boolean (True/False) suggesting whether the molecule is commercially available or not.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| purchasable | string |  | Whether the molecule is purchasable (True) or not (False) |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos8a5g](https://hub.docker.com/r/ersiliaos/eos8a5g)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8a5g.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8a5g.zip)

### Resource Consumption


### References
- **Source Code**: [https://github.com/whitead/molbloom](https://github.com/whitead/molbloom)
- **Publication**: [https://jcheminf.biomedcentral.com/articles/10.1186/s13321-023-00765-1](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-023-00765-1)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2023`
- **Ersilia Contributor:** [Amna-28](https://github.com/Amna-28)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos8a5g
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos8a5g
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
