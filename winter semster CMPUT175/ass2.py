from datetime import datetime

import matplotlib.pyplot as plt

import numpy as np

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


def returns(return_file):
    return_details = {}
    
    for lines in return_file[1:]:
        split_file = lines.split(",")
        transaction_id = split_file[0]
        return_details[transaction_id] = {
                         'date':split_file[1]
                         }
    
    return return_details


def update_sales(total_sales, return_file):

    returns = {}

    for line in return_file[1:]:
        split_line = line.strip().split(",")
        transaction_id = split_line[0]
        returns[transaction_id] = True 
    
    updated_sales = {}

    for transaction_id, transaction_details in total_sales.items():
        if transaction_id not in returns:
            updated_sales[transaction_id] = transaction_details


    return updated_sales
    

def q1(total_sale, product_detail):
    compare_date = datetime.strptime("1/8/2024", "%m/%d/%Y")
    
    all_time_total_before = 0
    all_time_total_after = 0
    tot_transaction_before = 0
    tot_transaction_after = 0
    
    avg_prod_discount_before = [0] * 20
    tot_prod_discount_before = [0] * 20
    
    avg_prod_discount_after = [0] * 20
    tot_prod_discount_after = [0] * 20
    
    product_count_before = [0] * 20
    product_count_before1 = [0] * 20
    product_count_after = [0] * 20
    
    for id, details in total_sale.items():
        
        date_string = details['date']
        transaction_date = datetime.strptime(date_string, "%Y-%m-%d")
        
        prod_id = details['product_id']
        position = int(prod_id[1:])
        
        if transaction_date < compare_date:
            all_time_total_before+=1
            if details['discount'] == 0:
                tot_transaction_before += 1
            else:
                tot_prod_discount_before[position-1] += float(details['discount'])
            product_count_before[position-1] += 1
        else:
            all_time_total_after+=1
            if details['discount'] == 0:
                tot_transaction_after += 1
            else:
                tot_prod_discount_after[position-1] += float(details['discount'])
            product_count_after[position-1] += 1

    for i in range(0,20):
        if product_count_before[i] > 0:
            avg_prod_discount_before[i] = (tot_prod_discount_before[i] / product_count_before[i]) * 100
        if product_count_after[i] > 0:
            avg_prod_discount_after[i] = (tot_prod_discount_after[i] / product_count_after[i]) * 100
    
    without_discount_before = (tot_transaction_before/all_time_total_before) * 100
    without_discount_after = (tot_transaction_after/all_time_total_after) * 100
    
    print(f'{"":<37}<08-01 - >=08-01')
    print(f'Average transaction without discount: {without_discount_before:.2f} - {without_discount_after:.2f}')
    
    print("Average discount per product:\n")
    print(f'PID{"":<11}Product Name <08-01 - >=08-01')
    
    for id,details in product_detail.items():
        position = int(id[1:])
        product_name = details['product_name']
        
        print(f'{id:<3} | {product_name:<20} | {avg_prod_discount_before[position-1]:05.2f} | {avg_prod_discount_after[position-1]:05.2f}')



def weekly_business(total_sale,product_detail):
    weekly_sale_number = [0] * 7
    weekly_sale_amount = [0] * 7
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# weekly_sale_number = [257,244,326,456,457,456,293]
    january_days = []
    for day in range(2,32):
        print("sd")
        print(january_days.append(datetime(2024, 1, day).weekday()))


    # weekdays_count = []
    # for i in range(0,6):
    #     weekdays_count[i] = january_days.count(i)
    
    for id,details in total_sale.items():
        transaction_date = datetime.strptime(details['date'], "%Y-%m-%d")
        day = transaction_date.weekday()

        prod_id = details['product_id']

        original_price = float(product_detail[prod_id]['price'])
        discounted_price = float((original_price * int(details['quantity'])) - (original_price * int(details['quantity']) *  float(details['discount'])))

        weekly_sale_number[day] += 1
        weekly_sale_amount[day] += discounted_price

    print("+----------+-----+---------+")
    print(f'|{"Day":<9} |NB Tr|{"Turnover":>10}')
    print("+----------+-----+---------+")

    # for i in range(0,7):
    #     print(f'|{weekdays[i]:<9} | {weekly_sale_number[i] / weekdays_count[i]:<3} | {weekly_sale_amount[i] / weekdays_count[i]:<10.2f}')

    print("+----------+-----+---------+")


    bar_colors = ['tab:blue','tab:blue','tab:blue','tab:blue','tab:blue','tab:red','tab:red']

    myBars1 = plt.bar(weekdays, height=weekly_sale_number, color=bar_colors)
    plt.xlabel('Days of the week')
    plt.ylabel('Transaction Amount')
    plt.show()
    myBars2 = plt.bar(weekdays, height=weekly_sale_amount, color=bar_colors)
    plt.xlabel('Days of the week')
    plt.ylabel('Sale Amount')
    plt.show()

