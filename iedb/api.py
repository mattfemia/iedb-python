from typing import Union
import re
import pandas as pd
import requests

def query_mhci_binding(method: str, sequence: Union[str, list], allele: Union[str, list], length: Union[int, list]):
    '''
    Query IC50 values for MHC class I peptide binding of either a single amino 
    acid sequence or set of sequences to an MHC class I molecule. Sends POST 
    request to IEDB API. 

    IEDB official web tool can be found here: http://tools.iedb.org/mhci/

            Parameters:
                    method (str): MHC class I binding prediction method. 
                        Available argument options (format: method-version):
                            - recommended
                            - ann-4.0
                            - comblib_sidney2008-1.0
                            - consensus-2.18
                            - netmhccons-1.1
                            - netmhcpan_ba-4.1
                            - netmhcpan_ba-4.0
                            - netmhcpan_el-4.1
                            - netmhcpan_el-4.0
                            - netmhcstabpan-1.0
                            - pickpocket-1.1
                            - smm-1.0
                            - smmpmbec-1.0
                        More information on prediction methods can be found 
                        here: http://tools.iedb.org/mhci/help/#Method

                    sequence ([str, list]): Peptide amino acid sequence or
                        list of sequences.
                    allele ([str, list]): HLA allele. Ex.) HLA-A*02:01
                    length ([int, list]): Peptide length or list of lengths

            Returns:
                    dataframe (pandas.DataFrame): Tabular results formatted
                        as pandas.DataFrame
    '''
    url = 'http://tools-cluster-interface.iedb.org/tools_api/mhci/'
    data = {
        'method': method,
        'sequence_text': sequence, 
        'allele': allele,
        'length': length
    }

    res = requests.post(
        url=url,
        data=data
    )

    if res.status_code != 200:
        print('Error: Query returned non-200 status code.')
        return None

    # Format response data
    res_decoded = re.split(r'\n+', res.text) # Response is formatted in tab-delimited string
    column_headers = re.split(r'\t+', res_decoded[0]) # First result of split is col headers
    data = [re.split(r'\t+', entry) for entry in res_decoded[1: -1]] 

    # Create pandas.DataFrame
    dataframe = pd.DataFrame(data, columns=column_headers)

    return dataframe

def query_mhcii_binding(method: str, sequence: Union[str, list], allele: Union[str, list], length: Union[int, list]):
    '''
    Query IC50 values for MHC class II peptide binding of either a single amino 
    acid sequence or set of sequences to an MHC class II molecule. Sends POST 
    request to IEDB API. 

    IEDB official web tool can be found here: http://tools.iedb.org/mhcii/

            Parameters:
                    method (str): MHC class II binding prediction method. 
                        Available argument options (format: method-version):
                            - recommended
                            - consensus-2.22
                            - consensus-2.18
                            - netmhciipan-4.0
                            - netmhciipan-3.2
                            - netmhciipan-3.1
                            - smm_align-1.1
                            - nn_align-2.3
                            - nn_align-2.2
                            - comblib-1.0
                            - tepitope-1.0
                        More information on prediction methods can be found 
                        here: http://tools.iedb.org/mhcii/help/#Method

                    sequence ([str, list]): Peptide amino acid sequence or
                        list of sequences.
                    allele ([str, list]): Single or multiple HLA alleles. 
                        Provide single alleles as a string. Multiple alleles
                        should be formatted in a comma separated list. Example
                        below:
                            Ex.) HLA-DRB1*01:01
                        To run alpha and beta chains together format as such:
                            Ex.) DPA1*01/DPB1*04:01"
                    length ([int, list]): Peptide length or list of lengths

            Returns:
                    dataframe (pandas.DataFrame): Tabular results formatted
                        as pandas.DataFrame
    '''
    url = 'http://tools-cluster-interface.iedb.org/tools_api/mhcii/'
    data = {
        'method': method,
        'sequence_text': sequence, 
        'allele': allele,
        'length': length
    }

    res = requests.post(
        url=url,
        data=data
    )

    if res.status_code != 200:
        print('Error: Query returned non-200 status code.')
        return None

    # Format response data
    res_decoded = re.split(r'\n+', res.text) # Response is formatted in tab-delimited string
    column_headers = re.split(r'\t+', res_decoded[0]) # First result of split is col headers
    data = [re.split(r'\t+', entry) for entry in res_decoded[1: -1]] 

    # Create pandas.DataFrame
    dataframe = pd.DataFrame(data, columns=column_headers)

    return dataframe

def query_tcell_epitope(method: str, sequence: Union[str, list], allele: Union[str, list], length: Union[int, list], proteasome: str):
    '''
    Query prediction tool used to produce overall score for each peptide's 
    intrinsic potential of being a T cell epitope.
    
    Algorithm combines predictors of proteasomal processing, TAP transport, 
    and MHC binding to produce score.

    IEDB official web tool can be found here: http://tools.iedb.org/processing/

            Parameters:
                    method (str): Prediction method. Available argument 
                        options:
                            - recommended
                            - netmhcpan
                            - ann
                            - smmpmbec
                            - smm
                            - comblib_sidney2008
                            - netmhccons
                            - pickpocket
                        More information on prediction methods can be found 
                        here: http://tools.iedb.org/processing/help/#Method

                    sequence ([str, list]): Peptide amino acid sequence or
                        list of sequences.

                    allele ([str, list]): Single or multiple HLA alleles. 
                        Provide single alleles as a string. Multiple alleles
                        should be formatted in a comma separated list. Example
                        below:
                            Ex.) HLA-A*02:01

                    length ([int, list]): Peptide length or list of lengths.
                        Possible lengths:
                            - 8, 9, 10, 11, 12, 13, 14	

                    proteasome (str): Must be either 'immuno' or 'constitutive'
                            Options reference the two types of proteasomes, the 
                            constitutively expressed 'house-keeping' type, 
                            and immuno proteasomes that are induced by IFN-γ 
                            secretion.

            Returns:
                    dataframe (pandas.DataFrame): Tabular results formatted
                        as pandas.DataFrame
    '''
    url = 'http://tools-cluster-interface.iedb.org/tools_api/processing/'
    data = {
        'method': method,
        'sequence_text': sequence,
        'allele': allele,
        'length': length,
        'proteasome': proteasome
    }

    res = requests.post(
        url=url,
        data=data
    )

    if res.status_code != 200:
        print('Error: Query returned non-200 status code.')
        return None

    # Format response data
    res_decoded = re.split(r'\n+', res.text) # Response is formatted in tab-delimited string
    column_headers = re.split(r'\t+', res_decoded[0]) # First result of split is col headers
    data = [re.split(r'\t+', entry) for entry in res_decoded[1: -1]] 

    # Create pandas.DataFrame
    dataframe = pd.DataFrame(data, columns=column_headers)

    return dataframe

