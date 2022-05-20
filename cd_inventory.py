"""
Title: CD Inventory
Desc: Displays menu to user to choose between adding CD info, display info, save to file, or exit
Change Log: (Who, When, What)
NToulas, 2022-May-17, Created File
"""

cd_data = {'ID': ['Artist Name', 'Album Name', 'Year Released']}
# print(cd_data)

cd_data['1234'] = ['Essam', '12.12', '2018']
# print(cd_data)

cd_file = 'cd_inventory.txt'

ALBUM_ID_INDEX = 0
ARTIST_NAME_INDEX = 1
ALBUM_NAME_INDEX = 2
ALBUM_YEAR_INDEX = 3

name = input('Welcome! Please sign your name: ')
print(f'Welcome to {name.title()}\'s Music Collection.')
while True:
    # displays menu
    print('Please choose from the following options:')
    print("1. View current inventory", "2. Add new album", "3. Delete album from inventory", "4. Save to file", "5. Exit", sep='\n')
    user_input = input('What would you like to do? ')
    import random
    # option 1: display current inventory
    if user_input == '1':
        for key, value in cd_data.items():
            print(f"{key} | {value}")
    # option 2: add new album
    elif user_input == '2':
        album_id = str(random.randint(1000, 9999))
        artist_name = input('Enter Artist Name: ')
        album_name = input('Enter Album Name: ')
        album_year = input('Enter Release Year (n/a if unknown): ')
        cd_data[album_id] = [artist_name.title(), album_name.title(), album_year]
    # option 3: delete album from inventory
    elif user_input == '3':
        del_album = input('Please enter album ID: ')
        for key in cd_data.keys():
            #if/el statement for checking to see if user inputs only numbers
            if key == del_album:
                print("Album", cd_data[del_album], "will now be deleted")
                cd_data.pop(del_album)
                break
            #

    # option 4: save data to file cd_inventory.txt
    # elif user_input == '4':
    #     del cd_data['ID']
    #     with open('cd_inventory.txt', 'a') as file:
    #         for row in data:
    #             file.write(f"\n           ID: {row[ALBUM_ID_INDEX]}\n  Artist Name: {row[ARTIST_NAME_INDEX]}\n   Album Name: {row[ALBUM_NAME_INDEX]}\nYear Released: {row[YEAR_NUM_INDEX]}\n")
    # option 5: exit program
    elif user_input == '5':
        print('Thank you for accessing your Music Collection. Goodbye!')
        break
    else:
        print("That is not a valid input. Please try again.")