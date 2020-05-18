class surveyResponse:
    def __init__(self):
        self.answers = []

    def addAnswers(self, answers):
        for answer in answers:
            if answer != 1 and answer != 2 and answer != 3 and answer != 4 and answer != 5:
                return "All your answer must be a number between 1 and 5"
        for answer in answers:
            self.answers.append(answer)


class survey:
    def __init__(self, name):
        self.name = name
        self.questions = []
        self.responses = []

    def addQuestion(self, question):
        if len(self.questions) < 10:
            for Question in self.questions:
                if Question == question:
                    return "This question already exist in the survey"
            self.questions.append(question)
            return "Successfully added the question to the survey"
        else:
            return "Reached limit of questions for this survey"

    def addResponse(self, answers):
        newResponse = surveyResponse()
        if len(self.questions) != len(answers):
            return "The number of answers must be equal with the number of questions in this survey. This survey contain " + str(len(self.questions)) + " questions"
        else:
            newResponse.addAnswers(answers)
            if len(newResponse.answers) != 0:
                self.responses.append(newResponse)
                return "Answers successfully registered for this survey"
            else:
                return "All your answer must be a number between 1 and 5"


class controller:
    def __init__(self):
        self.surveys = []

    def createSurvey(self, name):
        self.surveys.append(survey(name))
        return ("Survey '" + name + "' created successfully")

    def addQestionSurvey(self, name, question):
        for survey in self.surveys:
            if survey.name == name:
                return survey.addQuestion(question)
            else:
                return "Survey not found, please check the name of the survey"

    def addResponseSurvey(self, name, answers):
        for survey in self.surveys:
            if survey.name == name:
                return survey.addResponse(answers)
            else:
                return "Survey not found, please check the name of the survey"
