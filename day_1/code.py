import os

with open('day_1/input.txt','r') as f_in:
    data = f_in.read()
    
lines = data.split('\n')[:-1]

count_sum = 0

for line in lines:
    n = len(line)
    i_found = False
    j_found = False
    i = 0
    j = n - 1
    while not (i_found and j_found):
        if line[i].isnumeric():
            count_sum += 10*int(line[i])
            i_found = True
        elif not i_found:
            i += 1
        else:
             pass
        
        if line[j].isnumeric():
            count_sum += int(line[j])
            j_found = True
        elif not j_found:
                j -= 1
        else:
             pass
    print(f"line = {line}, number = {line[i]}{line[j]}, current sum = {count_sum}")

print(f"count_sum = {count_sum}")

    