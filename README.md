<p align="center">
  <img src="http://www.holbertonschool.com/holberton-logo.png">
</p>
<p align="center">
  <img src="https://i.imgur.com/ogbfW3k.png">
</p>

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
<p align="center">
  <img src="https://i.imgur.com/lgZnZrz.png">
</p>

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
