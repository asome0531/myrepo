# myrepo

This project focused on human herpesvirus 5 which is also known as cytomegalovirus and is typically abbreviated as HCMV. We will be creating a python pipeline using wrapper script to help run this code in one command line. There are two different tracks in this project, but we will be soley focusing on track 2 where we would like to compare HCMV transcriptomes 2- and 6-days post infection. 

First we retrieved 2 paitents transcriptomes from SRA and coverted to paird-end fastq files using wget by constructing the URL path based on the SRR numbers for each of these smaples. 

Donor 1 (2dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896360
Donor 1 (6dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896363
Donor 3 (2dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896374
Donor 3 (6dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896375


This pipeline automates the analysis of transcriptome data, including mapping reads to the HCMV genome. assembling the mapped reads, and analyzing the resulting assembly. 

# Requirements
- Python 3.x
- Bowtie2
- SPAdes

## How to convert each file into fastq
1. First click on the link, find 'RUN' click on the run numbers which start with 'SRR'
2. You will be moved into the metadata page, from the opetions choose 'Data Access'
3. Copy the 'AWS' link/address and head back to your terminal, and put in the following command: 
        wget (post the link/address you copied earlier)
4. Use the followig command to split the file: 
        fastq-dump -I --split-files (file name)
5. follow the same steps for every link until you have a total of 12 files, which includes the main files, and the split files. Each file would create two spilt files. 
6. Lastly, run the following command to the mutliple pair-end reads:
        spades.py -k 77,99,127 -t 2 --pe1-1 sample1_1.fastq --pe1-2 sample1_2.fastq --pe2-1 sample2_1.fastq --pe2-2 sample2_2.fastq --pe3-1 sample3_1.fastq --pe3-2 sample3_2.fastq (and so on if you have more samples)
Note: this will take from 60-120minutes to run and compile together. 

# Installation 

1. clone this repository to your local machine: 

 ''' bash 

        git clone https://github.com/asome0531/myrepo.git
 '''

2. Install Python dependecies: 

 ''' bash 
        pip install -r requirements.txt
 '''

# Usage

1. Place your FASTQ giles for transcriptome reads in the 'data' directory.
2. Edit the 'config.yaml' file to specify the input FASTQ files and other parameters if necessary. 
3. run the pipeline sctipt: 
 '''bash
        python pipeline.py
 '''

4. Monitor the progress of the pipeline and check the generated log gile ('pipeline log') for any errors or warnings.

# Output 

- Mapped reads: 'mapped_reads.sam'
- Assembly output: 'assembly_output/contigs.fasta'
- BLAST output: 'blast_output.txt'
- Log file: 'pipeline.log'

# Troubleshooting

If you encounter any issues while running the pipeline, please check the log file for error messages and consult the documentation for each tool used in the pipeline (Bowtie2, SPAdes) for troubleshotting tips. 


