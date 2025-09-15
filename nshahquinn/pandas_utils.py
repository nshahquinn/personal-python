import pandas as pd

def read_tsv(file, na_values=[""], **kwargs):
    return pd.read_csv(
        file,
        sep="\t",
        keep_default_na=False,
        na_values=na_values,
        **kwargs
    )
        