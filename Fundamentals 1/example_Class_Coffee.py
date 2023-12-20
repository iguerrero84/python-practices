class Coffee:
    # Constructor
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def check_budget(self, budget):
        # Check if the budget is valid
        if not isinstance(budget, (int, float)):
            print('Enter float or int')
            exit()
        if budget < 0:
            print('Sorry you don\'t have money')
            exit()

    def get_change(self, budget):
        return budget - self.price

    def sell(self, budget):
        self.check_budget(budget)
        if budget >= self.price:
            print(f'You can buy the {self.name} coffee')
            if budget == self.price:
                print('It\'s complete')
            else:
                print(f'Here is your change {self.get_change(budget)}$')

            exit('Thanks for your transaction')


small = Coffee('Small', 2)
regular = Coffee('Regular', 5)
big = Coffee('Big', 6)

try:
    user_budget = float(input('What is your budget? '))
except ValueError:
    exit('Please enter a number')

for coffee in [big, regular, small]:
    coffee.sell(user_budget)


# import pickle
# d = {}
# mydict = {"a": 1, "b": {"c": 10}}

# key = pickle.dumps(mydict)

# d[key] = {"d": 20}

# print(d[key])

# def sum(a, b):
#    return (a + b)

# a = int(input('Enter 1st number: '))
# b = int(input('Enter 2nd number: '))

# print(f'Sum of {a} and {b} is {sum(a, b)}')
