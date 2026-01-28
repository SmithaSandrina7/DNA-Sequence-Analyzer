touch dna_analyzer.py
def sequence_length(dna):
    """
    Returns the length of a DNA sequence.
    """
    return len(dna)


def gc_content(dna):
    """
    Calculates GC percentage of a DNA sequence.
    """
    gc_count = dna.count('G') + dna.count('C')
    return round((gc_count / len(dna)) * 100, 2)


def nucleotide_composition(dna):
    """
    Returns nucleotide composition of a DNA sequence.
    """
    return {
        'A': dna.count('A'),
        'T': dna.count('T'),
        'G': dna.count('G'),
        'C': dna.count('C')
    }


def has_start_codon(dna):
    """
    Checks for presence of ATG start codon.
    """
    return 'ATG' in dna
