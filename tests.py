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
