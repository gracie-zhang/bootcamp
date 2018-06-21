import bootcamp_utils

def is_valid(seq):
    """Check for valid seq"""
   
    for aa in seq:
        if aa not in bootcamp_utils.aa.keys():
            raise RuntimeError(aa + ' is not a valid aa you fuckface')

def prep_seq(seq):
    """Prepare sequence for counting"""
    
    return seq.upper()
            
def number_negatives(seq):
    """Return number of neg res in protein seq"""
    
    seq = prep_seq(seq)
    is_valid(seq)
        
    return seq.count('E') + seq.count('D')

def number_positives(seq):
    """Return number of pos res in protein seq"""
    
    seq = prep_seq(seq)
    is_valid(seq)
    
    return seq.count('R') + seq.count('K') + seq.count('H')