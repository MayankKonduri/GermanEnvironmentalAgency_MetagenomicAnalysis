# Metagenomic (Transcriptomics) Viral Analysis Project Summary]
## Wastewater Monitoring of SARS-CoV-2 and Pathogens in Leipzig, Germany


> **Important Note:** This is not the entire of the project, most of the analysis was conducted on KBASE.

## **Notes:** https://docs.google.com/document/d/1vZHqGcQSfkYFBZaXUkSO1Slh_AaXgMW4f6ISO0NfxlQ/edit?usp=sharing

## Overview

During the SARS-CoV-2 pandemic, we conducted weekly monitoring of wastewater samples in Leipzig, Germany, using PCR techniques to track various pathogens. This project analyzes metagenomic and meta-transcriptomic profiles of microbial communities, focusing on the temporal dynamics of microbial populations, functional genes, and antibiotic resistance genes. Additionally, we aim to identify microbial indicators of specific environmental conditions and explore virome diversity and pathogenic viruses.

## Objectives

- Assess the temporal dynamics of microbial communities.
- Analyze functional genes and antibiotic resistance genes.
- Identify microbial indicators of specific environmental conditions.
- Investigate virome diversity and pathogenic viruses to understand seasonal variations and antiviral resistance.
- Explore the functional roles of viruses within microbial ecosystems, including the investigation of viral "dark matter" using RNA data to potentially disclose unknown viruses.

## Methodology

## Workflow Overview

| Step | Input                        | Tool            | Output                       |
|------|------------------------------|-----------------|------------------------------|
| 1    | Raw reads (FASTQ)             | Trimmomatic     | Trimmed reads (FASTQ)         |
| 2    | Trimmed reads (FASTQ)         | SPAdes          | Contigs (FASTA)               |
| 3    | Contigs (FASTA)               | QUAST           | Assembly quality metrics     |
| 4    | Contigs (FASTA)               | VirSorter2      | Viral contigs (FASTA)         |
| 5    | Viral contigs (FASTA)         | CheckV          | Viral genome quality metrics  |


## Tools and Dependencies

Ensure the following tools are installed and available in your `PATH`:

1. **[Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic)**: For adapter trimming and quality filtering.
2. **[SPAdes](https://cab.spbu.ru/software/spades/)**: For de novo genome assembly.
3. **[QUAST](http://quast.sourceforge.net/)**: For assessing assembly quality.
4. **[VirSorter2](https://github.com/jiarong/VirSorter2)**: For identifying viral sequences.


1. **Sample Collection:**
   - Weekly pooled samples from individual days per calendar week, covering calendar week 27 of 2021 to week 36 of 2022.

2. **Quality Control:**
   - **Trimming:** Utilized **Trimmomatic** for preprocessing raw data.
   - **Assembly:** Employed **RNA-Spades** for RNA assembly.
   - **Identification:** Used **FastViromeExplorer** for viral identification.

3. **Analysis:**
   - Integration of virological insights into microbial ecosystem modeling.
   - Applications in public health monitoring and risk assessment of wastewater-based epidemiology.

## Tools and Technologies

- **PCR:** Polymerase Chain Reaction for pathogen tracking.
- **Trimmomatic:** For quality trimming of RNA sequences.
- **RNA-Spades:** For assembling RNA sequences.
- **FastViromeExplorer:** For the identification of viral sequences.
- **Quast:** For quantifying attributes of identifies RNA sequences.

## Results

Our analysis provides insights into:

- Temporal dynamics of microbial communities.
- Functional genes related to antibiotic resistance.
- Identification of microbial indicators under varying environmental conditions.
- Virome diversity, including known and potentially unknown viruses.

## Future Work

This research has the potential to enhance public health monitoring and inform risk assessment strategies in wastewater-based epidemiology applications.

## References

1. Bolger, A. M., Lohse, M., & Usadel, B. (2014). Trimmomatic: A flexible trimmer for Illumina Sequence Data. *Bioinformatics*, btu170.

2. Arkin, A. P., Cottingham, R. W., Henry, C. S., Harris, N. L., Stevens, R. L., Maslov, S., et al. (2018). KBase: The United States Department of Energy Systems Biology Knowledgebase. *Nature Biotechnology*, 36, 566. doi: [10.1038/nbt.4163](https://doi.org/10.1038/nbt.4163)

3. Mikheenko, A., Saveliev, V., Hirsch, P., Gurevich, A. (2023). WebQUAST: online evaluation of genome assemblies. *Nucleic Acids Research*, 51(W1), W601–W606. doi: [10.1093/nar/gkad406](https://doi.org/10.1093/nar/gkad406)

4. Nayfach, S., Camargo, A. P., Schulz, F., et al. (2021). CheckV assesses the quality and completeness of metagenome-assembled viral genomes. *Nature Biotechnology*, 39, 578–585. doi: [10.1038/s41587-020-00774-7](https://doi.org/10.1038/s41587-020-00774-7)

