def gc_blocks(seq, block_size):
    """Divides a sequence into blocks and computes the GC content for each block, returning a tuple."""
    
    for i, _ in enumerate(seq):
        block = ''
        gc_count = 0
        for base in seq[i:len(seq)]:
            if base in 'GgCc':
                gc_count += 1
            block += seq[i:i+4]
            i += 4
            gc_content = gc_count / len(block)
            
    return block, gc_content