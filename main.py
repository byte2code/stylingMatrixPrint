def print_matrix(matrix):
    
    print('-\t' + '\t'*(len(matrix)-1) + '\t-')
    ll = max([len(str(x)) for y in matrix for x in y])
    for i in matrix:
        print('|\t', end='')
        for j in i:
            print(' '*(ll-len(str(j)))+str(j), end='\t')
        print('|')
    print('-\t' + '\t'*(len(matrix)-1) + '\t-')