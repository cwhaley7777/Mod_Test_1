#Main Program File for Module_Test_1
print()
print("Welcome to the module import program!")

import Module_Database

num_1 = Module_Database.a
num_2 = Module_Database.b
num_3 = Module_Database.c
num_4 = Module_Database.d
num_5 = Module_Database.e

print ("We will now access the data from the module!")
print (num_1, "*", num_2, "=", num_1 * num_2)
print (num_3, "*", num_4, "*", num_5, "=", num_3 * num_4 * num_5)
print ("Magic!!")
