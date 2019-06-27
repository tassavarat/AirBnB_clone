![alt text](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20190627%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190627T162017Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=716fddf7f4b8819f05f332dcf22cea347c8c1dd8dc85118381a7baacc09902cd)

# AirBnB_clone
* This repository contains a full-stack clone of AirBnB divided into 6 parts:
  * Console
    * Creation of data model
    * Management (create, update, destroy, etc.) of objects via command interpreter
    * Storage and persistence of objects (JSON format)
  * Web static
    * HTML/CSS
    * Templates of each object
  * MySQL storage
    * Replacement of file storage with database storage
    * Using O.R.M. to map models
  * Web framework - templating
    * Deployment of web server in Python
    * Dynamic HTML elements using objects stored in database
  * RESTful API
    * JSON web interface to display all objects
    * Manipulation of objects via a RESTul API
  * Web dynamic
    * JQuery
    * Loading of objects from client side using RESTful API

Example of final product:
<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/8-index.png">
</p>

# Techstack
* Python 3
  * Flask
* MySQL
* Javascript
* HTML
![alt text](https://imgur.com/a/kS1SOl4)

# Usage

The console works in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

The console also works in non-interactive mode:
```sh
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

# Authors
* __Tu Vo__
* __Tim Assavarat__
