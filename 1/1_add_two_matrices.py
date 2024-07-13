def matrix(m,n):
    output=[]
    for i in range(m):
        row=[]
        for j in range(n):
            inp=int(input(f"Enter output[{i}][{j}]: "))
            row.append(inp)
        output.append(row)
    return output

def sum(A,B):
    if len(A)!=len(B) or len(A[0])!=len(B[0]):
        print("Matrix addition is not possible")
    else:
        o=[]
        for i in range(len(A)):
            r=[]
            for j in range(len(A[0])):
                r.append(A[i][j]+B[i][j])
            o.append(r)
        return o

print("Enter the matrix: ")
m = int(input("Enter the row number: "))
n = int(input("Enter the column number: "))

print("The matrix A is: ")
A=matrix(m,n)
print(A)

print("The matrix B is: ")
B = matrix(m,n)
print(B)

print("The sum of the matrix is: ")
Sum=sum(A,B)
print(Sum)
