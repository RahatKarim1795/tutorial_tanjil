from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# Function to read and parse the CSV file
def read_csv(filename):
    file_data = []
    with open(filename, 'r') as file:
        headers = file.readline().strip().split(',')
        for line in file:
            values = line.strip().split(',')
            file_data.append(dict(zip(headers, values)))
    return file_data

def get_numeric_pid(pid):
    return int(pid[1:])

def get_numeric_pid(pid):
    return int(pid[1:])

def calculate_discount_impact(sales_data, products):
    before_policy = {}
    after_policy = {}
    total_quantity_before = {}
    total_quantity_after = {}
    before_policy_count = after_policy_count = 0
    total_transactions_before = total_transactions_after = 0

    for sale in sales_data:
        date = datetime.strptime(sale['date'], '%Y-%m-%d')
        quantity = int(sale['quantity'])
        discount = float(sale['discount']) * quantity
        product_id = sale['product_id']

        if date < datetime(2024, 1, 8):
            total_transactions_before += 1
            if discount == 0:
                before_policy_count += 1
            before_policy.setdefault(product_id, []).append(discount)
            total_quantity_before[product_id] = total_quantity_before.get(product_id, 0) + quantity
        else:
            total_transactions_after += 1
            if discount == 0:
                after_policy_count += 1
            after_policy.setdefault(product_id, []).append(discount)
            total_quantity_after[product_id] = total_quantity_after.get(product_id, 0) + quantity

    
    if total_transactions_before > 0:
        avg_no_discount_before = (before_policy_count / total_transactions_before) * 100
    else:
        avg_no_discount_before = 0
    
    if total_transactions_after > 0:
        avg_no_discount_after = (after_policy_count / total_transactions_after) * 100
    else:
        avg_no_discount_after = 0
    
    print(f'{"<08-01  - >=08-01":>54}')
    print(f'Average transaction without discount: {avg_no_discount_before:05.2f}%  -  {avg_no_discount_after:05.2f}%')

    print("Average discount per product:")
    print("PID         Product Name <08-01 - >=08-01")
    for product_id in sorted(set(before_policy.keys()).union(after_policy.keys()), key=get_numeric_pid):
        if product_id in before_policy:
            before_avg = (sum(before_policy[product_id]) / (total_quantity_before[product_id])) * 100
        else:
            before_avg = 0
        if product_id in after_policy:
            after_avg = (sum(after_policy[product_id]) / (total_quantity_after[product_id])) * 100
        else: 
            after_avg = 0
        print(f'{product_id:>3} {products[product_id]["Product_Name"]:>20} {before_avg:05.2f}% - {after_avg:05.2f}%')

def day_of_the_week_sales(sales_data, products):
    weekday_sales = {}
    for i in range(7):
        weekday_sales[i] = {'transactions': 0, 'turnover': 0}

    january_days = []
    for day in range(2,32):
        january_days.append(datetime(2024, 1, day).weekday())

    weekdays_count = {}
    for i in range(7):
        weekdays_count[i] = january_days.count(i)

    for sale in sales_data:
        weekday = datetime.strptime(sale['date'], '%Y-%m-%d').weekday()
        product_id = sale['product_id']
        price = float(products[product_id]['Price'])

        discount = float(sale['discount'])
        quantity = int(sale['quantity'])
        turnover = price * quantity * (1 - discount)

        weekday_sales[weekday]['transactions'] += 1
        weekday_sales[weekday]['turnover'] += turnover

    avg_trans = {}
    avg_turn = {}
    for i in range(7):
            avg_trans[i] = round(weekday_sales[i]['transactions'] / weekdays_count[i])
            avg_turn[i] = weekday_sales[i]['turnover'] / weekdays_count[i]

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print("+-----------+-----+-------------+")
    print("| Day       |NB Tr|    Turnover |")
    print("+-----------+-----+-------------+")

    for i, day in enumerate(days):
        NB_tr = avg_trans[i]
        turnover = avg_turn[i]
        print(f"| {day:<9} | {NB_tr:^3} | ${turnover:10,.2f} |")
    print("+-----------+-----+-------------+")

    avg_trans_list = list(avg_trans.values())
    avg_turn_list = list(avg_turn.values())

    colors = []
    for i in range(7):
        if i < 5:
            colors.append('blue')
        else:
            colors.append('red')

    avg_trans_bar = plt.bar(days, avg_trans_list, color = colors)
    plt.ylabel('Transactions')
    plt.xlabel('Day of the week')
    plt.bar_label(avg_trans_bar)
    plt.show()

    avg_turn_bar = plt.bar(days, avg_turn_list, color = colors)
    plt.ylabel('Dollar Amount')
    plt.xlabel('Day of the week')
    plt.bar_label(avg_turn_bar, fmt = '{:,.0f}')
    plt.show()

def most_returns_day(returns_data, sales_data, products):
    daily_costs = {}
    product_returns = {}

    for return_ in returns_data:
        date = datetime.strptime(return_['date'], '%Y-%m-%d').date()
        t_id = return_['transaction_id']

        sale = None
        found_sale = False
        for i in sales_data:
            if i['transaction_id'] == t_id:
                sale = i
                found_sale = True

        if found_sale:
            p_id = sale['product_id']
            quantity = int(sale['quantity'])
            price = float(products[p_id]['Price'])

            RS_cost = price * quantity * 0.1

            daily_costs[date] = daily_costs.get(date, 0) + RS_cost
            product_returns[date] = product_returns.get(date, [])
            product_returns[date].append((p_id, products[p_id]['Product_Name'], quantity, RS_cost))

    most_returns_day = max(daily_costs, key=daily_costs.get)
    total_cost = daily_costs[most_returns_day]

    print(f"{most_returns_day.strftime('%A, %B %d, %Y')} Total Return Shelving(RS) Cost=${total_cost:,.2f}\n")
    print("Products Returned that day:\n")
    print("PID         Product Name NoI     RS Cost")
    for p_id, p_name, quantity, RS_cost in product_returns[most_returns_day]:
        print(f"{p_id:3} {p_name:20} {quantity:3} ${RS_cost:10,.2f}")
    print('\n')

