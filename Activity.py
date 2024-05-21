import os

ls_bought = []
def fnt_limpiar():
    os.system('cls')
    print('>>>>> SPORT SHOP <<<<<')
    print('By: Cesar A. Castro P.')
    
def fnt_selector(op):
    global sw
    if op == '3':
        sw = False
    elif op == '1':
        fnt_buy()
    elif op == '2':
        fnt_query()
    
def fnt_query():
    fnt_limpiar()
    print('Items Bought:')
    for item, quantity in ls_bought:
        print(f'{item}: {quantity}')
    input('Press <ENTER> to continue...')
        
def fnt_buy():
    fnt_limpiar()
    op2 = input('Store menu\n1. Shirts\n2. Shorts\n3. Socks\n4. Shoes\n5. Soccer balls\n6. Exit\n.-> ')
    
    if op2 in ['1', '2' ,'3', '4', '5']:
        quantity = int(input('quantity?'))
        item = None
        if op2 == '1':
            item = 'Shirts'
        elif op2 == '2':
            item = 'Shorts'
        elif op2 == '3':
            item = 'Socks'
        elif op2 == '4':
            item = 'Shoes'
        elif op2 == '5':
            item = 'Soccer balls'
            
        for i, (existing_item, existing_quantity) in enumerate(ls_bought):
            if existing_item == item:
                ls_bought[i] = (existing_item, existing_quantity + quantity)
                break
        else:
            ls_bought.append((item, quantity))
        
        print(f'{quantity} {item} added to your cart.')
        input('Press <ENTER> to continue.')
    elif op2 == '6':
        print('Exiting buy menu...')
    else:
        print('Invalid option.')
        
#-----------------------


sw = True
while (sw == True):
    fnt_limpiar()
    op = input('Store menu\n1. Buy\n2. Query shops\n3. Finish\n-> ')
    fnt_selector(op)
    