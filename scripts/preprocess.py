#!/usr/bin/env python3
"""Preprocess ASV table: filter low counts."""
import pandas as pd

def main(metadata_fp='data/metadata.csv', asv_fp='data/asv_table.tsv', out_fp='data/asv_counts_filtered.tsv'):
    meta = pd.read_csv(metadata_fp, index_col=0)
    asv = pd.read_csv(asv_fp, sep='\t', index_col=0)
    asv = asv.loc[asv.sum(axis=1) >= 10]
    asv.to_csv(out_fp, sep='\t')
    print(f"Filtered ASV saved to {out_fp}")

if __name__ == '__main__':
    main()
