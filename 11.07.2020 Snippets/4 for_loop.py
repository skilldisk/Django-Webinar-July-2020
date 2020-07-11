############## FOR LOOP ##############

fruits = ['apple', 'mango', 'orange', 'pineapple']

for fruit in fruits:
    print(fruit)


SKILL_DISK =    {'website':'www.skilldisk.com',
                 'pincode':560010,
                 'lattitude':12.9795,
                 'longtitude':77.5537,
                 'phone':[9900444966, 7829006066]
                }


for key in SKILL_DISK:
    print(key)


for value in SKILL_DISK.values():
    print(value)


for key, value in SKILL_DISK.items():
    print(key, end=' : ')
    print(value)