def query_peptide_prediction(method: str, sequence: Union[str, list], allele: Union[str, list], length: Union[int, list]):
    '''
    Request data to predict probability that a given peptide is naturally
    processed and binds to a given MHC molecule.
    
    Uses data obtained from MHC elution experiments.

    IEDB official web tool can be found here: http://tools.iedb.org/mhcnp/

            Parameters:
                    method (str): Peptide-MHC prediction method. 
                        Available argument options (format: method-version):
                            - netmhcpan
                            - mhcnp
                        More information on prediction methods can be found 
                        here: http://tools.iedb.org/mhcnp/help/#Method

                    sequence ([str, list]): Peptide amino acid sequence or
                        list of sequences.

                    allele ([str, list]): Single or multiple HLA alleles. 
                        Provide single alleles as a string. Multiple alleles
                        should be formatted in a comma separated list. 
                        
                        ** Tool currently only supports the following alleles:
                             - HLA-A*02:01
                             - HLA-B*07:02
                             - HLA-B*35:01
                             - HLA-B*44:03
                             - HLA-B*53:01
                             - HLA-B*57:01
                             - H-2-Db
                             - H-2-Kb

                    length ([int, list]): Peptide length or list of lengths.
                        Possible lengths:
                            - 8, 9, 10, 11, 12, 13, 14

            Returns:
                    dataframe (pandas.DataFrame): Tabular results formatted
                        as pandas.DataFrame
    '''
    url = 'http://tools-cluster-interface.iedb.org/tools_api/mhcnp/'
    data = {
        'method': method,
        'sequence_text': sequence,
        'allele': allele,
        'length': length
    }

    res = requests.post(
        url=url,
        data=data
    )

    if res.status_code != 200:
        print('Error: Query returned non-200 status code.')
        return None

    # Format response data
    res_decoded = re.split(r'\n+', res.text) # Response is formatted in tab-delimited string
    column_headers = re.split(r'\t+', res_decoded[0]) # First result of split is col headers
    data = [re.split(r'\t+', entry) for entry in res_decoded[1: -1]] 

    # Create pandas.DataFrame
    dataframe = pd.DataFrame(data, columns=column_headers)

    return dataframe

def query_bcell_epitope(method: str, sequence: Union[str, list], window_size: int):
    '''
    Request prediction for continuous antibody epitope from protein sequences.
    Prediction parameters span focus on  hydrophilicity, flexibility, 
    accessibility, turns, exposed surface, polarity and antigenic propensity of
    polypeptides chains.

    IEDB official web tool can be found here: http://tools.iedb.org/bcell/

            Parameters:
                    method (str): Methods for predicting continuous antibody 
                        epitope from protein sequences. 
                        
                        Available argument options:
                            - Bepipred
                            - Bepipred-2.0
                            - Chou-Fasman
                            - Emini
                            - Karplus-Schulz
                            - Kolaskar-Tongaonkar
                            - Parker

                        More information on prediction methods can be found 
                        here: http://tools.iedb.org/bcell/help/#Method

                    sequence ([str, list]): Peptide amino acid sequence or
                        list of sequences.

                    window_size (int): Number of flanking residues for a single
                        given residue when calculating scores. 
                        
                        More from IEDB: 
                        
                        "When computing the score for a given residue i, the 
                        amino acids in an interval of the chosen length, 
                        centered around residue i, are considered. In other 
                        words, for a window size n, the i - (n-1)/2 neighboring
                        residues on each side of residue i were used to 
                        compute the score for residue i. Unless specified, 
                        the score for residue i is the average of the scale 
                        values for these amino acids (see table 1 for specific
                        method implementation details). In general, a window
                        size of 5 to 7 is appropriate for finding regions 
                        that may potentially be antigenic."

            Returns:
                    dataframe (pandas.DataFrame): Tabular results formatted
                        as pandas.DataFrame
    '''
    url = 'http://tools-cluster-interface.iedb.org/tools_api/bcell/'
    data = {
        'method': method,
        'sequence_text': sequence,
        'window_size': window_size
    }

    res = requests.post(
        url=url,
        data=data
    )

    if res.status_code != 200:
        print('Error: Query returned non-200 status code.')
        return None

    # Format response data
    res_decoded = re.split(r'\n+', res.text) # Response is formatted in tab-delimited string
    column_headers = re.split(r'\t+', res_decoded[0]) # First result of split is col headers
    data = [re.split(r'\t+', entry) for entry in res_decoded[1: -1]] 

    # Create pandas.DataFrame
    dataframe = pd.DataFrame(data, columns=column_headers)

    return dataframe
