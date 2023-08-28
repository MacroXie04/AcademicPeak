# Inheritance and Polymorphism

### Inheritance

Inheritance is a fundamental feature of object-oriented programming that allows one class(subclass) to inherit the properties and methods of another class(superclass). The main purpose of inheritance is to enable code reuse and extensibility, making the program easier to maintain and extend. 

When one class inherits another, it acquires all the public and protected attributes and methods of the superclass. The subclass can then add or override these properties and methods as needed. This helps reduce code duplication and improves the modularity of the program.

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

The **dog** class inherits the animal class. This means that the **dog** class will acquire all the properties and methods of the **animal** class. In this case, the **dog** class overrides the **makeSound** methods, so when the **makeSound** method of a **dog** object is called it will output “*The dog barks.*”

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

Java supports single inheritance, meaning a class can only inherit from one superclass. However, multiple inheritance can be achieved through interfaces. Additionally, all classes in Java directly or indirectly inherit from the **java.lang.Object** class, which is the root class in the Java class hierarchy. 

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

Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. This enables the same method or interface to be used with different types, providing flexibility and extensibility in code. Polymorphism comes in two main flavors: compile-time (static) polymorphism and runtime (dynamic) polymorphism. 

- Compile-time polymorphism (Static): This type of polymorphism is achieved through method overloading, which allows multiple methods with the same name but different parameters (either in the number or types of parameters) within the same class.

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

- Runtime polymorphism (Dynamic): This type of polymorphism is achieved through method overriding, which occurs when a subclass provides a new implementation for a method that is already defined in its superclass. Runtime polymorphism allows the program to decide which method implementation to call based on the actual type of the object at runtime.

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

- The **super** keyword is used to refer to the immediate superclass of a subclass. It allows you to call the superclass's methods or access its fields when you need to. This is particularly useful when you want to override a method in the subclass but still want to call the superclass's implementation of the method.

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

- The **super** keyword can also be used to call the superclass's constructor from the subclass's constructor. This is particularly useful when the superclass has some fields that need to be initialized before the subclass's constructor is executed.

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