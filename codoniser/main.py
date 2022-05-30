import re
from collections import Counter
from codoniser import io, parser

def get_codons(sequences):
    codons = []
    for sequence in sequences:
        codon = re.findall('...', str(sequence))
        codons.extend(codon)
    return codons

def get_codon_table(codons):
    codon_counts = Counter(codons)
    triplet_nt = []
    triplet_count = []
    triplet_percentage = []
    codon_table = ['codon','count','percentage']
    for triplet, count in codon_counts.items():
        triplet_nt.append(triplet)
        triplet_count.append(count)
    total_count = sum(triplet_count)
    for count in triplet_count:
        triplet_percentage.append((count/total_count)*100)
    for i in range(0,len(triplet_nt)):
        codon_table.append([triplet_nt[i], triplet_count[i],triplet_percentage[i]])
    return codon_table

def get_codon_distribution(codons, step_size, window_size):
    start_point = 0
    end_point = start_point + window_size
    while end_point < len(codons):
        window_codons = codons [start_point:end_point]
        mid_point = start_point + ((start_point - end_point)/2)
        codon_count = Counter(window_codons)
        print(codon_count)
        #add midpoint and counts to data
        start_point += step_size
        end_point = start_point + window_size
    #return x


def main():
    io.print_to_system('Running codoniser version 0.1.0!')
    args = parser.parse_args()

    if args.fasta != None:
        filename = args.fasta
        record_names, record_sequences = io.read_file(filename, "fasta")
    elif args.genbank != None:
        filename = args.genbank
        record_names, record_sequences = io.read_file(filename, "genbank") ###NEEDS EDITING TO EXTRACT CDSs
    else:
        io.print_to_system("No input provided; exiting.")
        exit()
    
    codons = get_codons(record_sequences)
    codon_table = get_codon_table(codons)
    io.list_to_csv('codon_table.csv', codon_table)
    
    step_size = 20 #parse input
    window_size = 100 #parse input
    get_codon_distribution(codons, step_size, window_size)
    plot_codon_distribution
    
if __name__ == '__main__':
    main()
