# Applying SOLID principles to TypeScript

Author: Destiny Erhabor

Date: 2023-01-13

[Original](https://blog.logrocket.com/applying-solid-principles-typescript/)


## Introduction

Defined long ago, the SOLID principles are intended to improve the readability, adaptability, extensibility, and maintainability of object-oriented designs. The five SOLID principles of object-oriented class design facilitate the development of understandable, tested software that many developers can use at any time and place.

We give [Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin), popularly known as Uncle Bob, credit for this idea in his 2000 work, [Design Principles and Design Patterns](http://staff.cs.utu.fi/~jounsmed/doos_06/material/DesignPrinciplesAndPatterns.pdf). He’s also known for the best-selling books [Clean Code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/) and [Clean Architecture](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/). The abbreviation SOLID was later coined by [Michael Feathers](https://github.com/rafaelfgx/SOLID) to illustrate the ideas identified by Uncle Bob.

In this article, we’ll go over each of the SOLID principles, providing TypeScript examples to illustrate and understand them. Let’s get started!


## S: Single-responsibility principle

According to the single-responsibility principle, a class should be responsible for only one activity and only have one cause to change. This rule also includes modules and functions.

Let’s consider the example below:

```cpp
class Student {
  public createStudentAccount(){
    // some logic
  }

  public calculateStudentGrade(){
    // some logic
  }

  public generateStudentData(){
    // some logic
  }
}
```

The idea of a single duty is broken in the `Student` class above. As a result, we should divide the `Student` class into different states of responsibility. According to SOLID, the idea of responsibility is a reason to change.

To pinpoint a reason to change, we need to look into what our program’s responsibilities are. We might change the `Student` class for three different reasons:

- The `createStudentAccount` computation logic changes
- The logic for calculating student grades changes
- The format of generating and reporting student data changes

The single-responsibility principle highlights that the three aspects above put three different responsibilities on the `Student` class:

```cpp
class StudentAccount {
  public createStudentAccount(){
    // some logic
  }
}


class StudentGrade {
  public calculateStudentGrade(){
    // some logic
  }
}


class StudentData {
  public generateStudentData(){
    // some logic
  }
}
```

Now that we‘ve divided the classes, each has only one duty, one responsibility, and only one alteration that needs to be made. Now, our code is simpler to explain and comprehend.



## O: Open-closed principle

According to the open-closed principle, software entities should be open for extension but closed for modification. The essential concept behind this approach is that we should be able to add new functionality without requiring changes to the existing code:

```cpp
class Triangle {
  public base: number;
  public height: number;
  constructor(base: number, height: number) {
    this.base = base;
    this.height = height;
  }
}

class Rectangle {
  public width: number;
  public height: number;
  constructor(width: number, height: number) {
    this.width = width;
    this.height = height;
  }
}
```

Let’s imagine that we want to develop a function that calculates the area of a collection of shapes. With our current design, it might appear something like the following:

```cpp
function computeAreasOfShapes(
  shapes: Array<Rectangle | Triangle>
) {
  return shapes.reduce(
    (computedArea, shape) => {
      if (shape instanceof Rectangle) {
        return computedArea + shape.width * shape.height;
      }
      if (shape instanceof Triangle) {
        return computedArea + shape.base * shape.height * 0.5 ;
      }
    },
    0
  );
}
```

The problem with this method is that every time we add a new shape, we have to change our `computeAreasOfShapes` function, thereby violating the open-closed concept. To demonstrate this, let’s add another shape called Circle:

```cpp
class Circle {
  public radius: number;
  constructor(radius: number) {
    this.radius = radius;
  }
}
```

As against the open-closed principle, the `computeAreasOfShapes` function will have to change to a circle instance:

```cpp
function computeAreasOfShapes(
  shapes: Array<Rectangle | Triangle | Circle>
) {
  return shapes.reduce(
    (calculatedArea, shape) => {
      if (shape instanceof Rectangle) {
        return computedArea + shape.width * shape.height;
      }
      if (shape instanceof Triangle) {
        return computedArea + shape.base * shape.height * 0.5 ;
      }
      if (shape instanceof Circle) {
        return computedArea + shape.radius * Math.PI;
      }
    },
    0
  );
}
```

We can solve this issue by enforcing that all of our shapes have a method that returns the area:

```cpp
interface ShapeAreaInterface {
  getArea(): number;
}
```

Now, the `shapes` class will have to implement our defined `interface` for `ShapeArea` to call its `getArea()` method:

```cpp
class Triangle implements ShapeAreaInterface {
  public base: number;
  public height: number;
  constructor(base: number, height: number) {
    this.base = base;
    this.height = height;
  }

  public getArea() {
    return this.base * this.height * 0.5
  }
}

class Rectangle implements ShapeAreaInterface {
  public width: number;
  public height: number;
  constructor(width: number, height: number) {
    this.width = width;
    this.height = height;
  }
  public getArea() {
    return this.width * this.height;
  }
}
```

Now that we’re certain that all of our shapes have the `getArea` method, we can utilize it further. From our `computeAreasOfShapes` function, let’s update our code as follows:

```cpp
function computeAreasOfShapes(
  shapes: Shape[]
) {
  return shapes.reduce(
    (computedArea, shape) => {
      return computedArea + shape.getArea();
    },
    0
  );
}
```

Now, we don’t have to change our `computeAreasOfShapes` function every time we add a new shape. You can test this out with the `Circle` shape class. We make it open for extension but closed for modification.



## L: Liskov substitution principle

The Liskov substitution principle, put forth by [Barbara Liskov](https://en.wikipedia.org/wiki/Liskov_substitution_principle), helps to ensure that modifying one aspect of our system does not affect other elements negatively.

According to the Liskov substitution principle, subclasses should be interchangeable with their base classes. This indicates that, assuming that class `B` is a subclass of class `A`, we should be able to present an object of class `B` to any method that expects an object of type `A` without worrying that the method may produce strange results.

To make it clearer, we‘ll dissect this idea into different components. Let’s use the example of a rectangle and square:

```cpp
class Rectangle {
    public setWidth(width) {
        this.width = width;
    }
    public setHeight(height) {
        this.height = height;
    }
    public getArea() {
        return this.width * this.height;
    }
}
```

We have a straightforward `Rectangle` class, and the `getArea` function returns the rectangle’s area.

Now, we’ll choose to make another class specifically for squares. As you may well know, a square is simply a particular variety of rectangle in which the width and height are equal:

```cpp
class Square extends Rectangle {

    setWidth(width) {
        this.width = width;
        this.height = width;
    }

    setHeight(height) {
        this.width = height;
        this.height = height;
    }
}
```

The code above runs without errors, as shown below:

```cpp
let rectangle = new Rectangle();
rectangle.setWidth(100);
rectangle.setHeight(50);
console.log(rectangle.getArea()); // 5000
```

But, we’ll run into problems when we swap out a parent class instance for one of its child classes:

```cpp
let square = new Square();
square.setWidth(100);
square.setHeight(50);
```

Given that `setWidth(100)` is expected to set both the width and height to `100`, you should have `10,000`. However, this will return `2500` as a result of the `setHeight(50)`, breaking the Liskov Substitution Principle.

To remedy this, you should create a general class for all shapes that contains all of the generic methods you want the objects of your subclasses to be able to access. Then, you’ll make a specific class for each unique method, like a rectangle or square.


## I: Interface segregation principle

The interface segregation principle encourages smaller, more targeted interfaces. According to this concept, multiple client-specific interfaces are preferable to a single general-purpose interface.

To see how easy it is to understand and use this simple theory, let’s consider the following scenario:

``` cpp
interface ShapeInterface {
    calculateArea();
    calculateVolume();
}
```

All of the methods must be defined when a class implements this interface, even if you won’t use them, or if they don’t apply to that class:

```cpp
class Square implements ShapeInterface {
    calculateArea(){
        // some logic
    }
    calculateVolume(){
        // some logic
    }  
}

class Cylinder implements ShapeInterface {
    calculateArea(){
        // some logic
    }
    calculateVolume(){
        // some logic
    }    
}
```

From the example above, you’ll see that you cannot determine the volume of a square or rectangle. You must declare every method, even the ones you won’t use or need because the class implements the interface.

Instead, we might put in place more compact interfaces, sometimes known as role interfaces:

```cpp
interface AreaInterface {
    calculateArea();
}

interface VolumeInterface {
    calculateVolume();
}
```

We can prevent bloating interfaces and simplify program maintenance by altering the way we think about interfaces:

```cpp
class Square implements AreaInterface {
    calculateArea(){
        // some logic
    }
}

class Cylinder implements AreaInterface, VolumeInterface {
    calculateArea(){
        // some logic
    }
    calculateVolume(){
        // some logic
    }    
}
```


## D: Dependency inversion principle

According to the dependency inversion concept, high-level modules shouldn’t be dependent on low-level modules. Instead, both should rely on abstractions.

Uncle Bob sums up this rule as follows in his 2000 article, Design Principles and Design Patterns:

> "If the open-closed principle (OCP) states the goal of object oriented (OO) architecture, the DIP states the primary mechanism".

Simply said, both high-level and low-level modules will depend on abstractions rather than high-level modules dependent on low-level modules. Every dependency in the design should be directed toward an abstract class or interface. No dependency should target a concrete class.

Let’s construct an illustration to further explore this principle. Consider an order service. In this example, we’ll use the `OrderService` class, which records orders in a database. The low level class `MySQLDatabase` serves as a direct dependency for the `OrderService` class.

In this case, we’ve violated the dependency inversion principle. In the future, if we were to switch the database that we’re utilizing, we’d need to modify the `OrderService` class:

```cpp
class OrderService {
  database: MySQLDatabase;

  public create(order: Order): void {
    this.database.create(order)
  }

  public update(order: Order): void {
    this.database.update
  }
}

class MySQLDatabase {
  public create(order: Order) {
    // create and insert to database
  }

  public update(order: Order) {
    // update database
  }
}
```

By designing an interface and making the `OrderService` class dependent on it, we can improve on this situation by reversing the dependency. Now, rather than relying on a low-level class, the high-level class depends on an abstraction.

We create an interface that helps abstract our services as follows:

```cpp
interface Database {
  create(order: Order): void;
  update(order: Order): void;
}

class OrderService {
  database: Database;

  public create(order: Order): void {
    this.database.create(order);
  }

  public update(order: Order): void {
    this.database.update(order);
  }
}

class MySQLDatabase implements Database {
  public create(order: Order) {
    // create and insert to database
  }

  public update(order: Order) {
    // update database
  }
}
```

Now, without changing the `OrderService` class, we can add and extend new databases services.


## Conclusion

In this article, we’ve explored every SOLID principle with practical examples using TypeScript. The SOLID principles allow us to improve the readability and maintainability of our code, and they also make it simpler to increase our codebase without compromising other areas of our application.

When writing code, you should keep these guidelines in mind. Be sure to understand what they mean, what they do, and why you need them in addition to object oriented programming (OOP). Happy coding!



