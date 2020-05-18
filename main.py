class survey:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def addQuestion(self, question):
        if len(self.questions) < 10:
            self.questions.append(question)
            return "Successfully added the question to the survey"
        else:
            return "Reached limit of questions for this survey"


class controller:
    def __init__(self):
        self.surveys = []

    def createSurvey(self, name):
        self.surveys.append(survey(name))
        return ("Survey '" + name + "' created successfully")

    def addQestionSurvey(self, name, question):
        for survey self.surveys:
            if survey.name == name:
                return survey.addQuestion(question)
            else:
                return "Survey not found, please check the name of the survey"
