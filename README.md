# Software Quality Assurance Final Assignment

## Demonstrating Software Quality

### **Introduction**

When developing and implementing a software project, It is capital to have a concrete Software Quality management plan including a quality assurance aspect for the project to be successfully developed, implemented and maintained.

The objective of quality assurance is to improve software development and maintenance processes, in order to easier spot weaknesses and errors in the project. Done properly, it allows to reduce the risks of critical bugs and improve the overall quality

This repository is an example software project that demonstrates some of the best practices of Software quality assurance that can be adopted during the development of a project.

You will find a software sample component in **python** for storing information about surveys and responses. Each Survey is made up of multiple Questions (up to a maximum of 10). And should contain an answer to each Question in its Survey, where the answer will be an integer value between 1 and 5

This repository also covers the following themes :

- [**Sprint backlog and task estimation**](#sprint-backlog-and-task-estimation)

- [**Unit testing and Test-Driven development**](#unit-testing-and-test-driven-development)

- [**Test coverage metric**](#test-coverage-metric)

- [**Team version-control**](#team-version-control)

- [**Code-review checklist**](#code-review-checklist)

---

### **Sprint backlog and task estimation**

Before starting the development of a project, it is important to estimate de time needed to develop each tasks of the project in order to correctly split the work between the group members.

Here is the different tasks of our sample project, each part must include a testing part to check for errors in the code that execute the task. Estimated time include test implementation.

#### Task estimation :

1 - **Project ideation** : provide the fundation of the project by imagining the infrastructure of it with the different classes, methods and variables necessary for the project to run correctly. - **Estimated time : 4 hours**

2 - **creates a new Survey** : method allowing to create a new survey. - **Estimated time : 40 minutes**

3 - **add a question to a survey** : method allowing to add a question to a survey by providing the name of the survey and the question. Each survey will contain 10 questions maximum. - **Estimated time : 1 hour 30 minutes**

4 - **add a response to a survey** : method allowing to add a response to a survey by providing the name of the survey and the question. Each survey's answer must be an integer value between 1 and 5. - **Estimated time : 1 hour 30 minutes**

5 - **get all surveys** : method allowing to get a list of all the surveys created. - **Estimated time : 15 minutes**

6 - **get a specific survey by name** : method allowing to get a specific survey created by providing its name. - **Estimated time : 25 minutes**

7 - **get all responses of a Survey** : method allowing to get a list of all the responses associated with a specific survey by providing its name. - **Estimated time : 15 minutes**

8 - **get summary calculations for a Survey** : method allowing to get all the statistics of a specific survey including the average, standard deviation, minimum and maximum score of it. - **Estimated time : 1 hour**

9 - **get summary calculations for a question of a survey** : method allowing to get all the statistics of a specific question of a survey including the average, standard deviation, minimum and maximum score of it. - **Estimated time : 1 hour 10 minutes**

---

Lilian Desvaux de Marigny - D19124161
