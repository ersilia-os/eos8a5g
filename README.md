# MolBloom: molecule purchasability in ZINC20

Reports whether a molecule can be purchased from the ZINC20 catalogue. MolBloom, by Medina and White, answers this with a Bloom filter, a probabilistic structure that stores set membership in a few megabytes instead of a full database, making the check instantaneous and offline. The trade-off is inherent to the method: a compound reported as absent is definitely absent, while one reported as available carries a small chance of being a false positive.

This model was incorporated on 2022-11-02.Last packaged on 2025-10-14.

## Information
### Identifiers
- **Ersilia Identifier:** `eos8a5g`
- **Slug:** `molbloom`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `ZINC`, `Compound generation`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Whether the molecule is purchasable from ZINC20, reported as True or False.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| purchasable | string |  | Whether the molecule is purchasable (True) or not (False) |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos8a5g](https://hub.docker.com/r/ersiliaos/eos8a5g)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8a5g.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8a5g.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `380`
- **Image Size (Mb):** `307.31`

**Computational Performance (seconds):**
- 10 inputs: `28.89`
- 100 inputs: `18.91`
- 10000 inputs: `23.45`

### References
- **Source Code**: [https://github.com/whitead/molbloom](https://github.com/whitead/molbloom)
- **Publication**: [https://doi.org/10.1186/s13321-023-00765-1](https://doi.org/10.1186/s13321-023-00765-1)
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
