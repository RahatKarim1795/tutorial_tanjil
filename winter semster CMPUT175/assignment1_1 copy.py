def open_file(file):
    
    f = open(file, "r")
    read_file = f.readlines()
    f.close()

    return read_file

def product_details(product_file):

    product_detail = {}
    
    for lines in product_file[1:]:
        split_file = lines.split(",")
        product_id = split_file[0]
        product_detail[product_id] = {
                         'product_name':split_file[1],
                         'price':split_file[2]
                        }
    
    return product_detail



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

#array position= [0,1,2,3,.......15]
# product id   = [1,2,3,4,5....15]
# sold_product = [5,22,53,......4]

def find_max_sales(updated_sale, product_detail):

    # initialize a list with 15 spaces of 0
    count_sales = [0] * 15

    # store the total of all product number of sales in the list where ('position of array' = 'product id - 1') (total P10 product sold = count_sales[9])

    for transaction_id,details in updated_sale.items():

        prod_id = details['product_id']
        position = int(prod_id[1:])
        count_sales[ position-1 ] += details['quantity']

# count_sales=[234,235,234,1234,]
        
    # from total sales list find out top 3
    max1 = 0
    max2 = 0
    max3 = 0

    pos1 = 0
    pos2 = 0
    pos3 = 0
    position = 1
    

    for i in count_sales:

        if i>max1:
            max3, max2, max1 = max2, max1, i
            pos3, pos2, pos1 = pos2, pos1, position

        elif i>max2:
            max3, max2 = max2, i
            pos3, pos2 = pos2, position

        elif i>max3:
            max3 = i
            pos3 = position

        position+=1

    # print(count_sales)

    # print(f'1st: {max1}\n2nd: {max2}\n3rd: {max3}')
    # print(pos1,pos2,pos3)


    prod1 = product_detail["P" + str(pos1)]["product_name"]
    prod2 = product_detail["P" + str(pos2)]["product_name"]
    prod3 = product_detail["P" + str(pos3)]["product_name"]

    print(f'Max no of sales:\n{prod1} {max1}\n{prod2} {max2}\n{prod3} {max3}')

    return count_sales


# count_sales_dollars = [34.34,122.00,]
    
def max_sales_dollars(updated_sale,product_detail):

    # initialize a list with 15 spaces of 0
    count_sales_dollars = [0] * 15

    # store the total of all product dollar of sales in the list where ('position of array' = 'product id - 1') (total P10 product sold = count_sales_dollars[9])

    for transaction_id,details in updated_sale.items():

        prod_id = details['product_id']
        position = int(prod_id[1:])

        # find price after discount
        normal_price = product_detail[prod_id]['price']
        final_price = float(normal_price) - (float(normal_price) * details['discount'])

        count_sales_dollars[ position-1 ] += final_price

    # from total sales list find out top 3
    max1 = -1
    max2 = -1
    max3 = -1

    pos1 = 0
    pos2 = 0
    pos3 = 0
    position = 1
    

    for i in count_sales_dollars:

        if i>max1:
            max3, max2, max1 = max2, max1, i
            pos3, pos2, pos1 = pos2, pos1, position

        elif i>max2:
            max3, max2 = max2, i
            pos3, pos2 = pos2, position

        elif i>max3:
            max3 = i
            pos3 = position

        position+=1

    # print(count_sales_dollars)


    prod1 = product_detail["P" + str(pos1)]["product_name"]
    prod2 = product_detail["P" + str(pos2)]["product_name"]
    prod3 = product_detail["P" + str(pos3)]["product_name"]

    print(f'\nMax sales in dollars:\n{prod1} {max1}\n{prod2} {max2}\n{prod3} {max3}')

    return count_sales_dollars

def myFunc(e):
  return e['disc']

def find_turnover(updated_sale,product_detail,count_sales,count_sales_dollars):
    
    avg_discount = [0] * 15
    tot_discount = [0] * 15
    discounted_amount = [0] * 15

    for id,details in updated_sale.items():
        prod_id = details['product_id']
        position = int(prod_id[1:])

        # find total discount
        tot_discount[ position-1 ] += details['discount']

        # find discounted amount
        normal_price = float(product_detail[prod_id]['price'])
        discounted_amount[position-1] += normal_price * details['discount']
        # print(normal_price * details['discount'])
        # discounted_amount[position-1] += normal_price - discount1

