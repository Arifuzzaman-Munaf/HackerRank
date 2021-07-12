def minion_game(string):
    # your code goes here
    v = ['A','E' , 'I' ,'O', 'U']
    size =  len(string)
    kevin = sum(size-i for i in range(size) if string[i] in v)
    stuart = size*(size + 1)/2 - kevin
    if kevin == stuart:
        print ('Draw')
    elif kevin > stuart:
        print ('Kevin %d' % kevin)
    else:
        print ('Stuart %d' % stuart)
if __name__ == '__main__':
    s = "MUNAFUAM"
    minion_game(s)