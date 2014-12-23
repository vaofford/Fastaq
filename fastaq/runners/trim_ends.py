import argparse
from fastaq import tasks

def run(description):
    parser = argparse.ArgumentParser(
        description = description,
        usage = 'fastaq trim_ends <fasta/q in> <bases off start> <bases off end> <fasta/q out>')
    parser.add_argument('infile', help='Name of input fasta/q file')
    parser.add_argument('start_trim', type=int, help='Number of bases to trim off start')
    parser.add_argument('end_trim', type=int, help='Number of bases to trim off end')
    parser.add_argument('outfile', help='Name of output fasta/q file')
    options = parser.parse_args()
    tasks.trim(options.infile, options.outfile, options.start_trim, options.end_trim)
