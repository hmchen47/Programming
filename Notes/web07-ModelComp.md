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
  - "one to many" relationships
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
      <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
        onclick= "window.open('https://www.guru99.com/mvc-vs-mvvm.html')"
        src    = "https://www.guru99.com/images/1/122118_0445_MVCTutorial1.png"
        alt    = "MVC pattern"
        title  = "MVC pattern"
      />
    </figure>


- Model component
  - storing data and related logic
  - representing data being transferred between controller components or any other related business logic
  - example: 
    - a Controller object retrieving the customer info from the database
    - Model: manipulate data and send it back to the database or use it to render the same data


- View component
  - part of the Application that represents the presentation of data
  - created by the data gathered from the model data
  - requesting the Model to give information so that it resents the output to the user
  - representing the data from charts, diagrams, and table
  - example: any customer view will include all the UI components like text boxes, dropdowns, etc.


- Controller component
  - part of the Application that handles the user interaction
  - interpreting the mouse and keyboard inputs from the user, informing the Model and the View to change as appropriate
  - sending commands to the Model to update its state, e.g., saving a specific document
  - sending commands to its associated view to change the View’s presentation, e.g., scrolling a particular document



## MVVM Pattern

- MVVM architecture
  - facilitating a separation of development of the graphical user interface with the help of mark-up language or GUI code
  - view model: a value converter that means that it is view model’s responsibility for exposing the data objects from the Model in such a way that objects are easily managed and presented
  - offerring two-way data binding between view and view-model
  - automating the propagation of modifications inside View-Model to the view
  - view-model: making use of observer pattern to make changes in the view-model
  - architecture

    <figure style="display: table; margin: auto; text-align: center;"">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
        onclick= "window.open('https://www.guru99.com/mvc-vs-mvvm.html')"
        src    = "https://www.guru99.com/images/2/041720_1054_MVCvsMVVMKe2.png"
        alt    = "MVVM pattern"
        title  = "MVVM pattern"
      />
    </figure>




