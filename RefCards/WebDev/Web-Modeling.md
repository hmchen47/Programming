# Web Modeling

## Overview




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






## Model-View-Presenter (MVP) Pattern





## Model-View-ViewModel (MVVM) Pattern





## Model-Template-View (MTV) Pattern




