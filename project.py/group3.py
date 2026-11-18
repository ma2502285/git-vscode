def menu():
    menu = '''--- Retail Inventory and Sales System ---
1. Add New Product
2. Record a Sale
3. Restock Product
4. Delete Discontinued Product
5. Search Products by Supplier
6. Search Products Below Stock Threshold
7. Display Sales Report by Date
8. Calculate Total Revenue per Product
9. Display Top-Selling Products
10. Save and Exit
Enter your choice (1-10):'''
    print(menu)
    choice=int(input('Enter the Choice:'))
    while choice <11:
        if choice == 1:
            add_new_product()
        elif choice==2:
            record_sale()
        elif choice==3:
            restock_product()
        elif choice==4:
            delete_discounted_producr()
        elif choice==5:
            search_products_by_supplier()
        elif choice==6:
            search_low_stock()
        elif choice==7:
            display_sales_report_by_date()
        elif choice==8:
            calculate_total_revenue_per_product()
        elif choice==9:
            display_top_selling_product()
        elif choice==10:
            save_and_exit()
        
            choice = int(input('Enter the Choice:'))


def add_new_product():
    extra_product_id=input('Enter Product ID:')
    f=open('products.txt','r')
    product_ID=f.readline()
    while product_ID!='':
        name=f.readline()
        price=f.readline()
        stock_quantity=f.readline()
        supplier_id=f.readline()
        product_ID=f.readline()
        if extra_product_id==product_ID:
            print(f'Product ID already exists {extra_product_id}. Please enter a unique ID.')
            extra_product_id=input('Enter Product ID:')
            extra_product_name=input('Enter Product Name:')
        extra_price=int(input('Price:'))
        if extra_price<0:
            print('Error: Price must be greater than 0.')
            extra_price=int(input('Enter Price:'))
        extra_stock_quantity=int(input('Enter Stock Quantity:'))
        if extra_stock_quantity<0:
                print('Error: Stock Quantity must be 0 or more.')
                extra_stock_quantity=int(input('Enter Stock Quantity:'))
        extra_supplier_id=input('Enter Supplier ID:')
        if extra_supplier_id != supplier_id:
            print(f'Error: Supplier ID"{extra_supplier_id}" not found. Please enter a valid supplier ID.')
            extra_supplier_id=input('Enter Supplier ID:')
        print('Product added successfully.')
    f.close()