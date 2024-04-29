# Classes and Objects

### OOP (Object-Oriented Programming)

- Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data
and code that manipulates the data. 
- Objects can interact with one another to achieve specific functions. The goal of OOP
is to break down complex programs into smaller, more manageable objects.
- In OOP, each object has both attributes (data) and behaviors (functions). OOP provides a way to organize and manage code
through abstraction and encapsulation.

### Object

In Java, an object is an instance of a class. A class defines the behavior and properties of objects, and objects are
created from classes as instances of that class. An object can be thought of as a unique instance of a particular data
type.

For example, consider a class called **`Person`** that defines the properties and behavior of a person, such as their
name, age, and address. A single instance of the **`Person`** class can be created as an object to represent a specific
person, such as "John Doe".

```java
//Example
class Person {
   String name;
   int age;
   String address;

   void sayHello() {
      System.out.println("Hello, my name is " + name + ".");
   }
}

//main
Person john = new Person();
john.name = "John Doe";
john.age = 30;
john.address = "123 Main St.";
john.sayHello();
```

In this example, a **`Person`** object is created using the **`new`**operator, and its properties are set to specific
values. The **`sayHello`** method can be called on the **`john`** object to display a message introducing the person.

### Class

A class in Java is a blueprint or template that defines the characteristics and behavior of objects of that type. A
class can contain data fields, methods, and constructors, among other elements.

A class acts as a blueprint for creating objects (a particular data structure), providing initial values for state (
member variables or fields), and implementations of behavior (member functions or methods). An object is an instance of
a class and is created using the new keyword followed by the class name.

Classes can also be used to define a group of related objects and to provide a way to access and manipulate those
objects. They are essential to object-oriented programming and allow for abstraction and encapsulation of data and
behavior.

```java
//Example: The farmework for a simple bank account class
public class BankAccount{
//Date field
	private String password;
	private double balance;
	public static final double OVERDRAWN_PENALTY = 20.00;

//constructors
public BankAccount(){ 
/* implementation code */ 
}
public BankAccount(String acctPassword, double acctBalance){
/* implementation code */
}

//accessor
public double getBalance(){
/* implementation code */
}

//mutators
public void deposit(String acctPassword, double amount){
/* implementation code */
}
public void withdraw(String acctPassword, double amount){
/* implementation code */
}

}
```

### Public, Private, and Static

Public, Private, and Static are keywords that can be used to specify access restrictions and behaviors of class
members (fields and methods).

- Public: Members with this access level can be accessed from anywhere in the code, both inside and outside the class.
- Private: Members with this access level can only be accessed within the class they are declared.
- Static: Members with this access level belong to the class and not to instances of the class. They can be accessed
  without creating an instance of the class, using the class name instead of an object reference.

A static method or variable belongs to the class rather than an instance of the class. This means that the same value or
method is shared across all instances of a class. A static method can be called without creating an instance of the
class.

```java
//Example of using static
class Counter {
   static int count=0;
   static void addCount() {
      count++;
   }
}

class Main {
   public static void main(String args[]) {
      Counter.count=5;
      Counter.addCount();
      System.out.println("Counter: "+Counter.count);
   }
}

//output: Counter: 6
```

### Methods Headers

A method header in Java refers to the first line of code that defines a method, including its name, return type, and
parameters. The method header specifies how the method should be called and what it will return when invoked.

### Type of Methods

"Constructors," "accessors," and "mutators" are terms commonly used in object-oriented programming.

- Constructors: Constructors are special methods that are called when an object of a class is created. They are used to
  initialize the state of an object. Constructors have the same name as the class and do not have a return type.
- Accessors: Accessors, also known as getters, are methods that allow you to retrieve the values of an object's private
  fields. They are typically used to get the values of instance variables.
- Mutators: Mutators, also known as setters, are methods that allow you to change the values of an object's private
  fields. They are typically used to set the values of instance variables.
- Help Method(Private):

Accessors and Mutators are often used together to encapsulate an object's state and provide a controlled way of
accessing and modifying its values.

```java
//Example
public class Person {
   private String name;
   private int age;

   // Accessor method
   public String getName() {
      return name;
   }

   // Mutator method
   public void setName(String name) {
      this.name = name;
   }

   // Accessor method
   public int getAge() {
      return age;
   }

   // Mutator method
   public void setAge(int age) {
      this.age = age;
```

### Methods Overloading

Methods Overloading is a feature that allow multiple methods to have the same name within a class, but with different
parameters.

### Scope

Scope refers to the visibility and accessibility of variables, methods, and other elements within a program.

```java
//Example 
class Student{
    private int age;
}
```

Only Accessors and Mutators in this class can read or edit the varible (age).

### The **This** Keyword

1. Distinguishing instance variables and method parameters: When the parameter name of a method is the same as the name
   of an instanmce variable.
   Using the "this" keyword to distinguish the instance variable "name" and the constructor parameter "name”

    ```java
    //Example 
    Publiuc class Person {
    	Private String name;
    
    	public Person(String name){
    		this.name = name;
    		//Using the "this" keyword to distinguish the 
    	}
    }
    ```

