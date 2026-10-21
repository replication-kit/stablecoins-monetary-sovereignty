# Stablecoins and Monetary Sovereignty

Replication materials for the paper:

**Stablecoins and Monetary Sovereignty: A Theory of Functional Fragmentation**

This repository contains the code used to generate Figure 1, which illustrates multiple equilibria under strong network effects in the paper's baseline model.

## Repository structure

```text
stablecoins-monetary-sovereignty/
├─ code/
│  └─ figure1_multiple_equilibria.py
├─ figures/
├─ requirements.txt
└─ README.md
```

The `figures/` directory is used for generated output and is created automatically if needed.

## Figure 1

Figure 1 illustrates the equilibrium condition

```text
x = F(z + alpha x)
```

using a standard logistic distribution and `alpha = 6`. This parameterization is used only for illustration. The analytical results in the paper are stated for a broader class of unimodal cost distributions.

The solid branches denote locally stable equilibria, the dashed branch denotes the locally unstable equilibrium, and the vertical dotted lines indicate the two saddle-node thresholds.

## Reproduction

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the script from the repository root:

```bash
python code/figure1_multiple_equilibria.py
```

The script writes:

```text
figures/figure1_multiple_equilibria_bw_v4.png
figures/figure1_multiple_equilibria_bw_v4.eps
```

## Requirements

- Python 3
- NumPy
- Matplotlib

## Scope

The code reproduces the illustrative figure only. The propositions and proofs in the paper are analytical; the numerical parameterization used here is not required for the theoretical results.

## Paper status

Working paper. Repository contents may be updated as the manuscript is revised.
