
# IEDB API Tools Python SDK  
  
### Python SDK for Immune Epitope Database (IEDB) Analysis Tools API. Includes support for the following prediction tools:  
  
- MHC-I peptide binding:  
  - Determine sequence's ability to bind to MHC class I molecule  
- MHC-II peptide binding:  
  - Determine sequence's ability to bind to MHC class II molecule  
- T-cell epitope prediction:  
  - Use predictors to determine peptide's potential of being a T-cell epitope  
- MHC-Natural Peptide:  
  - Assess probability that peptide is naturally processed by the MHC  
- Antibody epitope prediction:  
  - Predict B-cell epitopes from protein sequence(s)
  
View the [web application](http://tools.iedb.org/main/)  
  
## Installation  
  
Run the following to install:
```python  
pip install iedb
```  

## Usage  
  
```python
import iedb

# Send POST request to MHC class I peptide binding prediction tool:
mhci_res = iedb.query_mhci_binding(method="recommended", sequence="ARFTGIKTA", allele="HLA-A*02:01", length=8)

# Send POST request to MHC class II peptide binding prediction tool:
mhcii_res = iedb.query_mhcii_binding(method="nn_align", sequence="SLYNTVATLYCVHQRIDV", allele="HLA-DRB1*01:01", length=None)

# Send POST request to T-cell epitope prediction tool:
tcell_res = iedb.query_tcell_epitope(method="smm", sequence="SLYNTVATLYCVHQRIDV", allele="HLA-A*01:01", length=9, proteasome='immuno')

# Send POST request to peptide prediction tool:
pep_res = iedb.query_peptide_prediction(method="mhcnp", sequence="SLYNTVATLYCVHQRIDV", allele="HLA-A*02:01", length=9)

# Send POST request to B-cell epitope prediction tool:
bcell_res = iedb.query_bcell_epitope(method="Emini", sequence="VLSEGEWQLVLHVWAKVEADVAGHGQDILIRLFKSHPETLEKFDRFKHLKTE", window_size=9)

```