def most_expensive_day(return_detail,product_detail,total_sale):
    max_cost = 0
    max_cost_day = ""
    total_cost = 0
    # current_date = datetime.strptime(return_detail.strip(), "%Y-%m-%d")
    
    first_key = list(return_detail)[0]
    # current_date = return_detail[first_key]
    current_date = datetime.strptime(return_detail[first_key]['date'].strip(), "%Y-%m-%d")

    for id,detail in return_detail.items():

        transaction_date = datetime.strptime(detail['date'].strip(), "%Y-%m-%d")
        prod_id = total_sale[id]['product_id']

        quantity = total_sale[id]['quantity']

        reshelf_cost = int(product_detail[prod_id]['price']) * quantity * 0.1

        if current_date != transaction_date:
            total_cost = 0
            total_cost+=reshelf_cost
        else:
            total_cost+=reshelf_cost

        current_date = transaction_date

        if total_cost>max_cost:
            max_cost = total_cost
            max_cost_day = current_date
    
    returned_products = []
    no_of_returns = []
    print(f'{max_cost} {max_cost_day}')
    for id,detail in return_detail.items():
        if datetime.strptime(detail['date'].strip(), "%Y-%m-%d") == max_cost_day:
            returned_products.append(total_sale[id]['product_id'])
            no_of_returns.append(total_sale[id]['quantity'])

    formatted_date = max_cost_day.strftime("%A, %B %d, %Y")
    print(f'{formatted_date} Total Retuen Shelving(RS) Cost = $ {max_cost}')

    print(f'{"PID":<3} {"Product Name":>20} {"NoI":<3} {"RS Cost":>10}')
    for i in range(len(returned_products)):
        rs = int(product_detail[returned_products[i]]['price']) * 0.1
        print(f'{returned_products[i]:<3} {product_detail[returned_products[i]]['product_name']:>20} {no_of_returns[i]:>3} ${rs:>10.2f}')

def reorder(updated_sale,product_detail):
    order_list = [0] * 20

    file = open("order_supplier_January.txt", "w", encoding = "utf-8")
    # file.write("transaction_id,sales_count\n")

    for id,detail in updated_sale.items():
        prod_id = detail['product_id']
        position = int(prod_id[1:])
        order_list[position-1] += int(detail['quantity'])

    for i in range(0,20):
        prod_id = "P" + str(i + 1)
        prod_name = product_detail[prod_id]['product_name']
        file.write(prod_id + "#" + prod_name + "#" + str(order_list[i]) + "\n")
        print(f'{prod_id:>3} {prod_name:<20} {order_list[i]:>3}')

    return order_list


def unwanted_products(each_product_sale,product_detail,total_sale):
    never_sold = []
    sorted_product = [] * 20
    least_sales = 99999
    for i in range(0,20):
        if each_product_sale[i] == 0:
            prod_id = "P" + str(i + 1)
            never_sold.append(prod_id)
    
    if never_sold:
        for i in never_sold:
            print(f'{i:>3} {product_detail[i]['product_name']:<20}')

    else:
        dates = []
        for i in range(0,20):
            if each_product_sale[i] < least_sales:
                least_sales = each_product_sale[i]
                position = i            


        prod_id = "P" + str(position+1)
        for id,detail in total_sale.items():
            if detail['product_id'] == prod_id:
                if detail['date'] not in dates:
                    dates.append(detail['date'])

        print(f'Least Sales:\n')
        print(f'{prod_id:>3} {product_detail[prod_id]['product_name']:<20} {each_product_sale[position]} {dates}')

def correlation(updated_sale,product_detail,each_product_sale):
    tot_discount = [0] * 20
    avg_discount = [0] * 20
    original_price = [0] * 20

    for id,detail in updated_sale.items():
        prod_id = detail['product_id']
        position = int(prod_id[1:])
        tot_discount[position - 1] += (float(detail['discount']) * detail['quantity'])
    
    for i in range(0,20):
        avg_discount[i] = (tot_discount[i] / each_product_sale[i]) * 100
        prod_id = "P" + str(i+1)
        original_price[i] = float(product_detail[prod_id]['price'])


    r = np.corrcoef(avg_discount,original_price)
    print(f'Pearson Correlation = {r[0,1]:.3f}')
    coef = np.polyfit(avg_discount,original_price,1)
    poly1d_fn = np.poly1d(coef)
    plt.plot(avg_discount,original_price,'bo',avg_discount, poly1d_fn(avg_discount), '--k')
    plt.xlabel("Average Discount")
    plt.ylabel("Original Price")
    plt.show()




def main():

    transaction_file = open_file("transactions_Sales_January.csv")
    return_file = open_file("transactions_Returns_January.csv")
    product_file = open_file("transactions_Products_January.csv")

    total_sale = total_sales(transaction_file)

    product_detail = product_details(product_file)
    # print(product_detail)
    return_detail = returns(return_file)
    updated_sale = update_sales(total_sale,return_file)

    print("Q1:\n")
    q1(total_sale,product_detail)


    print("\nQ2:\n")
    weekly_business(total_sale,product_detail)

    print("\nQ3:\n")
    most_expensive_day(return_detail,product_detail,total_sale)

    # print("\nQ4:\n")
    # each_product_sale = reorder(updated_sale,product_detail)
    # # print(each_product_sale)

    # print("\nQ5:\n")
    # unwanted_products(each_product_sale,product_detail,total_sale)

    # print("\nQ6:\n")
    # correlation(updated_sale,product_detail,each_product_sale)

main()