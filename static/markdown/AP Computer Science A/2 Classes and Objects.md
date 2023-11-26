# Classes and Objects

### OOP (O****bject-Oriented Programming****)

Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data
and code that manipulates the data. Objects can interact with one another to achieve specific functions. The goal of OOP
is to break down complex programs into smaller, more manageable objects.

In OOP, each object has both attributes (data) and behaviors (functions). OOP provides a way to organize and manage code
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