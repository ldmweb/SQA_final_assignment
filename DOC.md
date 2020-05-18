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

2. `addQestionSurvey(self, name, question)` allow to add a question to a survey. 10 questions maximum per survey :

```
MyController.addQestionSurvey("My new survey", "My new question")
-> Successfully added the question to the survey
```

```
MyController.addQestionSurvey("My new survey", "My new question")
-> This question already exist in the survey
```

```
MyController.addQestionSurvey("My new survey", "My new question number 11")
-> Reached limit of questions for this survey
```

```
MyController.addQestionSurvey("My wrong survey", "My new question")
-> Survey not found, please check the name of the survey
```

3. `addResponseSurvey(self, name, answers)` allow to add a response to a survey containing the answers for each questions of the survey. The number of answers must be equal to the number of questions in the survey. The answers must be numbers between 1 and 5 formated in an array :

```
MyController.addResponseSurvey("My new survey", [1, 2, 5, 3])
-> Answers successfully registered for this survey
```

```
MyController.addResponseSurvey("My new survey", [1, 2, 5, 3, 1])
-> The number of answers must be equal with the number of questions in this survey. This survey contain number_of_survey_questions questions
```

```
MyController.addResponseSurvey("My new survey", [1, 7, 5, 3])
-> All your answers must be a number between 1 and 5
```

```
MyController.addResponseSurvey("My wrong survey", [1, 2, 5, 3])
-> Survey not found, please check the name of the survey
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

The `Missing` column represents the line number of the NOT tested code in the file

For a nicer presentation, and to get annotated HTML listings detailing missed lines, use the following command :

```
coverage html main.py
```

It will generate an HTML website that you can open by double-clicking on `index.html` located within the generated `htmlcov` folder.

PUT IMAGE RESULT WHEN FINISH DEV

---

Lilian Desvaux de Marigny - D19124161
