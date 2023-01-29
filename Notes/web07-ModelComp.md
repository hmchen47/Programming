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


- Features of MVC
  - easy and frictionless testability
  - highly testable, extensible and pluggable framework
  - leveraging existing features offered by ASP.NET, Django, JSP, etc
  - offering full control over your HTML as well as your URLs
  - supporting Test Driven Development (TDD)
  - offering separation of logic
  - allowing routing for SEO Friendly URLs
  - offering to map for comprehensible and searchable URLs


- Advantages of MVC
  - easier support for a new type of clients
  - able to be developed parallely
  - avoiding complexity by dividing an application into separate (MVC) units
  - using a front controller pattern that processes web application requests using a single controller
  - offering the best support for test-driven development
  - working well for Web apps, which are supported by large teams of web designers and developers
  - providing a clean separation of concerns(SoC)
  - all classed and objects independent of each other $\implies$ test separately
  - allowing logical grouping of related actions on a controller together


- Disadvantages of MVC
  - business logic mixed with Ul
  - hard to reuse and implement tests
  - no formal validation support
  - increased complexity and inefficiency of data
  - the difficulty of using MVC with the modern user interface
  - a need for multiple programmers to conduct parallel programming
  - knowledge of multiple technologies is required



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


- Model component
  - storing data and related logic
  - representing data being transferred between controller components or any other related business logic
  - example
    - a Controller object will retrieve the student info from the school database
    - Model: manipulate data and send it back to the database or use it to render the same data


- View component
  - UI components like HTML, CSS, jQuery, etc. 
  - held responsible for displaying the data which is received from the Controller as an outcome
  - also transformed Model(s) into the User Interface (UI)


- View Model component
  - responsible for presenting functions, commands, methods, to support the state of the View
  - accountable to operate the model and activate the events in the View


