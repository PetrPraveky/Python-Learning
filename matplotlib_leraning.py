# a= [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]
# for n, i in enumerate(a):
#   if i == 1:
#      a[n] = 10

# print(a)

import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import cycle

def BC_start(number_list):
    if '(' in number_list:
        y = BC_brackets(number_list)
    else:
        y = BC_calculation(number_list)
        y = y[0]
    return y

def BC_brackets(number_list):
    if "(" in number_list:
        for n in cycle(range(0, 1)):
            global l_bracket_index, r_bracket_index
            l_bracket_index, r_bracket_index = 0, 0
            l_bracket = list_duplicates_of(number_list, '(')
            r_bracket = list_duplicates_of(number_list, ')')
            
            def brackets_index():
                l_bracket_index = l_bracket.index(max(l_bracket))
                r_bracket_index = r_bracket.index(min(r_bracket))
                for n in cycle(range(0, 1)):
                    if int(l_bracket[l_bracket_index]) > int(r_bracket[r_bracket_index]):
                        r_bracket_index += 1
                        continue
                    else:
                        break
                return l_bracket_index, r_bracket_index
            
            l_bracket_index, r_bracket_index = brackets_index()

            index = int(l_bracket[l_bracket_index])+1
            brackets_num = []
            for n in cycle(range(0, 1)):
                if index == r_bracket[r_bracket_index]:
                    break
                else:
                    brackets_num.append(number_list[index])
                    index += 1
            
            if len(brackets_num) == 1:
                number_list[l_bracket[l_bracket_index]] = float(brackets_num[0])
                remove_index = l_bracket[l_bracket_index]+1
                for n in cycle(range(0, 1)):
                    if remove_index > r_bracket[r_bracket_index]:
                        break
                    else:
                        number_list.pop(l_bracket[l_bracket_index]+1)
                        remove_index += 1
                        continue
            else:
                for n in range(brackets_num.count('+')+brackets_num.count('-')+brackets_num.count('*')+brackets_num.count('/')+brackets_num.count('^')):
                    y = BC_calculation(brackets_num)
                    brackets_num = y
                number_list[l_bracket[l_bracket_index]] = y[0]
                remove_index = l_bracket[l_bracket_index]+1
                for n in cycle(range(0, 1)):
                    if remove_index > r_bracket[r_bracket_index]:
                        break
                    else:
                        number_list.pop(l_bracket[l_bracket_index]+1)
                        remove_index += 1
                        continue
                
            if "(" not in number_list:
                break
            else:
                continue

    if len(number_list) != 1:
        for n in cycle(range(0,1)):
            y = BC_calculation(number_list)
            number_list = y
            if len(number_list) == 1:
                break
            else:
                continue
        
    return number_list[0]

def BC_calculation(number_list):
    for n in cycle(range(0,1)):
        try:
            #Mocnina
            if '^' in number_list:
                number_list = BC_exponent(number_list)
            #Dělení x násobení
            elif "/" in number_list or "*" in number_list:
                try:
                    div_var =  number_list.index('/')
                    mul_var = number_list.index('*')
                    if div_var < mul_var:
                        number_list = BC_div(number_list)
                        continue 
                    elif div_var > mul_var:
                        number_list = BC_mul(number_list)
                        continue
                except:
                    if "/" in number_list:
                        number_list = BC_div(number_list)
                        continue 
                    elif "*" in number_list:
                        number_list = BC_mul(number_list)
                        continue
            #Sčítání x odčítání
            elif "+" in number_list or "-" in number_list:
                if '-' in number_list:
                    number_list = BC_sub(number_list)
                    continue  
                else:
                    pass
                if '+' in number_list:
                    number_list = BC_add(number_list)
                    continue  
                else:
                    pass
            if len(number_list) == 1:
                break
            else:
                continue
        except Exception as err:
            print(err)
            break
        
    return number_list
        
def BC_exponent(number_list):
    equal = []
    x = number_list.index("^")
    
    equal.append(str(math.pow(float(number_list[x-1]), float(number_list[x+1]))))
    y = number_list[:(x-1)] + equal + number_list[(x+2):]
    
    return y

def BC_mul(number_list):
    equal = []
    x = number_list.index("*")
    
    equal.append(str(float(number_list[x-1])*float(number_list[x+1])))
    y = number_list[:(x-1)] + equal + number_list[(x+2):]
    
    return y

def BC_div(number_list):
    equal = []
    x = number_list.index("/")
    
    equal.append(str(float(number_list[x-1])/float(number_list[x+1])))
    y = number_list[:(x-1)] + equal + number_list[(x+2):]
    
    return y

def BC_add(number_list):
    equal = []
    x = number_list.index("+")
    
    equal.append(str(float(number_list[x-1])+float(number_list[x+1])))
    y = number_list[:(x-1)] + equal + number_list[(x+2):]
    
    return y

def BC_sub(number_list):
    equal = []
    x = number_list.index("-")
    
    equal.append(str(float(number_list[x-1])-float(number_list[x+1])))
    y = number_list[:(x-1)] + equal + number_list[(x+2):]
    
    return y

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

num_list = ['(', '1', '/', '4', ')', '^', '(', 'x', '+', '3', ')', '+', '1']
equal_list = []
x = np.linspace(-5, 5, 10000)

def graph_draw(x):
    f = 0
    for n in cycle(range(0,1)):
        num_list_1 = num_list.copy()
        for n, i in enumerate(num_list_1):
            if i == "x":
                num_list_1[n] = x[f]
        y = BC_start(num_list_1)
        f += 1
        equal_list.append(float(y))
        if f == len(x):
            break
        else:
            continue
    print(x)
    print(equal_list)
    return equal_list

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.xlim(-np.pi,np.pi)

plt.plot(x, graph_draw(x))
plt.show()