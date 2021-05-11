import unittest
import iedb
import pandas as pd

class TestQuery(unittest.TestCase):
    def test_mhci_binding_req(self):
        res = iedb.query_mhci_binding(method="recommended", sequence="ARFTGIKTA", allele="HLA-A*02:01", length=8)
        self.assertIsNotNone(res)
        self.assertIsInstance(res, pd.core.frame.DataFrame)
        self.assertEqual(len(res), 2)
        self.assertEqual(res.columns.tolist(), 
                ['allele', 'seq_num', 'start', 'end', 'length', 'peptide', 'core','icore', 'score', 'percentile_rank']
        )
    def test_mhcii_binding_req(self):
        res = iedb.query_mhcii_binding(method="nn_align", sequence="SLYNTVATLYCVHQRIDV", allele="HLA-DRB1*01:01", length=None)
        self.assertIsNotNone(res)
        self.assertIsInstance(res, pd.core.frame.DataFrame)
        self.assertEqual(len(res), 4)
        self.assertEqual(res.columns.tolist(), 
                ['allele', 'seq_num', 'start', 'end', 'length', 'core_peptide', 'peptide', 'ic50', 'rank', 'adjusted_rank']
        )
    def test_tcell_epitope_req(self):
        res = iedb.query_tcell_epitope(method="smm", sequence="SLYNTVATLYCVHQRIDV", allele="HLA-A*01:01", length=9, proteasome='immuno')
        self.assertIsNotNone(res)
        self.assertIsInstance(res, pd.core.frame.DataFrame)
        self.assertEqual(len(res), 10)
        self.assertEqual(res.columns.tolist(), 
                ['allele', 'seq_num', 'start', 'end', 'length', 'peptide', 'proteasome_score', 'tap_score', 'mhc_score', 'processing_score', 'total_score', 'ic50_score']
        )
    def test_peptide_prediction_req(self):
        res = iedb.query_peptide_prediction(method="mhcnp", sequence="SLYNTVATLYCVHQRIDV", allele="HLA-A*02:01", length=9)
        self.assertIsNotNone(res)
        self.assertIsInstance(res, pd.core.frame.DataFrame)
        self.assertEqual(len(res), 10)
        self.assertEqual(res.columns.tolist(), 
                ['allele', 'seq_num', 'start', 'end', 'length', 'peptide', 'prob_score']
        )
    def test_bcell_epitope_req(self):
        res = iedb.query_bcell_epitope(method="Emini", sequence="VLSEGEWQLVLHVWAKVEADVAGHGQDILIRLFKSHPETLEKFDRFKHLKTE", window_size=9)
        self.assertIsNotNone(res)
        self.assertIsInstance(res, pd.core.frame.DataFrame)
        self.assertEqual(len(res), 44)
        self.assertEqual(res.columns.tolist(), 
                ['Position', 'Residue', 'Start', 'End', 'Peptide', 'Score']
        )


if __name__ == '__main__':
    unittest.main()