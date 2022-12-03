def calculateSkips(first_arrays):
    x = {}
    for i in range(len(first_arrays)-1, -1, -1):
        x[first_arrays[i]] = i
    return x


def count(pattern, wavelet_tree, first_arrays, bwt_arrays):
    skips = calculateSkips(first_arrays)
    top = 0
    bot = len(bwt_arrays)
    i = len(pattern) - 1
    #print(first_arrays, skips)
    while((i >= 0) and (bot > top)):
        c = pattern[i]
        # top = bwt.c[c]+ Bwt.rank[top]
        top = skips[c] + wavelet_tree.rank_query(c, top)
        # bot = bwt.c[c]+ Bwt.rank[bot]
        bot = skips[c] + wavelet_tree.rank_query(c, bot)
        i -= 1
    return bot-top
