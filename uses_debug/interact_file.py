# Writing to the File
xmen = './uses_debug/xmen.txt'
my_file = open(xmen, 'w+')
my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops\n',
    'Bishop\n',
    'Nightcrawler\n',
])
my_file.close()

# Reading from a File
my_file = open(xmen, 'r')
print(my_file.read())
my_file.close()

# The with Statement
with open(xmen, 'w+') as my_file:
    my_file.write('Beast\n')
    my_file.write('Phoenix\n')
    my_file.writelines([
        'Cyclops\n',
        'Bishop\n',
        'Nightcrawler\n',
    ])

my_file = open(xmen, 'r')
with my_file:
    print(my_file.read())