def get_pid(sales_tuple):
    return int(sales_tuple[0][1:])

def order_supplier(sales_data, returns_data, products):
    sales = {}
    for sale in sales_data:
        product_id = sale['product_id']
        quantity = int(sale['quantity'])
        sales[product_id] = sales.get(product_id, 0) + quantity

    for return_ in returns_data:
        t_id = return_['transaction_id']
        sale = None
        found_sale = False
        for i in sales_data:
            if i['transaction_id'] == t_id:
                sale = i
                found_sale = True
        if found_sale:
            product_id = sale['product_id']
            quantity = int(sale['quantity'])
            sales[product_id] = sales.get(product_id, 0) - quantity     

    sorted_sales = sorted(sales.items(), key=get_pid)

    out_file = 'order_supplier_January.txt'
    with open(out_file, 'w') as file:
        for product_id, quantity in sorted_sales:
            name = products[product_id]['Product_Name']
            file.write(f"{product_id}#{name}#{quantity}\n")
            print(f"{product_id:>3} {name:<20} {quantity:>3}")

    print('\n')

def unwanted_products(sales_data, returns_data, products):
    sales = {}
    for pid in products:
        sales[pid] = {'sales': 0, 'date': []}

    for sale in sales_data:
        pid = sale['product_id']
        sales[pid]['sales'] += int(sale['quantity'])
        sales[pid]['date'].append(datetime.strptime(sale['date'], '%Y-%m-%d').strftime('%Y/%m/%d'))

    for return_ in returns_data:
        t_id = return_['transaction_id']
        found_sale = False
        sale = None
        for i in sales_data:
            if i['transaction_id'] == t_id:
                sale = i
                found_sale = True
        if found_sale:
            pid = sale['product_id']
            sales[pid]['sales'] -= int(sale['quantity'])

    never_sold_products = {}
    for pid, data in sales.items():
        if data['sales'] == 0:
            never_sold_products[pid] = data

    least_sales = None
    if not never_sold_products:
        min_sales = float('inf')
        for data in sales.values():
            if data['sales'] < min_sales:
                min_sales = data['sales']
        if min_sales != float('inf'):
            least_sales = min_sales
        else:
            least_sales = None

    if never_sold_products:
        for pid in never_sold_products:
            print(f"{pid:>3} {products[pid]['Product_Name']:<20}")
    else:
        for pid, data in sales.items():
            if data['sales'] == least_sales:
                dates = ','.join(data['date'])
                print(f"{pid:>3} {products[pid]['Product_Name']:<20} {least_sales:>3} [{dates}]")

def discount_price_correlation(sales_data, products, returns_data):
    total_discounts = {}
    total_units_sold = {}

    prices = []
    avg_discounts = []

    for sale in sales_data:
        p_id = sale['product_id']
        quantity = int(sale['quantity'])
        discount = float(sale['discount']) * quantity * float(products[p_id]['Price'])

        total_discounts[p_id] = total_discounts.get(p_id, 0) + discount
        total_units_sold[p_id] = total_units_sold.get(p_id, 0) + quantity

    for return_ in returns_data:
        t_id = return_['transaction_id']

        sale = None
        found_sale = False
        for i in sales_data:
            if i['transaction_id'] == t_id:
                sale = i
                found_sale = True
        

        if found_sale:
            p_id = sale['product_id']
            quantity = int(sale['quantity'])
            discount = float(sale['discount']) * quantity * float(products[p_id]['Price'])

        total_discounts[p_id] = total_discounts.get(p_id, 0) - discount
        total_units_sold[p_id] = total_units_sold.get(p_id, 0) - quantity

    for p_id, data in products.items():
        price = float(data['Price'])
        prices.append(price)

        if total_units_sold.get(p_id, 0) > 0:
            avg_discount = (total_discounts.get(p_id, 0) / (price * total_units_sold[p_id])) * 100
        else:
            avg_discount = 0
        avg_discounts.append(avg_discount)

    print(prices, avg_discounts)

    pc = np.corrcoef(prices, avg_discounts)[0,1]
    print(f"Pearson Correlation= {pc:.3f}")

    poly1d_fn = np.poly1d(np.polyfit(prices, avg_discounts, 1))

    plt.plot(prices, avg_discounts, 'bo', prices, poly1d_fn(prices), '--k')
    plt.show()

def main():
    sales_data = read_csv('transactions_Sales_January.csv')
    products_data = read_csv('transactions_Products_January.csv')
    returns_data = read_csv('transactions_Returns_January.csv')

    products = {}
    for product in products_data:
        product_id = product['Product_ID']
        products[product_id] = product

    calculate_discount_impact(sales_data , products)
    day_of_the_week_sales(sales_data, products)
    most_returns_day(returns_data, sales_data, products)
    order_supplier(sales_data, returns_data, products)
    unwanted_products(sales_data, returns_data, products)
    discount_price_correlation(sales_data, products, returns_data)

if __name__ == '__main__':
    main()