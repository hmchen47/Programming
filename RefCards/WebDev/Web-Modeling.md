# Web Modeling

## Overview


- [Key differences b/w MVC and MVVM](../Notes/web07-ModelComp.md#mvc-vs-mvvm---difference-between-them)
  - **MVC framework:** an architectural pattern that separates an application into three main logical components Model, View, and Controller
  - **MVVM framework:** facilitating a separation of development of the graphical user interface with the help of mark-up language or GUI code
  - controller in MVC: the entry point to the Application
  - View in MVVM: the entry point to the Application
  - MVC Model component: tested separately from the user
  - MVVM model: easy for separate unit testing, and code in event-driven
  - "one to many" relationships
    - MVC:  b/w Controller & View
    - MVVM: b/w View & View Model




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






## Model-Template-View (MTV) Pattern




