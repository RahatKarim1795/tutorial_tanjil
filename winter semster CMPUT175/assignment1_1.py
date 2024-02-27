import csv

# def count_sales(sales,product):
#     count = 0

#     for i in sales:
#         product_id = "P" + product
#         if i[2] == product_id:
#             count += 1

#     return count
    

# def noOfSales(filename):
#     file = open(filename)
#     sales = csv.reader(file)
#     product = 1
#     max = 0

#     for i in range(1,16):
#         current = count_sales(sales,product)
#         if current > max:
#             max = current
            
#         product+=1


def noOfSales():

    count_sales = [0] * 15

    file = open("transactions_Sales.csv")
    sales = csv.reader(file)

    file1 = open("transactions_Returns.csv")
    returns = csv.reader(file1)
    
    for i in sales:
        product_id = i[2]
        quantity_sold = i[3]
        prod_id = ""

        for char in product_id:
            if char.isdigit():
                prod_id+=char
               
        if prod_id and prod_id.isdigit():
            count_sales[int(prod_id)-1] += int(quantity_sold)

    for each_return in returns:
        trans_id = each_return[0]

        for each_transaction in sales:
            if each_transaction[0] == trans_id:

                product_id = each_transaction[2]

                for char in product_id:
                    if char.isdigit():
                        prod_id2+=char

                quantity_returned = each_transaction[3]
                
                count_sales[int(prod_id2)-1] -= int(quantity_returned)
    
    max1 = 12
    max2 = 15
    max3 = 8
    position = 1
# count_sales = [10,13,5,50.....12]

    for i in count_sales:

        if i>max1:
            max3, max2, max1 = max2, max1, i
        elif i>max2:
            max3, max2 = max2,i
        elif i>max3:
            max3 = i

        position+=1

    print(f'1st: {max1}\n2nd: {max2}\n3rd: {max3}')

     

# total products = 4
#             #p1 p2 p3 p4 
# no of sales = [1,4,3,2]


def main():
    noOfSales()


if __name__ == "__main__":
    main()