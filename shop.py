#1

import csv

PRODUCT = []
save_PRODUCT = ['','','','']

def menu():
    print()
    print('1. show')
    print('2. add')
    print('3. edit')
    print('4. delete')
    print('5. search')
    print('6. buy & print')
    print('7. save & exit')

def load():
    print('Load...')

    f = open('database.csv' , 'r')
    all = f.read()
    row = all.split('\n')
    
    for r in row:
        inf = r.split(',')
        new_dictianory = { 'id':inf[0] , 'name':inf[1] , 'price':inf[2] , 'count':inf[3] }
        PRODUCT.append(new_dictianory)
    print('Done.')

    
def save():
    print('save...')

    f = open('database.csv' , 'w')
    r = csv.writer(f)
    
    for pr in PRODUCT:    
        save_PRODUCT[0] = pr["id"]
        save_PRODUCT[1] = pr["name"]
        save_PRODUCT[2] = pr["price"]
        save_PRODUCT[3] = pr["count"]

        r.writerow(save_PRODUCT)

    f.close()
    print ('Done.')

    print()
    print('#bye#')


def show():
    print('show...')

    i = 1
    for pr in PRODUCT:
        print(i , "-" , pr)
        i += 1
    print('showed.')


def add():
    print('add...')
    
    name = input('Enter name: ')
    for c in PRODUCT:
        if name == c['name']:
            print("Exist - try new")
            return
    
    id = input('Enter id: ')
    price = input('Enter price: ')
    count = input('Enter count: ')

    PRODUCT.append({"id":id , "name":name , "price":price , "count":count})
    print('added.')
    

def edit():
    print('edit...')

    name = input('Enter name: ')
    while True:
        for c in PRODUCT:
                if name == c['name']:
                    n_id = input('Enter new id: ')
                    n_price = input('Enter new price: ')
                    n_count = input('Enter new count: ')
                    
                    c['id'] = n_id
                    c['price'] = n_price
                    c['count'] = n_count

                    print('edited.')
                    return
        print("do not Exist")
        name = input('Enter new name: ')
            

def delete():
    print('delete...')

    name = input('Enter name: ')#id
    for c in PRODUCT:
        if name == c['name']:
            
            PRODUCT.remove(c)
            print('deleted.')
            return
            
    print("do not Exist")

  
def search():
    print('search')
    
    name = input('Enter name: ')
    for c in PRODUCT:
        if name == c['name']:
            print (c)
            print('searched.')

            return True

    print("do not Exist")
    return False    


def buy():
    print('buy...')

    name = input('Enter name: ')
    for c in PRODUCT:
        if name == c['name']:

            print(c)

            id = c['id']
            price = int(c['price'])
            old = int(c['count'])

            how = int(input("How much: "))
            new = old - how
            c['count'] = str(new)

            bill = price * how

            print('buy.')
            print("*Pay: " , bill)
            print('printed.')
            return
    print("do not Exist")



load()

print()
print("*welcome*")
    
while True:
    menu()
    print()
    inp = int(input('Choose: '))
    
    if inp == 1:
        show()
        
    elif inp == 2:
        add()

    elif inp == 3:
        edit()
        
    elif inp == 4:
        delete()
        
    elif inp == 5:
        search()
        
    elif inp == 6:
        buy()
        
    elif inp == 7:
        save()
        exit()