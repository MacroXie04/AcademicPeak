# Classes

## Creating and Using a Class

### Creating and Using a Class


```python
class Dog():
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def sit(self):
        print(f'{self.name.title()} is now sitting')

    def roll_over(self):
        print(f'{self.name.title()} rolled over')
```

### The  __init__()  Method

>The __init__() method is a special method in Python used for initialization when creating an object. It acts as a constructor and is automatically called during the instantiation process of a class.

>When you create a new object using a class, the __init__() method is automatically invoked, allowing you to perform initial setup for the object. This method can take parameters and use them to assign values to the object's attributes.


```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
print(person1.name)
print(person1.age)
```

>In the above example, the Person class has an __init__() method that takes two parameters: name and age. When initializing the object, the passed values are used to assign values to the object's name and age attributes.

>Note that the first parameter of the __init__() method is typically self, which represents the current instance of the object. Within the method, self is used to access and manipulate the object's attributes.

>In summary, the __init__() method allows you to perform initialization operations and assign initial values to the object's attributes when creating an object.

### Making an Instance from a Class

>Define the class: Start by defining the class using the class keyword and give it a name. Inside the class, you can define attributes and methods that describe the behavior of the objects created from the class.


```python
class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def my_method(self):
        # Code for the method
        pass
```

>Create an instance: To create an instance (also known as an object) of the class, you call the class name as if it were a function, passing any required arguments to the constructor method (__init__ in Python). The constructor method initializes the instance with the provided values.


```python
# Create an instance of MyClass
# my_object = MyClass(value1, value2)
# In this example, value1 and value2 are the values that will be assigned to attribute1 and attribute2 respectively.
```

> Use the instance: Once the instance is created, you can access its attributes and methods using the dot notation (.).


```python
# Access attributes
print(my_object.attribute1)
print(my_object.attribute2)

# Call a method
my_object.my_method()
```

## Working with Classes and Instances

### The Car Class


```python
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
```

### Setting a Default Value for an Attribute


```python
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it')

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

### Modifying Attribute Values


```python
class Example():
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def print_data(self):
        print(f'data1 is {self.data1}')
        print(f'data2 is {self.data2}')

    def change_data1(self, data):
        self.data1 = data

print('Modifying an Attribute’s Value Directly')
Example = Example('20','15')
Example.print_data()
Example.data2 = 10000
Example.print_data()
print()

print("Modifying an Attribute’s Value Through a Method")
Example.change_data1(30)
Example.print_data()
```

## Inheritance

>In Python, when defining a child class, you can override the __init__() method of the parent class by defining a new __init__() method in the child class. This allows you to customize the initialization process for the child class.

>The __init__() method is a special method in Python classes that gets called automatically when an object is created from the class. It is used to initialize the attributes of the object.


```python
class ParentClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

class ChildClass(ParentClass):
    def __init__(self, attribute1, attribute2, attribute3):
        super().__init__(attribute1, attribute2)
        self.attribute3 = attribute3
```

>In the example above, ChildClass is a child class that inherits from ParentClass. The __init__() method in the child class takes three arguments: attribute1, attribute2, and attribute3.

>To initialize the attributes attribute1 and attribute2 inherited from the parent class, we call the __init__() method of the parent class using the super() function. This ensures that the initialization code in the parent class is executed. Then, we initialize the attribute3 specific to the child class.

>By using super().__init__(attribute1, attribute2), we pass the values of attribute1 and attribute2 to the parent class constructor, allowing it to initialize those attributes before adding the child class-specific attribute.


```python
obj = ChildClass('value1', 'value2', 'value3')
```

>This will create an object of ChildClass and initialize its attributes attribute1, attribute2, and attribute3 with the corresponding values value1, value2, and value3.


```python
# Example
class Car_example():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.make}, {self.model}, {self.year}'
        return long_name.title()

    def read_odometer(self):


```
