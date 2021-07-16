# Matrix Multiplication in python without numpy
#matrix multiplication of 3 by 3 Matrix without numpy

A = [[10,20,10],[4,5,6],[2,3,5]]
B = [[3,2,4],[3,3,9],[4,4,2]]

matrix = []


def multiplication(nxt,col):
    try:
        sizenxt = len(nxt)
        sizecol= len(col)
        if (sizenxt != sizecol):
            raise ValueError("Exception")
        res = sum([nxt[k]*col[k] for k in range(sizenxt)])
        return res
    except ValueError:
        print("Should Have the same len row&col")

def getcol(matrix,numcol):
    size = len(matrix)
    col = [matrix[k][numcol] for k in range(size)]
    return col

def getnxt(matrix,numnxt):
    nxt = matrix[numnxt]
    return nxt

for k in range(len(A)):
    matrix.append([])
    for m in range(len(B)):
        matrix[k].append(multiplication(getnxt(A,k),getcol(B,m)))

print(matrix)


    
    



     
    
