"""
Title: CD Inventory
Desc: Displays menu to user to choose between adding CD info, display info, save to file, or exit
Change Log: (Who, When, What)
NToulas, 2022-May-17, Created File
"""

cd_data = {}
cd_row = {}
obj_file = None
cd_file = 'cd_inventory.txt'

ALBUM_ID_INDEX = 0
ARTIST_NAME_INDEX = 1
ALBUM_NAME_INDEX = 2

user_name = input('Welcome! Please login with your name: ')
print(f'Hello {user_name.title()}! Welcome to your Music Collection.')

while True:
    # displays menu
    print('\nPlease choose from the following options:')
    print("1. View inventory", "2. Add new album", "3. Delete album", "4. Save to file", "5. Exit", sep='\n')
    user_input = input('What would you like to do? ')

    # option 1: display current inventory
    if user_input == '1':
        obj_file = open(cd_file, 'r')
        for row in obj_file:
            cd_row = row.strip().split(',')
            cd_data[cd_row[ALBUM_ID_INDEX]] = [cd_row[ARTIST_NAME_INDEX], cd_row[ALBUM_NAME_INDEX]]
        obj_file.close()
        for key, value in cd_data.items():
            print(f"{key} | {value}")

    # option 2: add new album
    elif user_input == '2':
        import random
        album_id = str(random.randint(1000, 9999))
        artist_name = input('Enter Artist Name: ')
        album_name = input('Enter Album Name: ')
        cd_data[album_id] = [artist_name.title(), album_name.title()]
        print('Album has been successfully added!')

    # option 3: delete album from inventory
    elif user_input == '3':
        del_album = input('Please enter album ID: ')
        for key in cd_data.keys():
            if key == del_album:
                print("Album", cd_data[del_album], "will now be deleted.")
                cd_data.pop(del_album)
                break

    # option 4: save data to file cd_inventory.txt
    elif user_input == '4':
         with open(cd_file, 'a') as file:
            for key, values in cd_data.items():
                file.write(f"\n{key},{values}")
         print('Successfully saved!')

    # option 5: exit program
    elif user_input == '5':
        print(f'Thank you, {user_name.title()}, for accessing your Music Collection. Goodbye!')
        break
    else:
        print("That is not a valid input. Please try again.")