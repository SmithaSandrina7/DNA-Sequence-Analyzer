touch sample_sequences.py
from dna_analyzer import (
    sequence_length,
    gc_content,
    nucleotide_composition,
    has_start_codon
)

dna_sequences = [
    "ATGCGTAC",
    "GGCCGGCC",
    "ATATATAT"
]

for i, dna in enumerate(dna_sequences):
    print(f"\nSequence {i+1}")
    print("DNA:", dna)
    print("Length:", sequence_length(dna))
    print("GC %:", gc_content(dna))
    print("Nucleotide composition:", nucleotide_composition(dna))
    print("Start codon present:", has_start_codon(dna))
