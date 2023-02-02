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