# count_sales[1]
# count_sales_dollars[1]
# avg_discount[1]
# discounted_amount[1]
# all same product's data

    # find average discount for each product
    position = 0
    for i in tot_discount:
        avg_discount[position] = i / count_sales[position]
        position+=1

# tot_discount = [9.6,4.5,2.5,....9.9]
# av_dicount   = [0.13,0,0,0,0,0,0,]
    # print()

    # print(discounted_amount)
    # print(tot_discount)
    # print(avg_discount)
        
    print()
    
    # position = 0        
    # for id,details in product_detail.items():
    #     print(f'{id} | {details['product_name']} | {count_sales[position]} | $ {count_sales_dollars[position]} | {avg_discount[position]}% | $ {discounted_amount[position]}')
    #     position+=1


    data = []
    for i in range(1,16):
        data.append({'id': str("P" + str(i)), 'disc' : discounted_amount[i-1]})

    data.sort(key = myFunc)
    # print(data)

    print(f'+---+---------------------+---+---------+-----+-----------+')

    for i in data:
        prod_id = i['id']
        disc = i['disc']
        position = int(prod_id[1:])

        prod_name = product_detail[prod_id]['product_name']
        max_sales = count_sales[position-1]
        max_sales_dollars = count_sales_dollars[position-1]

        print(f'|{prod_id:3}|{prod_name:20}|{max_sales}|$ {max_sales_dollars} | {avg_discount[position-1]}%| {disc}')

    print(f'+---+--------------------+----+---------+-----+-----------+')


# list.sort(reverse=True)
    
from datetime import datetime #needed to calculate weekday name from a date

def transaction_weekday(total_sale):

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    weekday_count = [0] * 7
    #weekday_count = [0,2,3,1,2,0,0]

    for id,details in total_sale.items():
        date_string = details['date']

        date_object = datetime.strptime(date_string, "%Y-%m-%d")

        position = date_object.weekday()

        # weekday_count[position] += details['quantity']
        weekday_count[position] += 1
        
    print("------------------------\nWeekday stats:\n------------------------")

    for i in range(7):
        print(f'{weekdays[i]} : {weekday_count[i]}')


def count_returned(return_file,product_detail,total_sale):
    
    count_return = [0] * 15

    for line in return_file[1:]:
        split_file = line.split(",")
        tr_id = split_file[0]

        prod_id = total_sale[tr_id]['product_id']
        quantity = total_sale[tr_id]['quantity']

        position = int(prod_id[1:])
        count_return[position-1] += quantity

    print("------------------------\nReturned Products:\n------------------------")

    # print(count_return)
    
    for i in range(15):
        prod_id = "P" + str(i + 1)
        prod_name = product_detail[prod_id]['product_name']

        print(f'{prod_id} | {prod_name} : {count_return[i]}')

# count_return = [1,2,1,,,,,,1]

def calculate_performance(count_sales):

    file = open("transactions_units.txt", "w", encoding = "utf-8")
    file.write("transaction_id,sales_count\n")

    for i in range(len(count_sales)):
        prod_id = "P" + str(i+1)
        
        file.write(prod_id + "," + str(count_sales[i]) + "\n")

def main():

    transaction_file = open_file("transactions_Sales.csv")
    return_file = open_file("transactions_Returns.csv")
    product_file = open_file("transactions_Products.csv")

    total_sale = total_sales(transaction_file)
    updated_sale = update_sales(total_sale, return_file)

    # print(updated_sale)

    product_detail = product_details(product_file)

    # print(product_detail)

    count_sales = find_max_sales(updated_sale,product_detail)

    count_sales_dollars = max_sales_dollars(updated_sale,product_detail)

    find_turnover(updated_sale,product_detail,count_sales,count_sales_dollars)

    transaction_weekday(total_sale)

    
    # count_returned(return_file,product_detail,total_sale)

    # calculate_performance(count_sales)

    # print(updated_sale)
    
main()