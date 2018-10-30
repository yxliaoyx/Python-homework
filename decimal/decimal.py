import decimal

m = decimal.Decimal(input('本金:'))
r = decimal.Decimal(input('利率:'))
y = decimal.Decimal(input('存幾年:'))

print('本利和:{}'.format(m * (1 + r) ** y))
# 本金:100000
# 利率:0.06
# 存幾年:100
# 本利和:33930208.35144854913075581851
