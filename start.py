#Import math Libary 
import math

#Formula
def dist(x1, y1, x2, y2):  
    return math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2) 

#Introduction
print("WELCOME TO THE TRIANGLE PERIMETER CALCULATOR")
print("Enter the coordinates of the vertices of a triangle...") 

#Vertex A
print("\nVertex A") 
VAX = int(input("Enter x-coordinate for Vertex A:"))
VAY = int(input("Enter y-coordinate for Vertex A:"))

#Vertex B
print("\nVertex B") 
VBX = int(input("Enter x-coordinate for Vertex B:"))
VBY = int(input("Enter y-coordinate for Vertex B:"))

#Vertex C 
print("\nVertex C") 
VCX = int(input("Enter x-coordinate for Vertex C:"))
VCY = int(input("Enter y-coordinate for Vertex C:"))

#Output 
print("\nSIDE LENGTH AND PERIMETER") 
AB = dist(VAX, VAY, VBX, VBY)
print('AB = ' + str(AB)) 
AC = dist(VAX, VAY, VCX, VCY) 
print('AC = ' + str(AC))
BC = dist(VBX, VBY, VCX, VCY)
print('BC = ' + str(BC)) 
Perimeter = (AB, AC, BC) 
print( 'Perimeter = ' + str(AB + AC + BC))  
 