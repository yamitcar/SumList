## Get Started

Prerequisites:

* Python >= 3.11

Initialize a python virtual environment:

```bash
python3 -m venv venv
source ./venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Utils
 create requirements file:
 
```bash
pip freeze > requirements. txt
```

For run the app:

```bash
python3 app.py
```
then enter the input (example):
```bash
    1,9,5,0,20,-4,12,16,7 12
```

also you can use the input.txt file

edit the file as your convenience, and then run:

```bash
python3 app.py < huge-input.txt
```

## Design considerations:

The project structure is based on a hexagonal Architecture

there are 2 folders
    - adapters, with the UI to handle the command line interfaces, and its respective parsing to pass the information to a port
    - ports, with 1 business class, based on a command pattern (and following a duck typing style without interfaces)
        - each method here has its own responsibility and have only one "public" method 

- on the test folders you will find the unit test for the PORTS based on the business cases

### Assumptions:
    
- all the input contains numbers, I didn't put focus on border cases, like wrong inputs, or bad formats


Some pending improvements, (because lack of time):

    - include tests for the adapter class
    - possible refactor, avoid delete elements from the array and move thougth it based on on the indexes, and move the index pointers instead. that could improve enven more the complexity metric