2. Invoking another constructor with in a constructor: In class, there can be multiple constructors, and one constructor
   can call another constructor.
   Invoking another constructor Person(String name, int age)

    ```java
    //Example 
    public class Person {
    	private String name;
    	private int age;
    
    	public Person(String name){
    		this(name,0);
    	}
    
    	public Person(String name, int age){
    		this.name=name;
    		this.age=age;
    	}
    }
    ```

3. Returning the reference to the current object

    ```java
    public class Person {
        private String name;
        private int age;
    
        public Person setName(String name) {
            this.name = name;
            return this; 
    				// Returning the reference to the current object
        }
    
        public Person setAge(int age) {
            this.age = age;
            return this; 
    				// Returning the reference to the current object
        }
    }
    ```

### Reference vs. Primitive Data Types

- Primitive data types are basic data types that represent a single value. There are eight primitive data types in Java:
  boolean, byte, char, short, int, long, float, and double. Primitive data types are stored on the stack and directly
  contain their values.
- Reference data types, on the other hand, are not actual data values, but rather references to objects. Reference data
  types include classes, interfaces, arrays, and enumerations. They are stored on the heap and contain a memory address
  that points to the location of the actual object. Reference variables store the memory address of the object, not the
  object itself.

### The Null Reference

Null is a special keyword that represents a null reference. A null reference is a reference that does not point to any
object, meaning it does not point to any memory address in the heap.

If you attempt to access a method or property of an object using a null reference, it will result in a
NullPointerException.

```java
//Example
String str = null;
System.out.println(str.length()); 
// This will throw a NullPointerException

//Example code that uses a conditional statement to check for null reference
String str = null;
if (str != null) {
  System.out.println(str.length());
} 
else {
  System.out.println("str is null");
}
```

### Inheritance

Inheritance is a fundamental feature of object-oriented programming that allows one class(subclass) to inherit the
properties and methods of another class(superclass). The main purpose of inheritance is to enable code reuse and
extensibility, making the program easier to maintain and extend.

When one class inherits another, it acquires all the public and protected attributes and methods of the superclass. The
subclass can then add or override these properties and methods as needed. This helps reduce code duplication and
improves the modularity of the program.

```java
//Example

// Superclass
class Animal {
    public void makeSound() {
        System.out.println("The animal makes a sound");
    }
}

// Subclass
class Dog extends Animal {
    public void makeSound() {
        System.out.println("The dog barks");
    }
}
```

The **dog** class inherits the animal class. This means that the **dog** class will acquire all the properties and
methods of the **animal** class. In this case, the **dog** class overrides the **makeSound** methods, so when the *
*makeSound** method of a **dog** object is called it will output “*The dog barks.*”

Subclasses can also call the methods of the superclass using the **super** keyword.

```java
//Example 
class Dog extends Animal {
    public void makeSound() {
        super.makeSound(); 
				// Call the makeSound method of the superclass
        System.out.println("The dog barks");
    }
}
```

Java supports single inheritance, meaning a class can only inherit from one superclass. However, multiple inheritance
can be achieved through interfaces. Additionally, all classes in Java directly or indirectly inherit from the *
*java.lang.Object** class, which is the root class in the Java class hierarchy.

```java
//Example
// Superclass
class Animal {
    public void makeSound() {
        System.out.println("The animal makes a sound");
    }
}

// Subclass
class Dog extends Animal {
    public void makeSound() {
        System.out.println("The dog barks");
    }
}

// Another Subclass
class Cat extends Animal {
    public void makeSound() {
        System.out.println("The cat meows");
    }
}

// Main class
public class Main {
    public static void main(String[] args) {
        // Declare and create a Dog object (subclass of Animal)
        Dog myDog = new Dog();

        // Declare and create a Cat object (subclass of Animal)
        Cat myCat = new Cat();

        // Call methods on the Dog and Cat objects
        myDog.makeSound(); 
				// Outputs "The dog barks"
        myCat.makeSound(); 
				// Outputs "The cat meows"
    }
}
```

**Rules for Subclasses**

- A subclass can ass new private instance variables.
- A subclass can ass new public, private, or static methods.
- A subclass can override inherited methods.
- A subclass may not redefine a public methods as private.
- A subclass may not override static methods of the superclass.
- A subclass should define its own constructors.
- A subclass cannot directly access the private members of its superclass. It must use accessor or mutator methods.

### Polymorphism

Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to
be treated as objects of a common superclass. This enables the same method or interface to be used with different types,
providing flexibility and extensibility in code. Polymorphism comes in two main flavors: compile-time (static)
polymorphism and runtime (dynamic) polymorphism.

- Compile-time polymorphism (Static): This type of polymorphism is achieved through method overloading, which allows
  multiple methods with the same name but different parameters (either in the number or types of parameters) within the
  same class.

