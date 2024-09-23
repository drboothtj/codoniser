'''
main routine for codoniser
    functions:
        !!!
'''
from typing import List
from codoniser.utils import io, parser
from codoniser.utils.classes import CDS
from codoniser.plotting.barchart import plot_barchart

'''
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
        #add midpoint and counts to data
        start_point += step_size
        end_point = start_point + window_size
    #return x
'''

def get_cdses_from_fasta(files: List[str]) -> List[CDS]: #change type hint to list of cds objects
    '''
    generates cds objects for each protein in a list of fasta files
        arguments: 
            files:
                list of paths to fasta files
        returns:
            cdses:
                a list of cds objects
    '''
    cdses = []
    for file in files:
        sequence_names, sequences = io.read_cds_from_records(file, 'fasta')
        for sequence_name, sequence in zip(sequence_names, sequences):
            cds = CDS(source=file, name=sequence_name, sequence=sequence)
            cdses.append(cds)
    return cdses

def get_cdses_from_genbank(files: List[str]) -> List: #change type hint to list of cds objects
    pass

def main():
    '''
    main routine for codoniser
        args:
            None
        returns:
            None
    '''
    #io.print_to_system('Running codoniser!') ADD LOGGING
    args = parser.parse_args()
    if args.mode == 'fasta':
        cdses = get_cdses_from_fasta(args.files)
    elif args.mode == 'genbank':
        cdses = get_cdses_from_genbank(args.files)
    else:
        print('add a propper error!')
        exit()

    plot_barchart(cdses)
    #heatmap

    print('done')

    '''
    #make a more useful datastructure
    codons = get_codons(record_sequences)
    codon_table = get_codon_table(codons)
    io.list_to_csv('codon_table.csv', codon_table)
    #compare all vs all correlation (pearsons and the other on...)
    
    step_size = 20 #parse input
    window_size = 100 #parse input
    get_codon_distribution(codons, step_size, window_size)
    plot_codon_distribution
    '''
if __name__ == '__main__':
    main()
