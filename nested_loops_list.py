def nested_list():
    list = [ ['a','b','c'] , ['x','y','z'] ]

    list1 = [1,2,3]

    for inner_list in list:

        for i in inner_list:
            print(i, end="")

        print("\n")

def star_triangle():
    # for i in range(4):
    #     print("*")

    for i in range(5):

        for j in range(i):
            print("*", end="")
            
        print()

# range(4)
# range(start,stop,step)
# for i in range(0,4,1) == range(4)
        
def star_triangle2():

    # for i in reversed(range(5)):
    #     print("*" * i , end="")

    for i in reversed(range(5)):
        print()
        for j in range(i):
            print("*", end="")

        # print()

# star_triangle()
# star_triangle2()




## practice 1
# Enter the following matrix into a single list:
# [[1,2,3],[4,5,6],[7,8,9]]

def practice_1():
    nested = [[1,2,3],[4,5,6],[7,8,9]]

    flat_list = []

    for i in nested:
        for j in i:
            flat_list.append(j)

    # for i in nested:
    #     for j in i:
    #         print(j, end=" ")
    #     print()



## practice 2
# For the previous list, show all values to the user in a single line without using another list

def practice_2():
    nested = [[1,2,3],[4,5,6],[7,8,9]]

    for inner_list in nested:
        for element in inner_list:
            print(element)


## practice 3

def practice_3():
    planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 
  
    flatten_planets = [] 
    
    for sublist in planets: 
        for planet in sublist: 
            
            if len(planet) < 6: 
                flatten_planets.append(planet) 
            
    print(flatten_planets)


## practice 4
def practice_4():
    matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] 
    
    # Nested List Comprehension to flatten a given 2-D matrix 
    flatten_matrix = [val for sublist in matrix for val in sublist]
    
    print(flatten_matrix)

## practice 5
# show the output as a single, flattened list
# nested_list = [[1,2,3],[4,[5,6]],[7,8,9],[9,1,2]]

def practice_5():
    nested_list = [[1, 2, 3], [4, [5, 6]], [7, 8, 9], [9, 1, 2]]

    flat_list = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            flat_list.extend(practice_5(sublist))
        else:
            flat_list.append(sublist)

    return flat_list

## make a matrix of 2x2 with values from 1 to 4
def practice_6():
    inner = []
    nested = [inner]
    row = 2
    column = 2

    num = 1
    # nested[0][0] = 1
    # nested[0][1] = 2
    # nested[1][0] = 3
    # nested[1][1] = 4
    # print(nested)

    for i in range(row):
        for j in range(column):
            nested.append(num)
            num+=1

    print(nested)





# practice_1()
# practice_2()
# practice_3()
# practice_4()
practice_6()

### new functionalities

## list.extend()
# extends a list to allow for more storage
original_list = [1, 2, 3]
new_elements = [4, 5, 6]

original_list.extend(new_elements)

original_list = [1, 2, 3, 4, 5, 6]


## variable.isinstance(object, type)

# used to check if an object is an instance of 
# a specific type or class. It can check for a 
# wide range of types, including built-in types, 
# user-defined classes, and more

x = 1
check = isinstance(x, int)
check = True


# def flatten_list(nested_list):
#     flat_list = []
#     stack = [nested_list]

#     while stack:
#         current = stack.pop()
#         for item in current:
#             if isinstance(item, list):
#                 stack.append(item)
#             else:
#                 flat_list.append(item)

#     return flat_list

# nested_list = [[1, 2, 3], [4, [5, 6]], [7, 8, 9], [9, 1, 2]]
# result = flatten_list(nested_list)
# print(result)