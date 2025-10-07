#Practical 1 : 
# Algebra of complex numbers
print("Menu :")
x1 = int(input("Enter x1 : "))
y1 = int(input("Enter y1 : "))
z1 = complex(x1,y1)

x2 = int(input("Enter x2 : "))
y2 = int(input("Enter y2 : "))
z2 = complex(x2,y2)

while True:
    print("\n1.Addition \n2.Sub \n3.Multiplication \n4.Multiplication of conjugate \n5.Division \n6.Exit")
    op = input("\nEnter your choice :")
    if op=='1':
        print('Additon :',z1+z2)     

    elif op=='2':
        print('Subtraction  :',z1-z2)

    elif op=='3':
        print('Multiplication : ',z1*z2)

    elif op=='4':
        c1 = z1.conjugate()
        c2 = z2.conjugate()
        print('Multiplication of conjugate :',(z1*c1).real)
        print('Multiplication of conjugate :',(z2*c2).real)

    elif op=='5':
        print('Division :',z1/z2)

    elif op=='6':
        print('exit..')
        break

    else :
        print("Enter Correct choice :")
        #####################
        prac 2
        
import matplotlib.pyplot as plt
import numpy as np

def plot_vectors(z1, z2, label):
    # plt.figure()
    plt.plot([0, z1.real], [0, z1.imag], 'bx-', label='Original')
    plt.plot([0, z2.real], [0, z2.imag], 'ro--', label=label)
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.grid(True)
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.title(label)
    plt.legend()
    plt.axis('equal')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.show()

def rotate(z, angle_deg):
    return z * np.exp(1j * np.deg2rad(angle_deg))

def scale(z, factor):
    return z * factor

# Input
x = int(input("Enter real part: "))
y = int(input("Enter imaginary part: "))
z = complex(x, y)
print(f"Original complex number: {z}")

# Menu Loop
while True:
    print("\nMain Menu:\n1. Rotate (90°, 180°, 270°)\n2. Scale (×0.5, ×1, ×1.5)\n3. Exit")
    choice = input("Choose (1-3): ")

    if choice == '1':
        print("\nRotation Options:\n1. 90°\n2. 180°\n3. 270°")
        r_choice = input("Choose rotation (1-3): ")
        angles = {'1': 90, '2': 180, '3': 270}
        if r_choice in angles:
            angle = angles[r_choice]
            z_rot = rotate(z, angle)
            plot_vectors(z, z_rot, f"Rotated by {angle}°")
        else:
            print("Invalid rotation choice.")

    elif choice == '2':
        print("\nScaling Options:\n1. ×0.5\n2. ×1\n3. ×1.5 \n4. x2")
        s_choice = input("Choose scaling (1-4): ")
        factors = {'1': 0.5, '2': 1, '3': 1.5,'4':2}
        if s_choice in factors:
            factor = factors[s_choice]
            z_scl = scale(z, factor)
            plot_vectors(z, z_scl, f"Scaled ×{factor}")
        else:
            print("Invalid scaling choice.")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
##############
prac 3

import numpy as np 

def scalar_combination(v1,v2,a,b):
    au=a*v1
    bv=b*v2
    return (au+bv)

dimension=int(input("Enter the dimension : "))
v1=np.array([int(input(f"Enter value for v1[{i+1}]:"))for i in range(dimension)])
v2=np.array([int(input(f"Enter value for v2{i+1}]:"))for i in range(dimension)])

while True:
    print("Choose option : \n1.dot product \n2.scalar combination \n3.exit")
    option=int(input("Enter option : "))
    if option==1:
        print(np.dot(v1,v2))
    elif option==2 :
        a=int(input("Enter scalar value for v1"))
        b=int(input("Enter scalar value for v1"))
        print(scalar_combination(v1,v2,a,b))
    elif option==3:
        print( " exiting ") 
        break
    else: 
        print("invalid option ")

    #######
        prac 5
import numpy as np 
from scipy.linalg import eig

rows=int(input("Enter number of rows:"))
print("Enter matrix elements row by row seperated by space")

matrix=[]
for i in range(rows):
    row=list(map(int,input(f"Rows {i+1}:").split()))
    matrix.append(row)

A=np.array(matrix)
print(A)
eigenvalue,eigenvector=eig(A)
print(eigenvalue)
print(eigenvector)
#####
prac 6

import numpy as np
import sympy as sp

# Take matrix size input
rows = int(input("Enter number of rows: "))
print("Enter the matrix elements row by row (space separated):")
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split(',')))
    matrix.append(row)

# Convert to Sympy Matrix
A = sp.Matrix(matrix)

# LU decomposition
_, U, _ = A.LUdecomposition()

print("\nOriginal Matrix A:")
sp.pprint(A)

print("\nRow Echelon Form (U Matrix):")
sp.pprint(U)
print("\nRank of Matrix A:", int(A.rank()))


####
prac 7
import numpy as np

# Function to create vectors
def create_vector(dimension):
    vector = []
    for i in range(dimension):
        element = float(input("Enter the element of the vector: "))
        vector.append(element)
    return vector

# Input for vector dimension
dimension = int(input("Enter the vector dimension: "))

print("First vector:")
u = np.array(create_vector(dimension))
print(u)

print("Second vector:")
v = np.array(create_vector(dimension))
print(v)

# Menu-driven program
while True:
    print("\n1. Dot Product")
    print("2. Projection of (u on v)")
    print("3. Projection of (v on u)")
    print("4. Exit")

    option = int(input("Enter your option: "))

    if option == 1:
        dot_product = np.dot(u, v)
        print("Dot Product =", dot_product)

    elif option == 2:
        norm_v = np.linalg.norm(v)
        proj_u_on_v = (np.dot(u, v) / (norm_v ** 2)) * v
        print("Projection of u on v =", proj_u_on_v)

    elif option == 3:
        norm_u = np.linalg.norm(u)
        proj_v_on_u = (np.dot(u, v) / (norm_u ** 2)) * u
        print("Projection of v on u =", proj_v_on_u)

    elif option == 4:
        print("Exit!!")
        break

    else:
        print("Invalid option")
