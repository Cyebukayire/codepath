def find_balanced_subsequence(art_peices):
    """
    U: We want to find the length of the longest "balanced" subsequence.
    I: art_pieces array (int)
    O: length of longest subsequence (int)
    P:
    create dictionary
        for each num in array
            increment the count of that num
    
    max length = 0

    for each num in count dict
        if num+1 is in dictionary
            add x and x+1 count 
            update max length if larger

    return max length 
    """
    if not art_peices:
        return 0
    
    freq  = {}
    for num in art_peices:
        if num not in freq:
            freq[num] = 1 
            
        else:
            freq[num] += 1
            
    # return freq

    max_length = 0

    for num in freq:
        if num - 1 in freq:
            length = freq[num] + freq[num-1]
            if length > max_length:
                max_length = length
               
    return max_length
        # if num +1 in dic
        #new varible to store max length ourside of for looop 

    print(find_balanced_subsequence)
art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))
    
    
   