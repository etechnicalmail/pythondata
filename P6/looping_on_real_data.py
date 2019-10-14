personDetails = [
            {'name': 'John', 'age': 15, 
             'cars': [
                 {'name': 'Ford', 'models': ['Fiesta', 'Focus', 'Mustang']},
                 {'name': 'Maruti', 'models': ['800', 'Suzuki']},
                 {'name': 'Fiat', 'models': ['500', 'Panda']}]},
            {'name': 'chandu', 'age': 23,
             'cars': [
                 {'name': 'Tata', 'models': ['Nano', 'Manza']}, 
                 {'name': 'BMW', 'models': ['320', 'X3', 'X5']},
                 {'name': 'Ferrai', 'models': ['500', 'Panda']}]},
            {'name': 'ashok', 'age': 25,
             'cars': [
                 {'name': 'Maruti', 'models': ['1200', 'Suzuki']}, 
                 {'name': 'BMW', 'models': ['320', 'X3', 'X5']},
                 {'name': 'Fiat', 'models': ['500', 'Panda']}]},
            {'name': 'akshay', 'age': 30, 
             'cars': [
                 {'name': 'Ford', 'models': ['Fiesta', 'Focus', 'Mustang']},
                 {'name': 'BMW', 'models': ['320', 'X3', 'X5']},
                {'name': 'Maruti', 'models': ['800', 'Suzuki']}]}
            ]
result = 0
names = list()
for person in personDetails:
    for car in person['cars']:
        if car['name']=='Fiat' and ('Panda' in car['models']):
            print(person['name'])
            result = result + 1
            names.append(person['name'])

print(names)
print(result)
    





























