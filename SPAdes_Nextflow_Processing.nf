#!/usr/bin/env nextflow

params.inputDir = "/Users/mayank/Downloads/Output_RNA_Trim/"
params.outputDir = "/Users/mayank/Downloads/Output_Spades_Data/trial2/"

totalReads = 0

process countReads {
    input:
    file(trimmed_R1) from "${params.inputDir}/trimmed_paired_RNAKW0322_R1.fastq.gz"
    file(trimmed_R2) from "${params.inputDir}/trimmed_paired_RNAKW0322_R2.fastq.gz"
    file(pacbio_reads) from "${params.inputDir}/combined_trimmed_single_RNAKW0322.fastq.gz"

    script:
    """
    totalReads += \`zcat \${trimmed_R1} | wc -l\`
    totalReads += \`zcat \${trimmed_R2} | wc -l\`
    totalReads += \`zcat \${pacbio_reads} | wc -l\`
    """
}

process spades {

    input:
    file(trimmed_R1) from "${params.inputDir}/trimmed_paired_RNAKW0322_R1.fastq.gz"
    file(trimmed_R2) from "${params.inputDir}/trimmed_paired_RNAKW0322_R2.fastq.gz"
    file(pacbio_reads) from "${params.inputDir}/combined_trimmed_single_RNAKW0322.fastq.gz"

    script:
    """
    echo "Running SPAdes with the following inputs:"
    echo "  - Paired-end reads 1: \${trimmed_R1}"
    echo "  - Paired-end reads 2: \${trimmed_R2}"
    echo "  - PacBio reads: \${pacbio_reads}"
    echo "  - Output directory: \${params.outputDir}"

    /Users/mayank/Downloads/SPAdes-4.0.0/bin/spades.py \\
        -1 \${trimmed_R1} \\
        -2 \${trimmed_R2} \\
        --pacbio \${pacbio_reads} \\
        -o \${params.outputDir} \\
        --meta
    """

    script:
    """
    currentReads = \`zcat \${trimmed_R1} | wc -l\`
    currentReads += \`zcat \${trimmed_R2} | wc -l\`
    currentReads += \`zcat \${pacbio_reads} | wc -l\`
    progress = (currentReads * 100) / totalReads
    println "Progress: \${progress}%"
    """
}

workflow {
    spades
}
