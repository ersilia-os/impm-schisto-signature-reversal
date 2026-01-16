import mygene

def ensembl_to_entrez_symbol(ensembl_id):
    """
    Convert an Ensembl Gene ID to Entrez Gene Symbol using mygene.
    Args:
        ensembl_id (str): Ensembl Gene ID (e.g., 'ENSG00000139618')
    Returns:
        str or None: Entrez Gene Symbol if found, else None
    """
    mg = mygene.MyGeneInfo()
    result = mg.query(ensembl_id, scopes='ensembl.gene', fields='symbol', species='human')
    if result and 'hits' in result and result['hits']:
        return result['hits'][0].get('symbol')
    return None

# Example usage:
# symbol = ensembl_to_entrez_symbol('ENSG00000139618')
# print(symbol)
