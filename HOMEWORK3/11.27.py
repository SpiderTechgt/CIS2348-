#Anthony LAymond
#1636486
sporteam_dict={}

i=1
count=1
for i in range(1,6):
    j_number = int(input('Enter player {}\'s jersey number:\n'.format(i)))
    overall_rating = int(input('Enter player {}\'s rating:\n'.format(i)))
    print()

    if j_number < 0 and j_number >99 and overall_rating < 0 and overall_rating >9:
        print('invalid entry')
        break
    else:
        sporteam_dict[j_number] = overall_rating

print("ROSTER")
for j_number, overall_rating in sorted(sporteam_dict.items()):
    print("Jersey number: %d, Rating %d" % (j_number,overall_rating))

option=''

while option.upper()!='Q':
    print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\n'
          'r - Output players above a rating\no - Output roster\nq - Quit\n')

    option = input('Choose an option:\n')

if option == 'a':
    j_number = int(input('Enter a new player\'s jersey number:\n' .format(i)))
    overall_rating = int(input('Enter the players\'s rating:\n'.format(i)))
    sporteam_dict[j_number] = overall_rating

elif option == 'd':
    j_number = int(input('Enter a jersey number:\n'))
    if j_number in sporteam_dict.keys():
        del sporteam_dict[j_number]

elif option == 'u':
    j_number = int(input('Enter a jersey number:\n'))
    if j_number in sporteam_dict.keys():
        overall_rating = int(input('Enter a new rating for player:\n'))
        sporteam_dict[j_number] = overall_rating
elif option == 'r':
    overall_rating_input = int(input('Enter a rating:\n'))
    print('ABOVE{}'.format(overall_rating_input))

    for j_number,rating in sorted(sporteam_dict.items()):
        if overall_rating > overall_rating_input:
            print("Jersey number: %d, Rating: %d" % (j_number,overall_rating))
elif option == 'o':
    print("ROSTER")
    for j_number,overall_rating in sorted(sporteam_dict.items()):
        print("Jersey number: %d, Rating: %d" % (j_number,overall_rating))
