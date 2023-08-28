# Dictionaries

## A Simple Dictionary


```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
```

## Working with Dictionaries

>A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. A key’s value can be a number, a string, a list, or even another dictionary.
In fact, you can use any object that you can create in Python as a value in a dictionary.


```python
alien_0 = {'color': 'green', 'points': 5}
```


```python
## alien_0 = {'color': 'green'}
```

>This dictionary stores one piece of information about alien_0, namely the alien’s color. The string 'color' is a key in this dictionary, and i associated value is 'green'.

### Accessing Values in a Dictionary


```python
print(alien_0['color'])
```


```python
temp = alien_0['points']
print("You just earned " + str(temp) + " points!")
print(f"You just earned {temp} points!")
```

### Adding New Key-Value Pairs


```python
print(alien_0)
```


```python
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

### Starting with an Empty Dictionary


```python
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
```

### Modifying Values in a Dictionary


```python
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
```

### Removing Key-Value Pairs


```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
```

### A Dictionary of Similar Objects


```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(favorite_languages['jen'].title())
```

### Using get( ) to Access Value


```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['speed'])
```


```python
print(alien_0.get('points','there are no point'))
print(alien_0.get('speed','There are no point'))
```

## Looping Through a Dictionary

>A single Python dictionary can contain just a few key-value pairs or millions of pairs. Because a dictionary can contain large amounts of data, Python lets you loop through a dictionary. Dictionaries can be used to store information in a variety of ways; therefore, several different ways exist to loop through them. You can loop through all of a dictionary’s key-value pairs, through its keys, or through its values.

### Looping Through All Key-Value Pairs


```python
user_0 ={
    'username':  'efermi',
    'first':  'enrico',
    'last':  'fermi',
}
```


```python
for key, value in user_0.items():
    print(f'\nkey : {key}')
    print(f'Value : {value}')
```


```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
```


```python
for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite languages is {language.title()}")
```


```python
for key in favorite_languages.keys():
    print(key.title())
```


```python
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +", I see your favorite language is " +favorite_languages[name].title() + "!")
```

## Nesting

### A List of Dictionaries


```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
```


```python
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
```

>A more realistic example would involve more than three aliens with code that automatically generates each alien. In the following example we use range() to create a fleet of 30 aliens:


```python
# Make an empty list for storing aliens.
aliens = []
```


```python
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
```


```python
# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)

```


```python
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
```


```python
# Change the three
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
```


```python
# Show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)

```


```python
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

```

### A List in a Dictionary


```python
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
```


```python
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
```


```python
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite language are:")
    for language in languages:
        print(f"\t{language}")
    print(f"")
```

### A Dictionary in a Dictionary


```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
```


```python
for username,userinfo in users.items():
    print(f'Username: {username}')
    print(f"\tFull name: {userinfo['first'].title()} {userinfo['last'].title()}")
    print(f"\tLocation: {userinfo['location'].title()}\n")
```
