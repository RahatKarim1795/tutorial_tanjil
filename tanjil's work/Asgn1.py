def open_file(file):
    
    f = open(file, "r")
    read_file = f.readlines()
    f.close()

    return read_file



def total_sales(transaction_file):
    
    # Make a dictionary which stores the 'transaction_id', 'date', 'product_id', 'quantity', 'discount'
    
    product_sales = {}
    
    for lines in transaction_file[1:]:
        split_file = lines.split(",")
        transaction_id = split_file[0]
        product_sales[transaction_id] = {
                         'date':split_file[1],
                         'product_id':split_file[2],
                         'quantity':int(split_file[3]),
                         'discount':float(split_file[4])
                         }
    
    return product_sales



def update_sales(sales, return_file):

    returns = {}

    for line in return_file[1:]:
        split_line = line.strip().split(",")
        transaction_id = split_line[0]
        returns[transaction_id] = True 
    
    updated_sales = {}

    for transaction_id, transaction_details in sales.items():
        if transaction_id not in returns:
            updated_sales[transaction_id] = transaction_details

    return updated_sales

#array position=  0,1,2,3,
# product id   = [1,2,3,4,5....15]
# sold_product = [5,22,53,......4]

def find_max_sales(updated_sale):

    count_sales = [0] * 15

    for transaction_id,details in updated_sale.items():

        for key,value in details.items():

            if key == 'product_id':
                prod_id = value
                position = int(prod_id[1:])

            if key == 'quantity':
                count_sales[ position-1 ] += value

    max1,max2,max3 = -1
    # max2 = -1
    # max3 = -1

    for i in count_sales:

        if i>max1:
            max3, max2, max1 = max2, max1, i

        elif i>max2:
            max3, max2 = max2, i

        elif i>max3:
            max3 = i

    print(f'1st: {max1}\n2nd: {max2}\n3rd: {max3}')

# max1 = 30
# max2 = 29
# max3 = 28

# [27,29,1,1,1,1,1,1,11111]
    
def main():

    transaction_file = open_file("transactions_Sales.csv")
    return_file = open_file("transactions_Returns.csv")
    product_file = open_file("transactions_Products.csv")

    total_sale = total_sales(transaction_file)
    updated_sale = update_sales(total_sale, return_file)

    find_max_sales(updated_sale)
    # print(updated_sale)
    
main()
    
# a = "p10"
# print(a[1:])