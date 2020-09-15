service_prices = {
    'Oil change': (35),
    'Tire rotation': (19),
    'Car wash': (7),
    'Car wax': (12),
}
Oil_change = service_prices['Oil change']
Tire_rotation = service_prices['Tire rotation']
Car_wash = service_prices['Car wash']
Car_wax = service_prices['Car wax']
first_service_cost = 0
second_service_cost = 0



price_of_oil = (35)
price_of_tire = (19)
price_of_wash = (7)
price_of_wax = (12)
print("Davy's auto shop services\n" "Oil change -- $35\n" "Tire rotation -- $19\n" "Car wash -- $7\n" "Car wax -- $12\n")

first_service = (input("Select first service:\n"))
second_service = (input("Select second service:\n"))

print("\nDavy's auto shop invoice\n")

if first_service == 'Oil change':
    print("Service 1:",'{first_service},'.format(first_service=first_service),'${price_of_oil}'.format(price_of_oil=price_of_oil))
    first_service_cost = price_of_oil
elif first_service == 'Tire rotation':
    print("Service 1:",'{first_service},'.format(first_service=first_service),'${price_of_tire}'.format(price_of_tire=price_of_tire))
    first_service_cost = price_of_tire
elif first_service == 'Car wash':
    print("Service 1:",'{first_service},'.format(first_service=first_service),'${price_of_wash}'.format(price_of_wash=price_of_wash))
    first_service_cost = price_of_wash
elif first_service == 'Car wax':
    print("Service 1:",'{first_service},'.format(first_service=first_service),'${price_of_wax}'.format(price_of_wax = price_of_wax))
    first_service_cost = price_of_wax
else:
    print("Service 1: No service")
if second_service == 'Oil Change':
    print("Service 2:",'{second_service},'.format(second_service=second_service),'${price_of_oil}'.format(price_of_oil=price_of_oil))
    second_service_cost = price_of_oil
elif second_service == 'Tire rotation':
    print("Service 2:",'{second_service},'.format(second_service=second_service),'${price_of_tire}'.format(price_of_tire=price_of_tire))
    second_service_cost = price_of_tire
elif second_service == 'Car wash':
    print("Service 2:",'{second_service},'.format(second_service=second_service),'${price_of_wash}'.format(price_of_wash = price_of_wash))
    second_service_cost = price_of_wash
elif second_service == 'Car wax':
    print("Service 2:",'{second_service},'.format(second_service=second_service),'${price_of_wax}'.format(price_of_wax = price_of_wax))
    second_service_cost = price_of_wax
else:
    print("Service 2: No service")



total_both =(first_service_cost + second_service_cost)
print(f'\nTotal: ${total_both}'.format(total_both=total_both))