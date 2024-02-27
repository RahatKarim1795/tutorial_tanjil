# def nested_list():
#     list = [ ['a','b','c'] , ['x','y','z'] ]

#     list1 = [1,2,3]

#     for inner_list in list:

#         for i in inner_list:
#             print(i, end="")

#         print("\n")

# def star_triangle():
#     # for i in range(4):
#     #     print("*")

#     for i in range(5):

#         for j in range(i):
#             print("*", end="")
            
#         print()

# # range(4)
# # range(start,stop,step)
# # for i in range(0,4,1) == range(4)
        
# def star_triangle2():

#     # for i in reversed(range(5)):
#     #     print("*" * i , end="")

#     for i in reversed(range(5)):
#         print()
#         for j in range(i):
#             print("*", end="")

        # print()

# star_triangle()
# star_triangle2()




## practice 1
# Enter the following matrix into a single list:
# [[1,2,3],[4,5,6],[7,8,9]]

def practice_1():
    nested = [[1,2,3],[4,5,6],[7,8,9]]

    # for i in nested:
    #     for j in range(i):
    #         print(nested[i][j])
    print(nested[0][0])






## practice 2
# For the previous list, show all values to the user as a single flattened list/matrix

def practice_2():
    pass



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

practice_1()
# practice_2()
# practice_3()
# practice_4()