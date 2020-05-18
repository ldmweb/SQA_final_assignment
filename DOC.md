# Software Quality Assurance Final Assignment

## Sample Software code documentation

You will find in this file the technical documentation for the sample code project, including the following part :

- [**Code documentation**](#Code-documentation)
- [**Tests tool documentation**](#Tests-tool-documentation)
- [**Coverage tool documentation**](#coverage-tool-documentation)

---

### **Code documentation**

the different classes and methods of the project are listed here.

the `Main.py` file need the statistics python module in order to be launched. To install this module, run :

```
pip install -U statistics
```

To use the different methods, you must initialiaze the `controller()`class :

```
MyController = controller()
```

you can then use the different methods of the `controller()` class.

Here is the list of the methods available in the `controller()` class :

**1 - `createSurvey(name)`** allow to create a new survey by passing the survey name - **`string`** in parameters:

```
MyController.createSurvey("My new survey")
```

**Return** : `Survey 'name_of_the_new_survey' created successfully`

**2 - `addQestionSurvey(name, question)`** allow to add a question to a survey by passing the survey name - **`string`** and a new survey question - **`string`** in parameters. 10 questions maximum per survey :

```
MyController.addQestionSurvey("My new survey", "My new question")
```

**Return** : `Successfully added the question to the survey`

```
MyController.addQestionSurvey("My new survey", "My new question")
```

**Return** : `This question already exist in the survey`

```
MyController.addQestionSurvey("My new survey", "My new question number 11")
```

**Return** : `Reached limit of questions for this survey`

```
MyController.addQestionSurvey("My wrong survey", "My new question")
```

**Return** : `Survey not found, please check the name of the survey`

**3 - `addResponseSurvey(name, answers)`** allow to add a response to a survey containing the answers for each questions of the survey by passing the survey name - **`string`** and the answers for the survey - **`array Int`** in parameters. The number of answers must be equal to the number of questions in the survey. The answers must be numbers between 1 and 5 :

```
MyController.addResponseSurvey("My new survey", [1, 2, 5, 3])
```

**Return** : `Answers successfully registered for this survey`

```
MyController.addResponseSurvey("My new survey", [1, 2, 5, 3, 1, 2])
```

**Return** : `The number of answers must be equal with the number of questions in this survey. This survey contain number_of_survey_questions questions`

```
MyController.addResponseSurvey("My new survey", [1, 7, 5, 3])
```

**Return** : `All your answers must be a number between 1 and 5`

```
MyController.addResponseSurvey("My wrong survey", [1, 2, 5, 3])
```

**Return** : `Survey not found, please check the name of the survey`

**4 - `getAllSurveys()`** allow to get all the surveys created in the `MyController()` instance. If there is no survey created yet, an error message will be displayed. No parameters required :

```
MyController.getAllSurveys()
```

**Return** : `[surveys_list]`

**5 - `getSurvey()`** allow to get a specific survey created in the `MyController()` instance by passing the survey name - **`string`** in parameters. If there is no survey created yet, an error message will be displayed.

```
MyController.getSurvey("My new survey")
```

**Return** : `My_new_survey_object`

```
MyController.getSurvey("My wrong survey")
```

**Return** : `Survey not found, please check the name of the survey`

**6 - `getResponsesSurvey()`** allow to get the list of surveyResponses for a specific survey by passing the survey name - **`string`** in parameters. If there is no survey created yet, an error message will be displayed. If there is not responses registered yet for this survey, an error message will be displayed.

```
MyController.getResponsesSurvey("My new survey")
```

**Return** : `[My_new_survey_responses]`

```
MyController.getResponsesSurvey("My wrong survey")
```

**Return** : `Survey not found, please check the name of the survey`

**7 - `getSummarySurvey()`** allow to get all the statistics of the responses of a specific survey including the average, standard deviation, minimum and maximum score of it by passing the survey name - **`string`** in parameters. If there is no survey created yet, an error message will be displayed. If there is not responses registered yet for this survey, an error message will be displayed.

```
MyController.getSummarySurvey("My new survey")
```

**Return** : `{"average":`_average_score_of_the_answers_`, "std_dev":`_standard_dev_of_the_answers_`, "min":`_minimum_score_of_the_answers_`, "max":`_maximum_score_of_the_answers_`,}`

```
MyController.getSummarySurvey("My wrong survey")
```

**Return** : `Survey not found, please check the name of the survey`

**8 - `getSummaryQuestion()`** allow to get all the statistics of the responses of a specific question within a specific survey including the average, standard deviation, minimum and maximum score of it by passing the survey name - **`string`** and the question name - **`string`** in parameters. If there is no survey created yet, an error message will be displayed. If there is not responses registered yet for this survey, an error message will be displayed.

```
MyController.getSummaryQuestion("My new survey", My new question)
```

**Return** : `{"average":`_average_score_of_the_answers_`, "std_dev":`_standard_dev_of_the_answers_`, "min":`_minimum_score_of_the_answers_`, "max":`_maximum_score_of_the_answers_`,}`

```
MyController.getSummaryQuestion("My wrong survey", My new question)
```

**Return** : `Survey not found, please check the name of the survey`

```
MyController.getSummaryQuestion("My new survey", My wrong question)
```

**Return** : `Question not found, please check the name of the question`

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

To launch the test suite with full details, run the following command :

```
pytest tests.py -v
```

Here is the result of the test serie passed on the sample code :

![Result_test](https://i.imgur.com/YsVeE9Z.png)

As you can see, all of our feaure are tested

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

Here is the result of the coverage metric for the test serie passed on the sample code :

![Result_coverage](https://i.imgur.com/2k7LfIv.png)

As you can see, 100% of the lines of the code are tested.

The `Stmts` column represents the number of line in the file.

The `Miss` column represents the number of line not tested in the file.

The `Cover` column represents the percentage of code tested in the file

The `Missing` column represents the line number of the NOT tested code in the file

For a nicer presentation, and to get annotated HTML listings detailing missed lines, use the following command :

```
coverage html main.py
```

It will generate an HTML website that you can open by double-clicking on `index.html` located within the generated `htmlcov` folder :

![Result_coverage_HTML](https://i.imgur.com/R9mmTkX.png)

---

Lilian Desvaux de Marigny - D19124161
