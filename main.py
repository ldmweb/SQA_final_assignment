class survey:
    def __init__(self, name):
        self.name = name


class controller:
    def __init__(self):
        self.surveys = []

    def createSurvey(self, name):
        self.surveys.append(survey(name))
        return "Survey created successfully"
