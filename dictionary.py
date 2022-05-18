my_dictionary = {'hello': 'world', 1: True, False: 2.123}
print(type(my_dictionary))
print(my_dictionary)

donor = {'alec': [200, 23], 'anubhaw': [200.01, 23.01]}

# first value is called key
print(donor['alec'])
print(donor['anubhaw'])

#add to dictionary
donor['arya'] = [123, 12234, 1232]
print(donor)

#reassign to dictionary
donor['alec'] = [-100]
print(donor)

#append to dictionary
donor['alec'].append(500)
print(donor)

#remove from list
# del donor['alec']
# donor.pop('arya')
# print(donor)

#keys() is method of dictionary
for key in donor.keys():
    print(f"{key} has values of {donor[key]}")

for values in donor.values():
    print(f"values is {values}")

for key, value in donor.items():
    print(f"{key} has {values}")
    