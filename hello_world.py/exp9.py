n = 5 
for i in range(n):
    for j  in range(i):
        print('*',end ="")
    print("")
#nex pattern
def print_alphabet_triangle(rows):
    ascii_value = 65 
    for i in range(rows):
        for j in range(i + 1):
            alphabet = chr(ascii_value)
            print(alphabet, end=" ")
            ascii_value += 1
        print() 

num_rows = 5
print_alphabet_triangle(num_rows)

# next pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print() 
