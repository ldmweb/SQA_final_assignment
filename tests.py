from main import controller


def test_initializeController():
    MyController = controller()
    assert len(MyController.surveys) == 0


def test_createSurvey():
    MyController = controller()
    assert len(MyController.surveys) == 0
    assert MyController.createSurvey(
        "My new survey") == "Survey 'My new survey' created successfully"
    assert len(MyController.surveys) == 1
    assert MyController.surveys[0].name == "My new survey"


def test_addQuestionSurvey():
    MyController = controller()
    MyController.createSurvey("My new survey")
    assert len(MyController.surveys[0].questions) == 0
    assert MyController.addQestionSurvey(
        "My wrong survey", "My new question") == "Survey not found, please check the name of the survey"
    assert MyController.addQestionSurvey(
        "My new survey", "My new question") == "Successfully added the question to the survey"
    assert len(MyController.surveys[0].questions) == 1
    assert MyController.surveys[0].questions[0] == "My new question"
    assert MyController.addQestionSurvey(
        "My new survey", "My new question") == "This question already exist in the survey"
    assert len(MyController.surveys[0].questions) == 1
    MyController.addQestionSurvey("My new survey", "My new question 1")
    MyController.addQestionSurvey("My new survey", "My new question 2")
    MyController.addQestionSurvey("My new survey", "My new question 3")
    MyController.addQestionSurvey("My new survey", "My new question 4")
    MyController.addQestionSurvey("My new survey", "My new question 5")
    MyController.addQestionSurvey("My new survey", "My new question 6")
    MyController.addQestionSurvey("My new survey", "My new question 7")
    MyController.addQestionSurvey("My new survey", "My new question 8")
    MyController.addQestionSurvey("My new survey", "My new question 9")
    assert len(MyController.surveys[0].questions) == 10
    assert MyController.addQestionSurvey(
        "My new survey", "My new question 10") == "Reached limit of questions for this survey"


def test_addResponseSurvey():
    MyController = controller()
    MyController.createSurvey("My new survey")
    assert len(MyController.surveys) == 1
    MyController.addQestionSurvey("My new survey", "My new question 1")
    MyController.addQestionSurvey("My new survey", "My new question 2")
    MyController.addQestionSurvey("My new survey", "My new question 3")
    MyController.addQestionSurvey("My new survey", "My new question 4")
    assert len(MyController.surveys[0].questions) == 4
    assert MyController.addResponseSurvey(
        "My wrong survey", [1, 2, 5, 3]) == "Survey not found, please check the name of the survey"
    assert MyController.addResponseSurvey(
        "My new survey", [1, 2, 5, 3]) == "Answers successfully registered for this survey"
    assert len(MyController.surveys[0].responses) == 1
    assert len(MyController.surveys[0].responses[0].answers) == 4
    MyController.addResponseSurvey(
        "My new survey", [1, 2, 5, 3])
    assert len(MyController.surveys[0].responses) == 2
    assert len(MyController.surveys[0].responses[1].answers) == 4
    assert MyController.surveys[0].responses[1].answers[2] == 5
    assert MyController.addResponseSurvey(
        "My new survey", [1, 2, 5, 3, 1]) == "The number of answers must be equal with the number of questions in this survey. This survey contain 4 questions"
    assert MyController.addResponseSurvey(
        "My new survey", [1, 7, 5, 3]) == "All your answer must be a number between 1 and 5"
    assert len(MyController.surveys[0].responses) == 2


def test_getAllSurveys():
    MyController = controller()
    assert MyController.getAllSurveys() == "No surveys created for the moment"
    MyController.createSurvey("My new survey")
    surveys = MyController.getAllSurveys()
    assert surveys[0] == MyController.surveys[0]
    assert len(MyController.surveys) == 1
    MyController.createSurvey("My new survey 2")
    MyController.createSurvey("My new survey 3")
    surveys = MyController.getAllSurveys()
    assert surveys[0] == MyController.surveys[0]
    assert surveys[1] == MyController.surveys[1]
    assert surveys[2] == MyController.surveys[2]
    assert len(MyController.surveys) == 3
