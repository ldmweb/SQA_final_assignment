# Software Quality Assurance Final Assignment

## Demonstrating Software Quality

### **Introduction**

When developing and implementing a software project, It is capital to have a concrete Software Quality management plan including a quality assurance aspect for the project to be successfully developed, implemented and maintained.

The objective of quality assurance is to improve software development and maintenance processes, in order to easier spot weaknesses and errors in the project. Done properly, it allows to reduce the risks of critical bugs and improve the overall quality

This repository is an example software project that demonstrates some of the best practices of Software quality assurance that can be adopted during the development of a project.

You will find a software sample component in **python** for storing information about surveys and responses. Each Survey is made up of multiple Questions (up to a maximum of 10). And should contain an answer to each Question in its Survey, where the answer will be an integer value between 1 and 5

The documentation of the sample code is described in the [**DOC.md**](./DOC.md) file of the the repository.

This file also covers the following themes :

- [**Sprint backlog and task estimation**](#sprint-backlog-and-task-estimation)

  - [task estimation](#task-estimation)
  - [How to chose estimates](#how-to-chose-estimates)
  - [Velocity metric](#velocity-metric)

- [**Unit testing and Test-Driven development**](#unit-testing-and-test-driven-development)

- [**Test coverage metric**](#test-coverage-metric)

- [**Team version-control**](#team-version-control)

- [**Code-review checklist**](#code-review-checklist)

---

### **Sprint backlog and task estimation**

Before starting the development of a project, it is important to estimate de time needed to develop each tasks of the project in order to correctly split the work between the group members.

Here is the different tasks of our sample project, each part must include a testing part to check for errors in the code that execute the task. Estimated time include test implementation.

#### Task estimation

1. **Project ideation** : Imagining the infrastructure of it with the different classes, methods and variables necessary for the project to run correctly. - **Estimated time : 3 hours**

2. **Project base** : provide the fundation of the project with the file structure, the classes and the implementation of the testing tool and the coverage metric tool - **Estimated time : 1 hours**

3. **creates a new Survey** : method allowing to create a new survey. - **Estimated time : 40 minutes**

4. **add a question to a survey** : method allowing to add a question to a survey by providing the name of the survey and the question. Each survey will contain 10 questions maximum. - **Estimated time : 1 hour 30 minutes**

5. **add a response to a survey** : method allowing to add a response to a survey by providing the name of the survey an array of answers. Each answer must be an integer value between 1 and 5. - **Estimated time : 1 hour 30 minutes**

6. **get all surveys** : method allowing to get a list of all the surveys created. - **Estimated time : 15 minutes**

7. **get a specific survey by name** : method allowing to get a specific survey created by providing its name. - **Estimated time : 25 minutes**

8. **get all responses of a Survey** : method allowing to get a list of all the responses associated with a specific survey by providing its name. - **Estimated time : 15 minutes**

9. **get summary calculations for a Survey** : method allowing to get all the statistics of a specific survey including the average, standard deviation, minimum and maximum score of it. - **Estimated time : 1 hour**

10. **get summary calculations for a question of a survey** : method allowing to get all the statistics of a specific question of a survey including the average, standard deviation, minimum and maximum score of it. - **Estimated time : 1 hour 10 minutes**

**Sprint 1 :** tasks 1 to 4 - **Estimated time : 6 hours 10 minutes**

**Sprint 2 :** tasks 5 to 10 - **Estimated time : 4 hours 35 minutes**

#### how to chose estimates

The estimation of the time needed to develop a task can be done with any measuring unit as long as estimations are coherent between the tasks. for these sample project, we have used time in hours and minutes to be clear and simple but we could use levels of difficulty (0 being easy to develop and 5 being very difficult to develop for example) or even number of coffee drunk.

In this sample project, task number 5 : **add a response to a survey** is estimated at 1 hour and 30 minutes of work. This task needs to develop a method that will take arguments and create variables and objects. It is so obvious that it takes more time than the task number 8 : **get all responses of a Survey** estimated at 15 minutes because this method only needs to return an object and don't need to manage other variables. Usually, setter methods are longer to develop than getter methods. It does not apply to tasks 9 and 10 as they need mathematical calculations in order to provide the correct return value. They are so estimated at 1 hour or more. **Project ideation** is the task that takes the more time in the project, as it is the base of the project, it is important to spend a good amount of time to imagine a solid structure for the project. The more the structure is correctly thought, the fewer time developers will lose during development as they can only focus on building features.

It is also important to include in the estimation, the time needed to implement the tests of the task.

#### Velocity metric

To judge the efficiency of development of a team during a sprint, we can use the velocity metric. It can be measured using the same unit than the estimation of the tasks.

In this sample project, the total tasks in the product backlog are estimated at 10 hours and 45 minutes of work. Let's imagine that in the first sprint we chose to do the first 7 tasks. Our sprint is so estimated at 8 hours and 20 minutes hours of work. At the end of the sprint, we can calculate the team velocity, which is the amount of work the team succeed to develop in the sprint compared to the estimated amount of work of the sprint.

If the team succeed to develop only 6 tasks on the 7 planned, it has a sprint velocity of 7 hours and 55 minutes compared to the 8 hours and 20 minutes estimated of the sprint. Task 7 will so be postponed to the next sprint, and the estimation of tasks can be adjusted if necessary.

after a few sprints, you can get an average velocity for the team and can better split the work according to the team velocity to be sure that they can develop all tasks assigned. It can also be used to forecast how much time the project can be done.

If the velocity tends to drop, it can be a sign that part of the efficiency in the team gets lower, and it can be adjusted in the next sprint.

Velocity metric is an excellent tool to monitor the capabilities of the development team and to keep the development efficient during all the project building.

---

### **Unit testing and Test-Driven development**

Testing is capital when developing a software project. A project free from errors is more valuable and allows maintainability over time. Testing is checking differences between expected and actual results required in order to correct them.

It is so capital to provide tests for each part of the code. In this sample project, tests are provided to test each feature correctly.

Tests also allow ensure that the code previously developed does not change of comportment after a new implementation by another team member.

In this sample project, we use the python framework **py.test** to execute a series of unit test on each of our features

**pytest** is a framework that makes building simple and scalable tests easy

You can find how to launch the tests series in the documentation of the sample code : [**DOC.md**](./DOC.md)

---

### **Test Coverage Metric**

When implementing tests, it is capital that your test covers the integrality of your code. Which mean that all the code written should be tested by the test framework.

In order to verify this, we can use a test coverage metric to see how much percentage of your code is tested. And if it's not 100% you must adjust your tests series in order to take into account all the code.

In this sample project, we use the test coverage tool **coverage.py** to check how much of our code is covered by our **py.test** series

You can find how to launch the coverage metric and the result of it in the documentation of the sample code : [**DOC.md**](./DOC.md)

---

### **Team version-control**

When developing a project in teamwork, it is capital to organize in the team with a version control tool like **Git** to be able to develop in parallel different parts of the project. The most important is to not destroy the development of other members of the team while you develop your own part.

For this, it is important to have a clear gitflow process within the team so that everyone can develop its own part peacefully.

For this sample code project, we used the following gitflow process.

1. **Always keep your working tree up to date** with the development branch. The development branch regroups all the features ready for production that other team members could have developed already. So before starting writing new code, always pull last updates from the development branch by performing the following command :

```
    git pull origin development
```

2. Once your working tree up to date, if you want to start developing a new feature, create a new branch. Your new branch should contain the name of the feature you will develop for better clarity of the project by the other members of the team. Create a new branch by typing the following command :

```
    git checkout -b [new_branch_name]
```

3. Once on your new branch, you can start to develop your feature. After accomplishing a working section of code, you can create a commit and push the code to the feature_branch you are working on. To add the file that you have developed in the commit, type :

```
    git add [your_file(s)]
```

4. Then, commit your changes in the file(s), Before committing, don't forget to check if you are up to date with the working tree by pulling the development branch.
   Don't forget to provide a clear commit message indicating what changes you have brought to the file(s) and which feature/tasks it correspond to. To commit your file(s), just type :

```
    git commit -m "[your_commit_message]"
```

5. Finally, to push your changes on your feature_branch, just type :

```
    git push origin [feature_branch_name]
```

6. Once the feature you developed is done and tested, you can merge your feature_branch with the development branch to implement your work to the global project. To do so, perform a pull request on the dev branch from your feature_branch. The pull request will be reviewed by the project manager and accepted if all the requirement and tests are correct. You can then start a new feature in a new branch.

This following image is the result of the team version control for the sample code project :

PUT TEAM VERSION CONTROL IMAGE WHEN FINISH THE CODE

It is highly important that all the members of the team respect this gitflow process in order to develop separately the different part of the project without interfering with each other.

---

### **Code-review checklist**

Before validating a pull request, project manager or reviewer must check a list of things that needs to be present in the code in order to be validated.

For this sample project, here is the checklist of things that a reviewer should check when reviewing a Pull Request :

- [x] Code is fonctionnal
- [x] Code can be understood by all the team members
- [x] Code follow the coding style of the team
- [x] No duplicate code
- [x] No commented or debuging code
- [x] No unused code
- [x] Each code feature is documented in the [**DOC.md**](./DOC.md) file
- [x] Each third party framework and module used are documented in the [**DOC.md**](./DOC.md) file
- [x] Each code feature is tested / can be tested
- [x] Testing coverage of the code is 100%

You can find on [**this closed pull request**](https://github.com/ldmweb/SQA_final_assignment/pull/10#issue-419630885) an exemple of a validated review that validate all requested code-review checks.

---

**Lilian Desvaux de Marigny** - D19124161
