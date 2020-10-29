lem_juice = float(input('Enter amount of lemon juice(in cups):'))
water_amt = float(input('Enter amount of water(in cups):'))
agave_n = float(input('Enter amount of agave nectar(in cups):'))
ser_vings = float(input('How many servings does this make?'))

print('Lemonade ingredients - yields','{:.2f}'.format(ser_vings),'servings')
print('{:.2f}'.format(lem_juice),'cup(s)lemon juice')
print('{:.2f}'.format(water_amt),'cup(s)water')
print('{:.2f}'.format(agave_n),'cup(s)agave nectar')

servings_amt = float(input('How many servings would you like to make?\n'))

print('Lemonade ingredients - yields','{:.2f}'.format(servings_amt,'servings'))
print('{:.2f}'.format(lem_juice),'cup(s)lemon juice')
print('{:.2f}'.format(water_amt),'cup(s)water')
print('{:.2f}'.format(agave_n),'cup(s)agave nectar')

print('Lemonade ingredients - yields','{:.2f}'.format(ser_vings),'servings\n')

tru_lem = lem_juice * 8
tru_water = water_amt * 8
tru_agave = agave_n * 8

print('{:.2f}'.format(tru_lem),'cup(s)lemon juice')
print('{:.2f}'.format(tru_water),'cup(s)water')
print('{:.2f}'.format(tru_agave),'cup(s)agave nectar')

lemto_gallons = tru_lem / 16
waterto_gallons = tru_water / 16
agaveto_gallons = tru_agave / 16

print('Lemonade ingredients - yields','{:.2f}'.format(ser_vings),'servings\n')

print('{:.2f}'.format(lemto_gallons),'Gallon(s) lemon juice')
print('{:.2f}'.format(waterto_gallons),'Gallon(s) water')
print('{:.2f}'.format(agaveto_gallons),'Gallon(s) agave nectar')