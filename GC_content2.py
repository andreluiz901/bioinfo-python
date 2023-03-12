def calculate_gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    gc_content = (gc_count / len(seq)) * 100
    return gc_content

# Open file
filename = 'gc_file'
with open(filename, 'r') as f:
    # Initialize variables
    fastaid = ''
    seq = ''
    max_gc = 0
    max_gc_id = ''

    # Loop over each line in the file
    for line in f:
        line = line.strip() # Remove any whitespace characters
        if line.startswith('>'): # New sequence header
            # If we have a sequence in progress, calculate the GC content and print
            if seq:
                gc = calculate_gc_content(seq)
                print(f"{fastaid}\t{gc:.2f}%")
                # Update max GC if necessary
                if gc > max_gc:
                    max_gc = gc
                    max_gc_id = fastaid
            # Start a new sequence
            fastaid = line[1:] # Remove the '>' character from the header
            seq = ''
        else:
            seq += line

    # Calculate and print the GC content for the last sequence in the file
    gc = calculate_gc_content(seq)
    print(f"{fastaid}\t{gc:.2f}%")
    # Update max GC if necessary
    if gc > max_gc:
        max_gc = gc
        max_gc_id = fastaid

    # Print the sequence ID with the highest GC content
    print(f"\nSequence with the highest GC content:\n{max_gc_id}\t{max_gc:.2f}%")
