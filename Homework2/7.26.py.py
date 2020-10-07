def exact_change():
  user_total = int(input(''))
  if user_total <= 0:
    print('no change')
  else:

    num_dollars = user_total // 100
    user_total %= 100
    num_quarters = user_total // 25
    user_total %= 25
    num_dimes = user_total // 10
    user_total %= 10
    num_nickels = user_total // 5
    user_total %= 5
    num_pennies = user_total

    if num_dollars >1:
        print('%d dollars' % num_dollars)
    elif num_dollars ==1:
        print('%d dollar' % num_dollars)
    if num_quarters > 1:
        print('%d quarters' % num_quarters)
    elif num_quarters ==1:
        print('%d quarter' % num_quarters)
    if num_dimes >1:
        print('%d dimes' % num_dimes)
    elif num_dimes ==1:
        print('%d dime' % num_dimes)
    if num_nickels >1:
        print('%d nickels' % num_nickels)
    elif num_nickels ==1:
        print('%d nickel' % num_nickels)
    if num_pennies >1:
        print('%d pennies' % num_pennies)
    elif num_pennies ==1:
        print('%d penny' % num_pennies)
exact_change()