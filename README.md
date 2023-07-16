# MolBloom: molecule purchasability in ZINC20

This model uses a Bloom filter to query the ZINC20 database to identify if a molecule is purchasable. A bloom filter is a space-efficient probabilistic data structure to identify whether an element is in a given set. Due to the nature of bloom filters, false negatives are not possible (i.e if the model returns False, the molecule is not purchasable). As stated by the author, if the model returns True the molecule is purchasable with an error rate of 0.0003 (according to the ZINC20 catalog).

## Identifiers

* EOS model ID: `eos8a5g`
* Slug: `molbloom`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Boolean`
* Output Type: `String`
* Output Shape: `Single`
* Interpretation: It returns a boolean (True/False) suggesting whether the molecule is commercially available or not.

## References

* [Publication](https://github.com/whitead/molbloom/blob/main/CITATION.cff)
* [Source Code](https://github.com/whitead/molbloom)
* Ersilia contributor: [Amna-28](https://github.com/Amna-28)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos8a5g)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8a5g.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos8a5g) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://github.com/whitead/molbloom/blob/main/CITATION.cff) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!