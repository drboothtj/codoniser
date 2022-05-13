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

if __name__ == '__main__':
    main()