```java
class Math {
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }
}
```

- Runtime polymorphism (Dynamic): This type of polymorphism is achieved through method overriding, which occurs when a
  subclass provides a new implementation for a method that is already defined in its superclass. Runtime polymorphism
  allows the program to decide which method implementation to call based on the actual type of the object at runtime.

```java
// Superclass
class Animal {
    public void makeSound() {
        System.out.println("The animal makes a sound");
    }
}

// Subclass
class Dog extends Animal {
    public void makeSound() {
        System.out.println("The dog barks");
    }
}

// Subclass
class Cat extends Animal {
    public void makeSound() {
        System.out.println("The cat meows");
    }
}

// Main class
public class Main {
    public static void main(String[] args) {
        // Declare an Animal reference variable pointing to a Dog object
        Animal myAnimal = new Dog();
        myAnimal.makeSound(); 
				// Outputs "The dog barks"

        // Change the Animal reference variable to point to a Cat object
        myAnimal = new Cat();
        myAnimal.makeSound(); 
				// Outputs "The cat meows"
    }
}
```

### Using Super in Subclass

- The **super** keyword is used to refer to the immediate superclass of a subclass. It allows you to call the
  superclass's methods or access its fields when you need to. This is particularly useful when you want to override a
  method in the subclass but still want to call the superclass's implementation of the method.

```java
//Example
// Superclass
class Animal {
    public void makeSound() {
        System.out.println("The animal makes a sound");
    }
}

// Subclass
class Dog extends Animal {
    public void makeSound() {
        super.makeSound(); // Call the makeSound method of the superclass (Animal)
        System.out.println("The dog barks");
    }
}

// Main class
public class Main {
    public static void main(String[] args) {
        // Declare and create a Dog object
        Dog myDog = new Dog();

        // Call the makeSound method on the Dog object
        myDog.makeSound(); 
        // Outputs:
        // The animal makes a sound
        // The dog barks
    }
}
```

```python
# Superclass
class Animal:
    def make_sound(self):
        print("The animal makes a sound")

# Subclass
class Dog(Animal):
    def make_sound(self):
        super().make_sound()  
				# Call the makeSound method of the superclass (Animal)
        print("The dog barks")

# Create a Dog object
my_dog = Dog()

# Call the make_sound method on the Dog object
my_dog.make_sound()
# Outputs:
# The animal makes a sound
# The dog barks
```

- The **super** keyword can also be used to call the superclass's constructor from the subclass's constructor. This is
  particularly useful when the superclass has some fields that need to be initialized before the subclass's constructor
  is executed.

```java
// Superclass
class Animal {
    String name;

    Animal(String name) {
        this.name = name;
    }
}

// Subclass
class Dog extends Animal {
    String breed;

    Dog(String name, String breed) {
        super(name); 
				// Call the superclass's constructor
        this.breed = breed;
    }
}

// Main class
public class Main {
    public static void main(String[] args) {
        // Declare and create a Dog object
        Dog myDog = new Dog("Buddy", "Golden Retriever");

        // Access the fields of the Dog object
        System.out.println("Name: " + myDog.name); // Outputs "Name: Buddy"
        System.out.println("Breed: " + myDog.breed); // Outputs "Breed: Golden Retriever"
    }
}
```

```python
# Superclass
class Animal:
    def __init__(self, name):
        self.name = name

# Subclass
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  
				# Call the superclass's constructor
        self.breed = breed

# Create a Dog object
my_dog = Dog("Buddy", "Golden Retriever")

# Access the fields of the Dog object
print("Name:", my_dog.name)  
	# Outputs "Name: Buddy"
print("Breed:", my_dog.breed)  
	# Outputs "Breed: Golden Retriever"
```

# Recursion

Recursion is a programming technique in which a function calls itself one or more times to solve a problem. It is a
powerful and versatile tool that can be used to solve a wide range of problems, from simple mathematical computations to
complex data structures and algorithms.

To use recursion, a function typically checks if a specific termination condition has been met, and if not, the function
calls itself with a modified set of parameters until the termination condition is met. This creates a stack of function
calls, with each new call being added to the top of the stack, until the termination condition is met and the stack is "
unwound" as each function call returns.

```java 
public static int factorial(int n) {
    if (n == 0) {
        return 1; 
				// Termination condition
    } else {
        return n * factorial(n-1); // Recursive call
    }
}
```

In this function, if the input **`n`** is 0, the function returns 1 (the termination condition). Otherwise, the function
calls itself with **`n-1`** as the input, and multiplies the result with **`n`**. This process continues until the input
reaches 0, at which point the function returns the final result.

Recursion can be a powerful and elegant solution to many problems, but it can also be a source of bugs and performance
issues if not used carefully. Careful consideration should be given to the termination conditions, the base case, and
the recursive call to ensure that the function returns the correct result and does not result in an infinite loop or
excessive memory usage.