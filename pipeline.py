import os
import subprocess

# Step1: Setting up a directory strucutre
# Create a directory for the project
os.system("mkdir PipelineProject__")

# Change into the project directory
os.chdir("PipelineProject__")

# Step2: Bowtie2 indexing and mapping
def bowtie2_indexing():
	#Create Bowtie2 index for HCMV
	subprocess.run(["bowtie2-build", "NC_006273.2.fasta", "HCMV_index"])
	#run Bowtie2 mapping
	subprocess.run(["spades.py", "-o", "assembley_output", "-1", "sample_1.fastq", "-2", "sample_2.fastq", "-S", "sample.sam"])

# Step3: SPAdes assembly
def spades_assembly():
	#Assmeble transcriptomes with SPAdes
	subprocess.run(["spades.py", "-o", "assembly_output", "-1", "sample_1.fastq", "-2", "sample_2.fastq"])

# Step4: Contig analysis
def contig_analysis():
	# Calculate number of config > 1,000 bp
	subprocess.run(["python", "contig_analysis.py"])

# Step5: BLAST alignment
def blast_alignment():
	# Retrieve longest contig from SPAdes assembly
	subprocess.run(["python", "retrieve_longest_contig.py"])
	# Create local database for betaherpesvirinae subfamily
	subprocess.run(["makeblastb", "-in", "betaherpesvirinae.fasta", "-dbtype", "nucl"])
	#Run BLAST alignment
	subprocess.run(["blastn", "-in", "longest_contig.fasta", "-db", "betaherpesvirinae.fasta", "-out", "blast_output.xml", "outfmt", "5"])

# Step6: Logging
def log_results():
	with open("PipelineProject.log", "w") as logfile:
	logfile.write("Log gile for PipelineProject\n\n")
	# Write results of each step to log file
	Logfile.write("Step 2: Bowtie2 indexing and mapping\n")

# Step7: Execute the pipeline
def execute_pipeline():
	bowtie2_indexing()
	spades_assembly()
	contig_anaylsis()
	blast_alignment()
	log_results()

# Step8: run the pipeline
execute_pipeline()
