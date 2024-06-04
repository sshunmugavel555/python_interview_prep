def recur_rem_adj_dup(word):
    """ Recursively remove adjacent duplicates in a word 
    eg abccbccba -> empty string 
    ab(cc)b(cc)ba->abbba->a(bbb)a->aa->(aa)->""(empty string) """

    
    for x in range(len(word)):
        for y in range(x+1,len(word)):
            if fin[x]==fin[y]:
                fin=[]
                tmp=''

                for ch in word:
                    if ch != tmp:
                        tmp=ch
                        fin.append(tmp)
                    elif fin[-1]==ch:
                        fin.pop()
                
                
                   
    

    if fin: 
        
                    recur_rem_adj_dup(''.join(fin))
                else:
                    break
        #print(''.join(fin))
    #else:
        #print(''.join(fin))
    print(''.join(fin))



recur_rem_adj_dup('abccbccba')