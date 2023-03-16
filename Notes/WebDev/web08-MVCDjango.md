# Understanding the MVC patter in Django

Author: Ada Nduka Oyom

Date: 2017-07-19

[Original](https://medium.com/shecodeafrica/understanding-the-mvc-pattern-in-django-edda05b9f43f)


- MVC pattern overview
  - a software architecture pattern
  - separating data presentation from the logic of handling user interactions
  - one of the best ways to create client-server applications


- MVC components
  - **Model**:
    - handling data representation
    - serving as an interface to the data stored in the database itself
    - allowing to interact with data
    - w/o having to get perturbed with all the complexities of the underlying database
  - **View**:
    - representing what user see on user's browser for a web application or in the UI for a desktop application
  - **Controller**:
    - providing the logic to
      - handle presentation flow in the view
      - update the model’s data
    - using programmed logic to figure out what is pulled from the database through the model
    - passing to the view
    - getting information from the user through the view
    - implementing the given logic by either changing the view or updating the data via the model


- Django design pattern
  - embracing the popular **Model—View—Controller** pattern with a new twist
  - using it’s own logic in the implementation, **Model-Template-View** (MTV) pattern
  - also referred to as the **Model-Template-View + Controller**
  - **Model**:
    - same as the Model explanation in the MVC pattern
    - taking the same position as the interface or relationship between the data
    - containing everything related to data access and validation
  - **Template**:
    - related to the View in the MVC pattern
    - the presentation layer
    - handling the presentation logic in the framework
    - controling what should be displayed and how it should be displayed to the user
  - **View**:
    - related to the Controller in the MVC pattern
    - handling all the business logic that throws down back to the respective templates
    - serving as the bridge between the model and the template
  - pattern diagram

    <figure style="display: table; margin: auto; text-align: center;"">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
        onclick= "window.open('https://medium.com/shecodeafrica/understanding-the-mvc-pattern-in-django-edda05b9f43f')"
        src    = "https://miro.medium.com/max/786/1*pHlF3KufWwX7svv4Mv4Frg.jpeg"
        alt    = "MVC vs MTV"
        title  = "MVC vs MTV"
      />
    </figure>