- Features of MVVM
  - written for desktop application with data binding capabilities – XAML and the INotifyPropertyChanged interface
  - doing modification in the View-Model $\implies$ the View-Model using an observer pattern
  - mostly used by [WPF](https://www.guru99.com/sap-bods-tutorial.html), Silverlight, nRoute, etc.


- Advantages of MVVM
  - business logic decoupled from Ul
  - easy to maintain and test
  - easy to reuse components
  - loosely coupled architecture: MVVM makes your application architecture as loosely coupled
  - writing unit test cases for both the viewmodel and Model layer without the need to reference the View'


- Disadvantages of MVVM
  - maintenance of lots of codes in controller
  - some people think that for simple UIs of MVVM architecture can be overkill
  - not offering tight coupling between the view and view model


## Difference between MVC and MVVM Architecture

<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 60vw;" cellspacing=0 cellpadding=5 border=1 align="center">
  <colgroup>
    <col style="width: 20%">
    <col style="width: 20%">
  </colgroup>
  <thead>
  <tr style="font-size: 1.0em; vertical-align:middle;">
    <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;">MVC (Model View Controller)</th>
    <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;">MVVM (Model View ViewModel)</th>
  </tr>
  </thead>
  <tbody> 
    <tr>
      <td>Controller is the entry point to the Application.</td>
      <td>The view is the entry point to the Application.</td>
    </tr>
    <tr>
      <td>One to many relationships between Controller &amp; View.</td>
      <td>One to many relationships between View &amp; View Model.</td>
    </tr>
    <tr>
      <td>View Does not have reference to the Controller</td>
      <td>View have references to the View-Model.</td>
    </tr>
    <tr>
      <td>MVC is Old Model</td>
      <td>MVVM is a relatively New Model.</td>
    </tr>
    <tr>
      <td>Difficult to read, change, to unit test, and reuse this Model</td>
      <td>The debugging process will be complicated when we have complex data bindings.</td>
    </tr>
    <tr>
      <td>MVC Model component can be tested separately from the user</td>
      <td>Easy for separate unit testing and code is event-driven.</td>
    </tr>
  </tbody>
</table>


<br/>

# Difference Between MVC, MVP and MVVM Architecture Pattern in Android

Institute: Geek4Geek

Date: 2022-12-22

[Original](https://www.geeksforgeeks.org/difference-between-mvc-mvp-and-mvvm-architecture-pattern-in-android/)


- Architecture pattern
  - gives modularity to the project files
  - assures that all the codes get covered in Unit testing
  - making the task easy for developers to maintain the software
  - to expand the features of the application in the future
  - popular models and industry-recognized [android architecture pattern](https://www.geeksforgeeks.org/android-architecture-patterns/)
    - [MVC](https://www.geeksforgeeks.org/mvc-model-view-controller-architecture-pattern-in-android-with-example/) (Model — View — Controller)
    - [MVP](https://www.geeksforgeeks.org/mvp-model-view-presenter-architecture-pattern-in-android-with-example/) (Model — View — Presenter)
    - [MVVM](https://www.geeksforgeeks.org/mvvm-model-view-viewmodel-architecture-pattern-in-android/) (Model — View — ViewModel)


- The Model—View—Controller(MVC) pattern
  - splitting the code into 3 components
  - creating the class/file of the application
  - three layers
    - **Model:**
      - storing the application data
      - w/o knowledge about the interface
      - responsible for handling the domain logic(real-world business rules)
      - communication with the database and network layers
    - **View:**
      - the UI(User Interface) layer
      - holding components visible on the screen
      - providing the visualization of the data stored in the Model
      - offering interaction to the user
    - **Controller:**
      - establishing the relationship between the View and the Model
      - containing the core application logic
      - retrieving informed of the user’s response
      - updating the Model as per the need

  <figure style="display: table; margin: auto; text-align: center;"">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick= "window.open('https://www.geeksforgeeks.org/difference-between-mvc-mvp-and-mvvm-architecture-pattern-in-android/')"
      src    = "https://media.geeksforgeeks.org/wp-content/uploads/20201002214740/MVCSchema.png"
      alt    = "The Model—View—Controller(MVC) Pattern"
      title  = "The Model—View—Controller(MVC) Pattern"
    />
  </figure>


- The Model—View—Presenter (MVP) pattern
  - overcoming the challenges of MVC and provides an easy way to structure the project codes
  - providing modularity, testability, and a more clean and maintainable codebase
  - components
    - **Model:**
      - layer for storing data
      - responsible for handling the domain logic(real-world business rules)
      - communication with the database and network layers
    - **View:**
      - UI (User Interface) layer
      - providing the visualization of the data
      - keeping a track of the user’s action in order to notify the Presenter
    - **Presenter:**
      - fetching the data from the model
      - applying the UI logic to decide what to display
      - managing the state of the View
      - taking actions according to the user’s input notification from the View

  <figure style="display: table; margin: auto; text-align: center;"">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick= "window.open('https://www.geeksforgeeks.org/difference-between-mvc-mvp-and-mvvm-architecture-pattern-in-android/')"
      src    = "https://media.geeksforgeeks.org/wp-content/uploads/20201024233154/MVPSchema.png"
      alt    = "The Model—View—Presenter (MVP) Pattern"
      title  = "The Model—View—Presenter (MVP) Pattern"
    />
  </figure>


- The Model—View—ViewModel (MVVM) pattern
  - w/ some similarities with the MVP (Model—View—Presenter) design pattern
  - the Presenter role played by the ViewModel
  - drawbacks of the MVP pattern solved by MVVM
  - separating the data presentation logic (Views or UI) from the core business logic part of the application
  - components
    - **Model:**
      - responsible for the abstraction of the data sources
      - Model and ViewModel working together to get and save the data
    - **View:**
      - purpose: to inform the ViewModel about the user’s action
      - observing the ViewModel
      - not containing any kind of application logic
    - **ViewModel:**
      - exposing those data streams which are relevant to the View
      - serving as a link between the Model and the View
  
  <figure style="display: table; margin: auto; text-align: center;"">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick= "window.open('https://www.geeksforgeeks.org/difference-between-mvc-mvp-and-mvvm-architecture-pattern-in-android/')"
      src    = "https://media.geeksforgeeks.org/wp-content/uploads/20201002215007/MVVMSchema.png"
      alt    = "The Model—View—ViewModel (MVVM) Pattern"
      title  = "The Model—View—ViewModel (MVVM) Pattern"
    />
  </figure>


- Difference b/w MVC, MVP, and MVVM design pattern

  <table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 60vw;" cellspacing=0 cellpadding=5 border=1 align="center">
    <colgroup>
      <col style="width: 15%">
      <col style="width: 25%">
      <col style="width: 25%">
    </colgroup>
    <thead>
      <tr style="font-size: 1.0em; vertical-align:middle;">
        <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;">MVC (MODEL VIEW CONTROLLER)</th>
        <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;">MVP (MODEL VIEW PRESENTER)</th>
        <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;">MVVM (MODEL VIEW VIEWMODEL)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>One of the oldest software architecture</td>
        <td>Developed as the second iteration of software architecture which is advance from MVC.</td>
        <td>Industry-recognized architecture pattern for applications.</td>
      </tr>
      <tr>
        <td>UI(<strong>View</strong>) and data-access mechanism(<strong>Model</strong>) are tightly coupled.</td>
        <td>It resolves the problem of having a dependent <strong>View</strong> by using <strong>Presenter</strong> as a communication channel between <strong>Model</strong> and <strong>View</strong>.&nbsp;</td>
        <td>This architecture pattern is more event-driven as it uses data binding and thus makes easy separation of <strong>core business logic</strong> from the <strong>View</strong>.</td>
      </tr>
      <tr>
        <td><strong>Controller</strong> and <strong>View</strong> exist with the one-to-many relationship. One Controller can select a different View based upon required operation.</td>
        <td>The one-to-one relationship exists between <strong>Presenter</strong> and <strong>View</strong> as one Presenter class manages one View at a time.</td>
        <td>Multiple <strong>View</strong> can be mapped with a single <strong>ViewModel</strong> and thus, the one-to-many relationship exists between View and ViewModel.</td>
      </tr>
      <tr>
        <td>The <strong>View</strong> has no knowledge about the<strong> Controller</strong>.</td>
        <td>The <strong>View</strong> has references to the <strong>Presenter</strong>.</td>
        <td>The <strong>View</strong> has references to the <strong>ViewModel</strong></td>
      </tr>
      <tr>
        <td>Difficult to make changes and modify the app features as the code layers are tightly coupled.</td>
        <td>Code layers are loosely coupled and thus it is easy to carry out modifications/changes in the application code.</td>
        <td>Easy to make changes in the application. However, if <strong>data binding logic</strong> is too complex, it will be a little harder to debug the application.</td>
      </tr>
      <tr>
        <td>User Inputs are handled by the <strong>Controller</strong>.</td>
        <td>The <strong>View</strong> is the entry point to the Application</td>
        <td>The <strong>View</strong> takes the input from the user and acts as the entry point of the application.</td>
      </tr>
      <tr>
        <td>Ideal for small scale projects only.</td>
        <td>Ideal for simple and complex applications.</td>
        <td>Not ideal for small scale projects.</td>
      </tr>
      <tr>
        <td>Limited support to <strong>Unit testing</strong>.</td>
        <td>Easy to carry out <strong>Unit testing</strong> but a tight bond of View and Presenter can make it slightly difficult.</td>
        <td><strong>Unit testability</strong> is highest in this architecture.</td>
      </tr>
      <tr>
        <td>This architecture has a high dependency on Android APIs.&nbsp;</td>
        <td>It has a low dependency on the Android APIs.&nbsp;</td>
        <td>Has low or no dependency on the Android APIs.</td>
      </tr>
      <tr>
        <td>It does not follow the modular and single responsibility principle.</td>
        <td>Follows modular and single responsibility principle.</td>
        <td>Follows modular and single responsibility principle.</td>
      </tr>
    </tbody>
  </table>



<br>

# MVC, MVP, MVVM: Which One to Choose?

AAuthor: Rosa Tiara Galuh

Date: 2022-08-11

[Original](https://www.makeuseof.com/mvc-mvp-mvvm-which-choose/)


- Architectural pattern
  - clarifying and defining some crucial components of a software architecture
  - an image of a system, not an architecture
  - a general and reusable solution to a commonly occurring problem in software architecture in a certain context


- Design pattern
  - a formalized best practice used to solve common problems when designing an application or system


- Difference b/w architectural and design patterns
  - pattern in software: a recurrent property to break down a huge and complex structure into smaller, simpler components
  - using to craft a general solution for a class of problems
  - using different tools in each level of software development
    - smaller levels: design patterns
    - larger levels: architectural patterns
    - [programming paradigms](https://www.makeuseof.com/programming-paradigms-major/) at the implementation level


- Architectural design patterns
  - solving common problems
  - benefits
    - split complex tasks into simpler tasks
    - reduce bugs
    - produce testable and maintainable code


- Model terminologies
  - Model:
    - storing data and communicates directly with the database
    - representing data and application logic
    - defining the business rules that manage data handling, modification, or processing
  - View
    - displaying the model's data
    - responsible for the data’s representation in the user interface
  - ViewModel
    - exclusive to MVVM pattern
    - an abstraction of the view layer and also acts as a wrapper for the model data
  - Controller: integrateing the view and model
  - Presenter
    - a component that only exists in the MVP model
    - retrieving the input from the view component
    - processing the data with the help of the model



