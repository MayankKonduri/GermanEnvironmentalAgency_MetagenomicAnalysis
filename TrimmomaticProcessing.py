java -jar /Users/mayank/Downloads/trimmomatic-0.39/trimmomatic-0.39.jar PE \
/Users/mayank/Downloads/RNAKW2422_R1_001.fastq.gz /Users/mayank/Downloads/RNAKW2422_R2_001.fastq.gz \
/Users/mayank/Downloads/Output_RNA_Trim/trimmed_paired_RNAKW2422_R1.fastq.gz /Users/mayank/Downloads/Output_RNA_Trim/trimmed_single_RNAKW2422_R1.fastq.gz \
/Users/mayank/Downloads/Output_RNA_Trim/trimmed_paired_RNAKW2422_R2.fastq.gz /Users/mayank/Downloads/Output_RNA_Trim/trimmed_single_RNAKW2422_R2.fastq.gz \
ILLUMINACLIP:/Users/mayank/Downloads/trimmomatic-0.39/adapters/TruSeq3-PE.fa:2:30:10:2:True SLIDINGWINDOW:4:15 LEADING:3 TRAILING:3 MINLEN:36
