# MVC vs MVVM - Difference Between Them

Author: M. Martin

Date: 2033-22-36

[Original](https://www.guru99.com/mvc-vs-mvvm.html)


## Summary

- Key Differences between MVC and MVVM
  - MVC framework: an architectural pattern that separates an application into three main logical components Model, View, and Controller. On the other hand, 
  - MVVM framework: facilitating a separation of development of the graphical user interface with the help of mark-up language or GUI code
  - controller in MVC: the entry point to the Application
  - View in MVVM: the entry point to the Application
  - MVC Model component: tested separately from the user
  - MVVM model: easy for separate unit testing, and code in event-driven
  - “one to many” relationships
    - MVC:  between Controller & View
    - MVVC: between View & View Model

## MVC Pattern

- MVC architecture
  - an architectural pattern that separates an applications into three main logical components Model, View, and Controller
  - a component is built to handle specific development aspects of an application
  - separating the business logic and presentation layer from each other
  - mainly used for desktop graphical user interfaces (GUIs)
  - components
    - Model: including all the data and its related logic
    - View: presenting data to the user or handles user interaction
    - Controller: interface between Model and View components
  - architecture

    <figure style="display: table; margin: auto; text-align: center;"">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
        onclick= "window.open('https://www.guru99.com/mvc-vs-mvvm.html')"
        src    = "https://www.guru99.com/images/1/122118_0445_MVCTutorial1.png"
        alt    = "MVC pattern"
        title  = "MVC pattern"
      />
    </figure>







