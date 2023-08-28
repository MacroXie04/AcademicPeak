# Arrays and Array Lists

### Initialization

An array is an object; therefore, the keyword new must be used in its creation. The size of an array remains fixed once it has been created. 

```java
//Example of creates an arrey of 25 double values and assigns the reference data to this array
double[] data = new double[25];

double data[] = new double[25];

double data[];
data = new double[25];

//reassign date to a new array of length 40
//new array not incloud privious data
data = new double[40];
```

### Initializer List

```java
//new and full value of intager array
int[] coins = new int[4];
coins[0]=1;
coins[1]=5;
coins[2]=10;
coins[3]=25;

//same function rewrite
int[] coins = {1,5,10,25};
```

### Length of Array

```java
int[] arr = {1, 2, 3, 4, 5};
int length = arr.length; 
// length will be 5

String[] strArr = {"apple", "banana", "orange"};
int length = strArr.length; 
// length will be 3
```

**Length counting starts from 1, while indexing starts from 0**

### Traversing a One-Dimensional Array

**Do not modify the data when using an enhanced for loop to process an array**

```java
//Return the number of even integers in array arr of integers
Public static int countEven(int[] arr){
	int count = 0;
	for (int num: arr){
		if(num%2==0){
			count++;
		}
	}
}
```

```java
//Change each even-indexed element in array arr to 0
Public static void changeEven(int[] arr){
	for(int i=0,i<arr.length,i+=2){
		arr[i]=0;
	}
}
```

### Arrays as Parameters

In Java, when an array is passed as a parameter to a function, it is typically passed by reference, which means that the function uses the address of the original array instead of a copy of the array. This means that the function can modify the original array directly, thereby affecting the original array. 

```java
//Example
public static void printArray(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        System.out.println(a
//main
int[] myArray = {1, 2, 3, 4, 5};
printArray(myArray);

printArray(1, 2, 3, 4, 5);

//output
1
2
3
4
5
```

### Array Lists

Unlike an array, which has a fixed size once it is created, an array list can change its size at runtime. When an element is added to an array list, it is appended to the end of the list. If the array list is already full, it will automatically allocate additional memory to accommodate the new element. Similarly, when an element is removed from an array list, the list automatically adjusts its size to reflect the new number of elements.

```java
import java.util.ArrayList;

public class ArrayListExample {
    public static void main(String[] args) {
        
				// Create a new ArrayList
        ArrayList<Integer> numbers = new ArrayList<Integer>();

        // Add some elements to the ArrayList
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        numbers.add(4);

        // Print out the ArrayList
        System.out.println(numbers);
				// Priny 1 2 3 4

        // Remove an element from the ArrayList
        numbers.remove(2);
				// Remove the third element(index is 2)

        // Print out the ArrayList again
        System.out.println(numbers);
				// Peint 1 2 4
				
				// Array list size
				int size = numbers.size();
				//size is 3

				// Get number in ArrayList
				int firstElement = numbers.get(0);
				// Get number 1

				// Set number in ArrayList
				numbers.set(1, 4);
				// Set 2 to 4
				// ArrayList 1 4 4
    }
}
```

```python
# Create a new list
numbers = []

# Add some elements to the list
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)

# Print out the list
print(numbers)

# Remove an element from the list
numbers.remove(2)

# Print out the list again
print(numbers)
```

### Two-Dimensional Arrays

A two-dimensional array (matrix) is often the data structure of choice for object like board games, tables of values, theater seats, and mazes. 

```java
// Example

// Declarations

int[][] table;
// table can reference a 2D array of integers
// table is currently a null reference

double[][] matrix = new double[3][4];
// matrix of double reference 3 * 4
// Each element has value of 0.0

String[][] stars = new String[2][5];
// stars of String referebce 2 * 5
// Each element has value of null

int[][] = {{3,4,5},{6,7,8}};
// row1 {3,4,5}
// row2 {6,7,8}
```

### Matrix as Array of Row Arrays

```java
// Example
// 3 * 4 Matrix

	2 6 8 7
	1 5 4 0
	9 3 2 8

	mat[1] contains {2,6,8,7}
	mat[2] contains {1,5,4,0}
	mat[3] contains {9,3,2,8}
```

### Processing a Two-Dimensional Array

- Enhanced for loop (for accessing or modifying elements that are class object, but no replacement)
- row-by-row array processing (for accessing, modifying, or replacement of elements)

```java
// Example 
// Find the sum of all elements in a matrix mat
int sum = 0;
for(int r=0;r<mat.length;r++){
	for(int c=0;c<mat[r].length;c++){
		sum += mat[r][c];
	}
]

// using enhanced for loop
int sum = 0;
for(int[]row :mat){ //for each row array in mat
	for(int element :row){ //for each element in this row
		sum += element;
	}
}
```

- row-column (for accessing, modifying elements that are class objects, or replacing elements)