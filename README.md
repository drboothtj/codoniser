# codoniser
visualise codon usage and codon usage correlation

## Description
WIP

## Installation

You can install `codoniser` with `pip`.

Either use the PyPI installation: `pip install egger`.

Or, clone this repository and install manually. 

`codoniser` requires only Python dependencies, which should be installed automatically. 

## Usage

`codoniser` takes fasta nucleic acid files (`.fna`) as positional input. This file should contain the DNA sequences of all ORFs from the source genome.
Be careful to ensure that you have not included pseudogenes or other none-CDS sequences as this will interfer with the analysis (and probably cause an error!).
Example input can be found, [here](https://github.com/drboothtj/codoniser/example_data/example_in).

`codoniser` currently offers three analyses:

-  `-b` will plot a bar chart of the codon usage. You can plot one, or many genomes.
-  `-p` will plot a heatmap of the codon usage correlation (Pearsons's Rank)between the genomes. You must plot at least three genomes.
-  `-s` will plot a heatmap of the codon usage correlation (Spearman's rank) between the genomes. You must plot at least three genomes.


Therefore, to run all three analysis you can run, for example:

`codoniser -b -p -s *.fna`

## Output
`codoniser` produces a number of tables and figures as output. The example outputs can be found, [here](https://github.com/drboothtj/codoniser/example_data/example_out).

### Bar chart
`codoniser` can produce simple bar charts.

WIP

### Spearman's and Pearson's Rank

WIP

## Citation
Coming soon...

## Version History
- 1.0.0
  - Initial release
