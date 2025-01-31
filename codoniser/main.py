'''
main routine for codoniser
    functions:
        !!!
'''
from typing import List
from collections import Counter

from codoniser.utils import io, parser
from codoniser.utils.classes import CDS
from codoniser.utils.errors import NoAnalysisError
from codoniser.plotting.barchart import plot_barchart
from codoniser.plotting.heatmap import rank

'''
consider adding sliding window one day...

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

def get_cdses_from_fasta(files: List[str]) -> List[CDS]: 
    '''
    generates cds objects for each cds in a fasta file
        arguments: 
            file:
                paths to fasta file
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

def get_data(cdses):
    '''
    '''
    labels = list({cds.source for cds in cdses})
    counters = get_totals(cdses, labels)
    assert len(labels) == len(counters)
    categories = {key for counter in counters for key in counter.keys()}
    return labels, counters, categories 

def get_totals(cdses: List[CDS], labels: List[str]) -> List[Counter]:
    '''
    Combines and extracts counters from cdses relative to the labels
        arguments:
            cdses:
                list of CDS objects
            labels:
                list of lables
        returns:
            counters:
                list of counters
    '''
    counters = []
    for label in labels:
        counter = Counter()
        for cds in cdses:
            if cds.source == label:
                counter += cds.codon_count()
        counters.append(counter)
    return counters


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
    cdses = get_cdses_from_fasta(args.files)
    #set a flag to ensure some analysis was done
    analysis_complete = False
    sources, counters, categories = get_data(cdses)
    #barcharts
    if args.barchart:
        plot_barchart(sources, counters, categories)
        analysis_complete = True
    #heatmaps
    if args.pearsons == True:
        rank(sources, counters, categories, 'pearsons')
        analysis_complete = True
    if args.spearmans == True:
        rank(sources, counters, categories, 'spearmans')
        analysis_complete = True
    #check if anaylsis run
    if analysis_complete == False:
        raise NoAnalysisError('No analysis was requested. Use the paramaters to perform an analysis.')
    else:
        print('Codoniser completed the analysis.')
    

    #in the future ...
        #sliding window <- requires positional info from gbk
        #identify outliers?
        #identify genes with rare codons
        #anything else?

if __name__ == '__main__':
    main()
