# Web Modeling

## Overview


- [Key differences b/w MVC and MVVM](../Notes/web07-ModelComp.md#summary)
  - **MVC framework:** an architectural pattern that separates an application into three main logical components Model, View, and Controller
  - **MVVM framework:** facilitating a separation of development of the graphical user interface with the help of mark-up language or GUI code
  - controller in MVC: the entry point to the Application
  - View in MVVM: the entry point to the Application
  - MVC Model component: tested separately from the user
  - MVVM model: easy for separate unit testing, and code in event-driven
  - "one to many" relationships
    - MVC:  b/w Controller & View
    - MVVM: b/w View & View Model


- [Comparisons of MVC and MVVM](../Notes/web07-ModelComp.md#difference-between-mvc-and-mvvm-architecture)

  <table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 60vw;" cellspacing=0 cellpadding=5 border=1 align="center">
    <colgroup>
      <col style="width: 20%">
      <col style="width: 20%">
      <col style="width: 20%">
    </colgroup>
    <thead>
    <tr style="font-size: 1.0em; vertical-align:middle;">
      <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;">Feature</th>
      <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;">MVC (Model View Controller)</th>
      <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff;">MVVM (Model View ViewModel)</th>
    </tr>
    </thead>
    <tbody> 
      <tr>
        <td>Entry point to the Application</td> <td>Controller</td> <td>View</td>
      </tr>
      <tr>
        <td>One to many relationships</td> <td>Controller &amp; View</td> <td>View &amp; View Model</td>
      </tr>
      <tr>
        <td>View reference</td> <td>not to the Controller</td> <td>to the View-Model</td>
      </tr>
      <tr>
        <td>Age</td> <td>old Model</td> <td>relatively New Model</td>
      </tr>
      <tr>
        <td>Disadvantages</td> <td>read, change, to unit test, and reuse</td> <td>complicated debugging process w/ complex data bindings</td>
      </tr>
      <tr>
        <td>Testing</td> <td>component tested separately from the user</td> <td>separate unit testing and event-driven code</td>
      </tr>
    </tbody>
  </table>







## Model-View-Controller (MVC) Pattern

- [Model–view–controller (MVC) overview](../Notes/web05-WebModel.md#model-view-controller-mvc)
  - a software architectural pattern commonly used for developing user interfaces
  - dividing the related program logic into three interconnected elements
  - traditionally used for desktop graphical user interfaces (GUIs)
  - popular for designing web applications
  - diagram of MVC pattern

  <figure style="display: table; margin: auto; text-align: center;"">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
      onclick= "window.open('https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller')"
      src    = "https://upload.wikimedia.org/wikipedia/commons/a/a0/MVC-Process.svg"
      alt    = "Diagram of interactions within one possible take on the MVC pattern"
      title  = "Diagram of interactions within one possible take on the MVC pattern"
    />
    <figcaption>
      Diagram of interactions within one possible take on the MVC pattern
    </figcaption>
  </figure>


- [The Model-View-Controller (MVC) pattern](../Notes/web07-ModelComp.md#difference-between-mvc-mvp-and-mvvm-architecture-pattern-in-android)
  - splitting the code into 3 components
  - creating the class/file of the application
  - **Model:**
    - storing the application data
    - w/o knowledge about the interface
    - responsible for handling the domain logic (real-world business rules)
    - communication with the database and network layers
  - **View:**
    - the UI (User Interface) layer
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
      alt    = "The Model-View-Controller(MVC) Pattern"
      title  = "The Model-View-Controller(MVC) Pattern"
    />
  </figure>

- [Components of MVC](../Notes/web05-WebModel.md#model-view-controller-mvc)
  - **Model**
    - central component of the pattern
    - application's dynamic data structure
    - independent of the user interface
    - typically represents a table in the application's database
  - **View**
    - any representation of information such as a chart, diagram or table
    - multiple views of the same information, such as a bar chart for management and a tabular view for accountants
    - played by HTML templates
    - a view specifying an in-browser user interface rather than representing a user interface widget directly
    - Django called as a "template"
  - **Controller**
    - accepting input and converting it to commands for the model or view
    - mediating between the views and the models
    - one controller per application, or one controller per window
    - Django
      - called a "view" instead of a controller
      - a function that receives a web request and returns a web response
      - using templates to create the response


- [Interactions of MVC components](../Notes/web05-WebModel.md#model-view-controller-mvc)
  - model: 
    - responsible for managing the data of the application
    - receiving user input from the controller
  - view: rendering presentation of the model in a particular format
  - controller:
    - responding to the user input and performs interactions on the data model objects
    - receiving the input
    - optionally validating input
    - passing the input to the model


- [Diagram of MVC software architecture](../Notes/web06-MVCOverview.md)

  <figure style="display: table; margin: auto; text-align: center;"">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
      onclick= "window.open('https://www.patricksoftwareblog.com/overview-of-model-view-controller-mvc/')"
      src    = "https://i0.wp.com/www.patricksoftwareblog.com/wp-content/uploads/2015/07/Model-View-Controller-High-Level-Diagram.png?"
      alt    = "a high-level diagram of the MVC software architecture"
      title  = "a high-level diagram of the MVC software architecture"
    />
  </figure>


- [Components of MVC pattern](../Notes/web06-MVCOverview.md)
  - **View**
    - providing the interaction that the user sees (typically, a web page).  The view components 
    - providING data to the user and send actions to the Controller for manipulating data
  - **Model** – defining the data for the application (typically, the data is stored in a database)
  - **Controller** – basically, providING the interface between the View and the Model


- [MVC architecture](../Notes/web07-ModelComp.md#mvc-pattern)
  - an architectural pattern that separates an application into three main logical components, Model, View, and Controller
  - a component built to handle specific development aspects of an application
  - separating the business logic and presentation layer from each other
  - mainly used for desktop graphical user interfaces (GUIs)
  - components
    - Model: including all the data and its related logic
    - View: presenting data to the user or handling user interaction
    - Controller: interface b/w Model and View components


- [Model component](../Notes/web07-ModelComp.md#mvc-pattern)
  - storing data and related logic
  - representing data being transferred between controller components or any other related business logic
  - example: 
    - a Controller object retrieving the customer info from the database
    - Model: manipulate data and send it back to the database or use it to render the same data


- [View component](../Notes/web07-ModelComp.md#mvc-pattern)
  - part of the Application that represents the presentation of data
  - created by the data gathered from the model data
  - requesting the Model to give information so that it resents the output to the user
  - representing the data from charts, diagrams, and table
  - example: any customer view will include all the UI components like text boxes, dropdowns, etc.


- [Controller component](../Notes/web07-ModelComp.md#mvc-pattern)
  - part of the Application that handles the user interaction
  - interpreting the mouse and keyboard inputs from the user, informing the Model and the View to change as appropriate
  - sending commands to the Model to update its state, e.g., saving a specific document
  - sending commands to its associated view to change the View’s presentation, e.g., scrolling a particular document


- [Features of MVC](../Notes/web07-ModelComp.md#mvc-pattern)
  - easy and frictionless testability
  - highly testable, extensible and pluggable framework
  - leveraging existing features offered by ASP.NET, Django, JSP, etc
  - offering full control over your HTML as well as your URLs
  - supporting Test Driven Development (TDD)
  - offering separation of logic
  - allowing routing for SEO Friendly URLs
  - offering to map for comprehensible and searchable URLs


- [Advantages of MVC](../Notes/web07-ModelComp.md#mvc-pattern)
  - easier support for a new type of clients
  - able to be developed parallely
  - avoiding complexity by dividing an application into separate (MVC) units
  - using a front controller pattern that processes web application requests using a single controller
  - offering the best support for test-driven development
  - working well for Web apps, which are supported by large teams of web designers and developers
  - providing a clean separation of concerns (SoC)
  - all classed and objects independent of each other $\implies$ test separately
  - allowing logical grouping of related actions on a controller together


- [Disadvantages of MVC](../Notes/web07-ModelComp.md#mvc-pattern)
  - business logic mixed with Ul
  - hard to reuse and implement tests
  - no formal validation support
  - increased complexity and inefficiency of data
  - the difficulty of using MVC with the modern user interface
  - a need for multiple programmers to conduct parallel programming
  - knowledge of multiple technologies is required


- [Model-View-Controller pattern](../Notes/web07-ModelComp.md#mvc-mvp-mvvm-which-one-to-choose)
  - first and popular in the field of web applications
  - building an application around Separation of Concerns (SoC)
    - reducing the code size
    - making clean and manageable code
  - easing the effort to test, maintain, and develop application
  - no understanding of the view or the controller
  - observer receiving an alert whenever there's a change in the view and controller
  - controller helping the routing process to connect the model to the relevant view
  - advantages
    - separation of concerns (more focused)
    - making it easier to test and manage the code
    - promoting decoupling of the application's layers
    - better code organization and reusability



## Model-View-Presenter (MVP) Pattern

- [Model-View-Presenter (MVP) overview](../Notes/web05-WebModel.md#model-view-presenter-mvp)
  - derivation of the model–view–controller (MVC) architectural pattern
  - used mostly for building user interfaces
  - a user interface architectural pattern engineered to facilitate automated unit testing
  - improving the separation of concerns in presentation logic
  - diagram of MVP pattern

  <figure style="display: table; margin: auto; text-align: center;"">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
      onclick= "window.open('https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter')"
      src    = "https://upload.wikimedia.org/wikipedia/commons/d/dc/Model_View_Presenter_GUI_Design_Pattern.png"
      alt    = "Diagram that depicts the Model View Presenter (MVP) GUI design pattern"
      title  = "Diagram that depicts the Model View Presenter (MVP) GUI design pattern"
    />
    <figcaption>
      Diagram that depicts the Model View Presenter (MVP) GUI design pattern.
    </figcaption>
  </figure>


- [Components of MVP pattern](../Notes/web05-WebModel.md#model-view-presenter-mvp)
  - Model: an interface defining the data to be displayed or otherwise acted upon in the user interface
  - View:
    - a passive interface that displays data (the model) and routes user commands (events) to the presenter to act upon that data
    - instantiating the concrete presenter object
    - providing a reference to itself
  - Presenter
    - acting upon the model and the view
    - retrieving data from repositories (the model)
    - formating it for display in the view


- [Model-View-Presenter pattern](../Notes/web07-ModelComp.md#mvc-mvp-mvvm-which-one-to-choose)
  - sharing two components with MVC: model and view
  - replacing the controller with the presenter
  - allowing user to mock the view more easily
  - presenter:
    - used to present something
    - w/ the functionality of the "middle-man"
    - all presentation logic pushed to it
    - workflow
      - receiving input from the user via the view
      - processing the user’s actions with the help of the model
      - passing the results back to the view
    - communicating with the view through interfaces
  - view and presenter:
    - independent of one another
    - interacting via an interface


## Model-View-ViewModel (MVVM) Pattern

- [Model–view–viewmodel (MVVM) Overview](../Notes/web05-WebModel.md#modelviewviewmodel-mvvm)
  - an architectural pattern in computer software
  - facilitating the separation of the development of the graphical user interface (GUI; the view)
  - via a markup language or GUI code
  - the development of the business logic or back-end logic (the model) such that the view is not dependent upon any specific model platform
  - viewmodel
    - a value converter
    - responsible for exposing (converting) the data objects from the model in such a way they can be easily managed and presented
    - more model than view
    - handling most (if not all) of the view's display logic
    - implement a mediator pattern, organizing access to the back-end logic around the set of use cases supported by the view
  - a variation of Martin Fowler's Presentation Model design pattern
  - invented by Microsoft architects specifically to simplify event-driven programming of user interfaces
  - incorporated into the Windows Presentation Foundation (WPF) and Silverlight
  - a.k.a. model–view–binder

  <figure style="display: table; margin: auto; text-align: center;"">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
      onclick= "window.open('https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel')"
      src    = "https://upload.wikimedia.org/wikipedia/commons/8/87/MVVMPattern.png"
      alt    = "Diagram of MVVM pattern"
      title  = "Diagram of MVVM pattern"
    />
  </figure>


- [Components of MVVM pattern](../Notes/web05-WebModel.md#modelviewviewmodel-mvvm)
  - Model
    - domain model: real state content (an object-oriented approach)
    - data access layer: content (a data-centric approach)
  - View
    - the structure, layout, and appearance of what a user sees on the screen
    - same as the model–view–controller (MVC) and model–view–presenter (MVP) patterns
    - displaying a representation of the model
    - receiving the user's interaction with the view
    - forwarding the handling of these to the view model via the data binding (properties, event callbacks, etc.)
  - View model
    - an abstraction of the view exposing public properties and commands
    - binder:
      - automating communication between the view
      - bound properties in the view model
    - a state of the data in the model
    - Presenter in the MVP pattern: a reference to a view, whereas the view model does not
    - directly binding to properties on the view model to send and receive updates
    - requiring a binding technology
    - generating boilerplate code to do the binding
  - Binder
    - declarative data and command-binding
    - implicit
    - freeing the developer from being obliged to write boiler-plate logic to synchronize the view model and view
    - the presence of a declarative data binding technology enabling the pattern
    - using MVP or MVC w/o binder


- [MVVM architecture](../Notes/web07-ModelComp.md#mvvm-pattern)
  - facilitating a separation of development of the graphical user interface with the help of mark-up language or GUI code
  - view model: a value converter that means that it is view model’s responsibility for exposing the data objects from the Model in such a way that objects are easily managed and presented
  - offerring two-way data binding between view and view-model
  - automating the propagation of modifications inside View-Model to the view
  - view-model: making use of observer pattern to make changes in the view-model


- [Model component](../Notes/web07-ModelComp.md#mvvm-pattern)
  - storing data and related logic
  - representing data being transferred between controller components or any other related business logic
  - example
    - a Controller object will retrieve the student info from the school database
    - Model: manipulate data and send it back to the database or use it to render the same data


- [View component](../Notes/web07-ModelComp.md#mvvm-pattern)
  - UI components like HTML, CSS, jQuery, etc. 
  - held responsible for displaying the data which is received from the Controller as an outcome
  - also transformed Model(s) into the User Interface (UI)


- [View Model component](../Notes/web07-ModelComp.md#mvvm-pattern)
  - responsible for presenting functions, commands, methods, to support the state of the View
  - accountable to operate the model and activate the events in the View


- [Features of MVVM](../Notes/web07-ModelComp.md#mvvm-pattern)
  - written for desktop application with data binding capabilities – XAML and the INotifyPropertyChanged interface
  - doing modification in the View-Model $\implies$ the View-Model using an observer pattern
  - mostly used by [WPF](https://www.guru99.com/sap-bods-tutorial.html), Silverlight, nRoute, etc.


- [Advantages of MVVM](../Notes/web07-ModelComp.md#mvvm-pattern)
  - business logic decoupled from UI
  - easy to maintain and test
  - easy to reuse components
  - loosely coupled architecture: making application architecture as loosely coupled
  - writing unit test cases for both the viewmodel and Model layer w/o the need to reference the View


- [Disadvantages of MVVM](../Notes/web07-ModelComp.md#mvvm-pattern)
  - maintenance of lots of codes in controller
  - some people think that for simple UIs of MVVM architecture can be overkill
  - not offering tight coupling between the view and view model


- [Model-View-ViewModel pattern](../Notes/web07-ModelComp.md#mvc-mvp-mvvm-which-one-to-choose)
  - the modern evolution of MVC
  - main goal: providing a clear separation between the domain logic and presentation layer
  - Supporting two-way data binding between the view and viewmodel
  - allowing to separate Code’s view and model
  - model changes $\iff$ view remaining the same
  - viewmodel: doing unit testing and testing logic behavior without involving the view




## Model-Template-View (MTV) Pattern




