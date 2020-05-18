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
