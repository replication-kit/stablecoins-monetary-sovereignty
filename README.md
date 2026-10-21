# Stablecoins and Monetary Sovereignty

Replication materials for the paper:

**Stablecoins and Monetary Sovereignty: A Theory of Functional Fragmentation**

This repository currently contains the code used to generate Figure 1, which illustrates multiple equilibria under strong network effects in the paper's baseline model.

## Repository structure

```text
stablecoins-monetary-sovereignty/
├─ code/
│  └─ figure1_multiple_equilibria.py
├─ figures/
│  ├─ figure1_multiple_equilibria_bw_v4.png
│  └─ figure1_multiple_equilibria_bw_v4.eps
├─ requirements.txt
└─ README.md
```

## Figure 1

Figure 1 illustrates the equilibrium condition

```text
x = F(z + alpha x)
```

using a standard logistic distribution and `alpha = 6`. The parameterization is illustrative; the analytical results in the paper are stated for a broader class of unimodal cost distributions.

The solid branches denote locally stable equilibria and the dashed branch denotes the locally unstable equilibrium. The vertical dotted lines indicate the two saddle-node thresholds.

## Reproduction

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python code/figure1_multiple_equilibria.py
```

The script produces both PNG and EPS versions of Figure 1.

## Requirements

- Python 3
- NumPy
- Matplotlib

## Notes

The repository is intended to document and reproduce the computational material used in the paper. The theoretical propositions and proofs are derived analytically in the manuscript; the code is used only to produce the illustrative figure.
