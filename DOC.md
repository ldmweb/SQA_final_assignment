# Software Quality Assurance Final Assignment

## Sample Software code documentation

You will find in this file the technical documentation for the sample code project, including the following part :

- [**Code documentation**](#Code-documentation)
- [**Tests tool documentation**](#Tests-tool-documentation)
- [**Coverage tool documentation**](#coverage-tool-documentation)

---

### **Code documentation**

the different classes and methods of the project are listed here.

To use the different methods, you must initialiaze the `controller()`class :

```
MyController = controller()
```

you can then use the different methods of the `controller()` class.

Here is the list of the methods available in the `controller()` class :

1. `createSurvey(self, name)` allow to create a new survey :

```
MyController.createSurvey("My new survey")
-> Survey 'name_of_the_new_survey' created successfully
```

```
pip install -U statistics
```

---

### **Tests tool documentation**

In this sample project, we use the python framework **py.test** to execute a series of unit test on each of our features

**pytest** is a framework that makes building simple and scalable tests easy

To install the pytest tool, run the following command :

```
pip install -U pytest
```

To check that you installed the correct version:

```
pytest --version
```

To launch the test suite, run the following command :

```
pytest tests.py
```

---

### **Coverage tool documentation**

In this sample project, we use the test coverage tool **coverage.py** to check how much of our code is covered by our **py.test** series

To install the coverage.py tool, run the following command :

```
pip install coverage
```

Use coverage run to run your test suite and gather data about the coverage metrics :

```
coverage run -m pytest tests.py
```

once the tests run, use the following command to report on the result of the coverage for our **main.py** file:

```
coverage report -m main.py
```

PUT IMAGE RESULT WHEN FINISH DEV

The `Stmts` column represents the number of line in the file.

The `Miss` column represents the number of line not tested in the file.

The `Cover` column represents the percentage of code tested in the file

The `Missing` column represents the percentage of code NOT tested in the file

For a nicer presentation, and to get annotated HTML listings detailing missed lines, use the following command :

```
coverage html main.py
```

It will generate an HTML website that you can open by double-clicking on `index.html` located within the generated `htmlcov` folder.

PUT IMAGE RESULT WHEN FINISH DEV

---

Lilian Desvaux de Marigny - D19124161
