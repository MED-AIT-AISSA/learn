# Expense truckers 
expenses = []



def add_expense():
    name_expense = input('give the name of the expense !')
    while True : 
        try :
            amount = int(input('give the amount !'))
            if amount < 0 :
                print('give a positive amount')
                continue
            expenses.append({'name': name_expense, 'amount':amount})
            break 
        except ValueError:
            print('please give a number ') 


def Show_expenses(expense):
    if expense : 
        for ex in expense: 
            print(f"{ex['name']}\t {ex['amount']}")
    else :
        print('There is no data')

def Calculate_Totale(expense):
    somme = 0
    if expense :
        for exp in expense: 
            somme += exp['amount']
        return somme 
    else : 
        print('There is no data')


def Find_biggest_expense(expense):
    if expense :
        biggest =  max(expense, key=lambda x: x.get("amount"))
        print(f"the begest expenses{biggest['name']} , the a mount is {biggest['amount']}")
        return 
    else :
        print('there is no data')


while True: 
    print('======== Expense Trucker =============')
    print('1. Add expenses ')
    print('2. Show expenses')
    print('3. Calculate total')
    print('4. Find biggest expense ')
    print('5. Quite')


    try :
        choix = int(input('veuiller un choix'))
        if choix == 1:
            add_expense()
        elif choix == 2 :
            Show_expenses(expenses) 
        elif choix == 3 :
            totale = Calculate_Totale(expenses)
            print(f'the totale of your expenses is {totale}')
        elif choix == 4 :
            Find_biggest_expense(expenses)
        elif choix == 5:
            break
        else : 
            print('please choose number between 1 and 5 thanks') 


    except ValueError:
        print('veuillez choisir une nombre')