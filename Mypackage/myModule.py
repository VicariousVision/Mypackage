def top_n(items,n):
    """
    Return top n items in an array in descending order
    
    """

    for i in range(n):
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]


    top_n = items[-n:]

    return top_n[::-1]