# Airbnb Console - Introduction

Welcome to the Airbnb Console, the initial component of the Holberton School's Airbnb project. This console serves as the foundation for exploring essential concepts in higher-level programming. The overarching goal of the Airbnb project is to deploy a simplified version of the Airbnb website (HBnB) on our server. In this segment, we introduce a command interpreter designed to manage objects for the Airbnb (HBnB) website.

## Key Features of the Command Interpreter

Our Airbnb Console offers several functionalities:

- Creating new objects, such as users or places.
- Retrieving objects from various sources, including files and databases.
- Performing operations on objects, like counting and computing statistics.
- Updating attributes of objects.
- Deleting objects.

## Table of Contents
- [Environment](#environment)
- [Installation](#installation)
- [File Descriptions](#file-descriptions)
- [Usage](#usage)
- [Examples of Use](#examples-of-use)
- [Known Issues](#bugs)
- [Authors](#authors)
- [License](#license)

## Environment
This project has been tested and interpreted on Ubuntu 14.04 LTS using Python 3.4.3.

## Installation
To set up the Airbnb Console, follow these steps:

1. Clone this repository: `git clone "https://github.com/alexaorrico/AirBnB_clone.git"`
2. Navigate to the Airbnb directory: `cd AirBnB_clone`
3. Run the console interactively: `./console` and enter your desired commands.
4. Run the console non-interactively: `echo "<command>" | ./console.py`

## File Descriptions
- [console.py](console.py): The console contains the entry point of the command interpreter and supports the following commands:
  - `EOF`: Exits the console.
  - `quit`: Exits the console.
  - `<emptyline>`: Overwrites the default empty line method and does nothing.
  - `create`: Creates a new instance of `BaseModel`, saves it to the JSON file, and prints the ID.
  - `destroy`: Deletes an instance based on the class name and ID (saving the change to the JSON file).
  - `show`: Prints the string representation of an instance based on the class name and ID.
  - `all`: Prints the string representation of all instances based on the class name.
  - `update`: Updates an instance based on the class name and ID by adding or updating attributes (saving the change to the JSON file).

The `/models/` directory contains classes used in this project, including `BaseModel`, `Amenity`, `City`, `Place`, `Review`, `State`, and `User`.

The `/models/engine` directory contains the `FileStorage` class, which handles JSON serialization and deserialization.

The `/tests` directory includes all unit test cases for the project.

## Examples of Use
```bash
vagrantAirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel

(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9,28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9,28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit
Known Issues
No known bugs at this time.

## Bugs
No known bugs at this time. 

## Authors
Alexa Orrico - [Github](https://github.com/alexaorrico) / [Twitter](https://twitter.com/alexa_orrico)  
Jennifer Huang - [Github](https://github.com/jhuang10123) / [Twitter](https://twitter.com/earthtojhuang)


## Editors
Maria Mothiba - [Youtube](https://www.youtube.com/@OVERTIMECODING)
Phumlani Mabophe - [Youtube](https://www.youtube.com/@OVERTIMECODING)

Second part of Airbnb: Joann Vuong
## License
Public Domain. No copy write protection. 