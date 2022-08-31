def saisir_row(numero=1):
    print(f'ligne n {numero}')
    row = input('Saisir une ligne de 9 chiffres:')
    return [int(c) for c in row]

def saisir_sudoku():
    sudoku = list()
    for i in range(1,10):
        sudoku.append(saisir_row(i))
    return sudoku
    
def check_row(k):
    for i in range(1,10):
        if i not in k:
            return False
    return len(k)==9
    
def check_rows(sudoku):
    for i in range(9):
        if not check_row(sudoku[i]):
            return False
    return len(sudoku)==9
    
def transpose(sudoku):
    for i in range(9):
        for j in range(i+1,9):
            temp = sudoku[i][j]
            sudoku[i][j] = sudoku[j][i]
            sudoku[j][i] = temp
            
def check_square(sudoku, i0=0, j0=0):
    '''
    0,0 ; 0,3 ; 0,6
    3,0 ; 3,3 ; 3,6
    6,0 ; 6,3 ; 6,6
    '''
    l = list()
    for i in range(i0,i0+3):
        for j in range(j0, j0+3):
            l.append(sudoku[i][j])
    return check_row(l)
    
def check_squares(sudoku):
    pivo = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    for p in pivo:
        if not check_square(sudoku, p[0], p[1]):
            return False
    return True

def check_sudoku(sudoku):
    logic1 = check_rows(sudoku)
    transpose(sudoku)
    logic2 = check_rows(sudoku)
    transpose(sudoku)
    logic3 = check_squares(sudoku)
    return logic1 and logic2 and logic3
    
if __name__ == '__main__':
    sdk = saisir_sudoku()
    cheked = check_sudoku(sdk)
    if cheked:
        print('Votre Sudoku est valide.')
    else:
        print('Votre Sudoku n\'est pas valide!')
    
    

