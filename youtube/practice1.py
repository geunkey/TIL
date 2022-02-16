from hashlib import blake2b


def deposit(balance, money):
    print(f'입금완료 잔액은 {balance + money}입니다.')
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print(f'출금완료 잔액은{balance - money}원 입니다.')
        return balance - money
    else:
        print(f'출금이 완료되지 않음. 잔액은{balance}원')
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission



balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 400)

commission, balance = withdraw_night(balance, 500)
print(f'수수료 {commission}, 잔액은 {balance}')