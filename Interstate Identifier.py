def interstate(highway):

    highway = int(input('Enter the highway number: \n'))

    if (highway >= 1) and (highway <= 99):
        highway_type = 'primary'
        if (highway % 2) == 0:
            highway_direction = 'east/west'
            print(f'I-{highway} is {highway_type}, going {highway_direction}.')
        else:
            highway_direction = 'north/south'
            print(f'I-{highway} is {highway_type}, going {highway_direction}.')
    elif (highway >= 100) and (highway <= 999) and ((highway % 100) != 00):
        highway_type = 'auxiliary'
        if (highway % 2) == 0:
            highway_direction = 'east/west'
            print(f'I-{highway} is {highway_type}, serving I-{highway % 100}, going {highway_direction}.')
        else:
            highway_direction = 'north/south'
            print(f'I-{highway} is {highway_type}, serving I-{highway % 100}, going {highway_direction}.')
    else:
        print(f'{highway} is not a valid interstate highway number.')
