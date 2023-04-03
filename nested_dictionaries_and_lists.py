# Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

z[0]['x'] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

# Iterate Through a List of Dictionaries
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

# Get Values From a List of Dictionaries


def iterateDictionary(students):
    for i in range(len(students)):
        output = ''
        for keys in students[i]:
            output += (f"{keys} - {students[i][keys]}, ")
        else:
            output = output[:-2]
        print(output)
    return


def iterateDictionary2(key, list):
    for i in range(len(list)):
        print(list[i][key])
    return


# Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dictionary):
    repeating = False
    for keys in dictionary:
        if repeating == True:
            print('')
        else:
            repeating = True
        print(f"{len(dictionary[keys])} {keys}")
        for i in range(len(dictionary[keys])):
            print(dictionary[keys][i])
    return
