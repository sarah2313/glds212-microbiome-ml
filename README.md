# 🧬 GLDS-212 Microbiome Gene Expression Analysis

## Overview
This project explores and analyzes the **GLDS-212 dataset** from NASA’s GeneLab — a public collection of spaceflight-related omics data.
The goal is to **analyze microbial and gene expression patterns** in biological samples exposed to different spaceflight conditions.

The project aims to:
* Understand how **spaceflight affects microbial and host gene expression**.
* Build an **AI-assisted data analysis pipeline** for biological and space omics data.
* Demonstrate an **end-to-end workflow** — from raw FASTQ preprocessing to visualization and classification.
  
## Dataset Information
* **Dataset Name:** GLDS-212
* **Source:** [NASA GeneLab Data Repository](https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-212)
* **Description:** Contains microarray gene expression data from mouse gut microbiota exposed to microgravity and ground conditions.
* **Files Included:** Processed expression tables, metadata files, and sample information.
  
## Project Structure
```
GLDS-212/
│
├── data/
│   ├── raw/                  # Original data files (FASTQ / TXT)
│   ├── processed/            # Cleaned & filtered datasets
│   └── metadata/             # Sample info, experiment conditions
│
├── notebooks/
│   ├── 01_preprocessing.ipynb
│   ├── 02_quality_control.ipynb
│   ├── 03_differential_expression.ipynb
│   ├── 04_visualization.ipynb
│   └── 05_model_training.ipynb
│
├── results/
│   ├── plots/
│   ├── statistics/
│   └── reports/
│
├── scripts/
│   ├── data_cleaning.py
│   ├── analysis_pipeline.py
│   └── model.py
│
├── requirements.txt
└── README.md
```

## Tools & Technologies
* **Python** (pandas, numpy, matplotlib, seaborn, scikit-learn)
* **R / QIIME2 / DADA2** (for preprocessing microbial data if needed)
* **Jupyter Notebook** (for exploratory analysis)
* **GitHub** (for version control and collaboration)

## Main Steps in the Workflow
1. **Download & Inspect Data** – Retrieve data and metadata from NASA GeneLab.
2. **Preprocessing & Cleaning** – Filter low-quality reads or missing values.
3. **Normalization** – Adjust for biases in expression counts.
4. **Differential Expression Analysis** – Identify genes significantly affected by spaceflight.
5. **Visualization** – Generate PCA plots, heatmaps, and volcano plots.
6. **Machine Learning Integration** – Build a predictive model for biological classification or clustering.

## Output Examples
* Cleaned expression matrix
* List of differentially expressed genes
* Visualization plots (heatmaps, PCA)
* Model performance report

## Future Directions
* Extend the pipeline to integrate **multi-omics datasets (transcriptomics + microbiome)**.
* Apply **AI-driven feature selection and clustering**.
* Automate the entire workflow into a reproducible **bioinformatics pipeline**.

## Author
**Sarah Ahmed Badawi**
AI Engineer | ACTAIA – AI Solutions & Training Company
