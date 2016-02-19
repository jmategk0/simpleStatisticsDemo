# This is an example for how to use simpleStatistics
# all the data files may be pulled from here:
# ftp://ftp.ncbi.nlm.nih.gov/pathogen/Results/Campylobacter/
# ftp://ftp.ncbi.nlm.nih.gov/pathogen/Results/Escherichia_coli_Shigella/
# ftp://ftp.ncbi.nlm.nih.gov/pathogen/Results/Listeria/
# ftp://ftp.ncbi.nlm.nih.gov/pathogen/Results/Salmonella/
# ftp://ftp.ncbi.nlm.nih.gov/pathogen/

import parseUtility
import simpleStatistics

# files are named below
campylobacter_file = "campy.metadata.tsv"
escherichia_coli_file = "ecoli.metadata.tsv"
listeria_file = "lmono.metadata.tsv"
salmonella_file = "sal.metadata.tsv"
text_file_delimiter = "\t"

# numeric fields in the datafiles are listed below
genome_size = "asm_stats_length_bp"
contig_number = "asm_stats_n_contig"
draft_n50 = "asm_stats_contig_n50"

# The parse parse utility converts text files to python data structures
parser = parseUtility.ParseUtility()
descriptive_statistics = simpleStatistics.DescriptiveStatistics()
inferential_statistics = simpleStatistics.InferentialStatistics()

# Load data from file, query the size of every genome, and cleanup the data before downstream analysis
draft_genome_dataset = parser.load_data(salmonella_file, text_file_delimiter)  # update genome file here
genome_sizes = parser.select_row_from_list_of_dictionaries(draft_genome_dataset, genome_size) # update field
clean_genome_sizes = parser.clean_list(genome_sizes)

# You can call basic descriptive statistics individually such as mean, median, mode, and standard_deviation
mean_genome_size = descriptive_statistics.mean(clean_genome_sizes)
median_genome_size = descriptive_statistics.median(clean_genome_sizes)
range_genome_size = descriptive_statistics.standard_deviation(clean_genome_sizes, is_population=False)

# Or you can call all basic descriptive statistics with one line of code
summarised_data = descriptive_statistics.summarise_descriptive_statistics(clean_genome_sizes)
# For simplicity data is returned as a dictionary

# descriptive statistics can be plugged into the inferential statistics class
z_score_of_max = inferential_statistics.z_score_calculate(summarised_data["maximum"], summarised_data["mean"], summarised_data["standard_deviation"])
score_at_z_3 = inferential_statistics.score_value_from_z_score(summarised_data["mean"], summarised_data["standard_deviation"], 3.0)

# prints results to console
print(summarised_data)
print(z_score_of_max)
print(score_at_z_3)
