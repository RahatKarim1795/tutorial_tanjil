flower = {
    'daffodil' : 0.35,
    'tulip' : 0.33,
    'hyacinth' : 0.75
}

mary_order = {
    'daffodil' : 50,
    'tulip' : 100,
    'hyacinth' : 30
}

x = flower['tulip']
x = round(x + (x*0.25), 2)
flower['tulip'] = x

# print(flower['daffodil'])

# print(flower.get('daffodil'))


def add():
    x = input("flower: ")
    y = float(input("price: "))

    flower.update({x:y})

    print(flower)

# add()
# a = [656,434,64]

# a[0]
# flower['daffodil']
    
# x = flower.get('tulip')
# flower['tulip'] = round(x + (x*0.25), 2)

# # print(flower)

# code = 'DAF'
# p = 2.5
# n = 2
# n = round(p,2)

# print(f'{code:4} * {n:3} = $ {p:5}')

#q5
def order(order_name):

    tot_cost = 0
    tot_num = 0

    for name,num in order_name.items():

        code = (name[0] + name[1] + name[2]).upper()
        # code = code.upper()
        cost = flower[name]
        subtot = cost * num

        tot_cost += subtot
        tot_num += num

        print(f'{code:4} * {num:3} = $ {subtot:5.2f}')

    return tot_cost,tot_num

mary_order = dict(sorted(mary_order.items()))
# order(mary_order)


#q6
# print("\nYou have purchased the following bulbs: ")
# tot_cost, tot_num = order(mary_order)
# print(f'\nThank you for purchasing {tot_num} bulbs from Bluebell Greenhouses. Your total comes to $ {tot_cost:5.2f}.')



#################
##############
# exercise 2
# def sort_file(filename):
#     sorted = {
#         "[50-60mm)" : {},
#         "[60-70mm)" : {},
#         "[70-80mm)" : {},
#         "[80-90)" : {},

#     }
#     with filename open:

#2b