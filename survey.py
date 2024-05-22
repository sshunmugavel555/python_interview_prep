""" Survey Module """

class AnonymousSurvey():
    """ Class to model a survey of question in random """

    def __init__(self,question) -> None:
        self.question=question
        self.response=[]

    def show_question(self) -> None:
        """ Print out the question on the console """
        print(self.question)

    def store_response(self,new_response) -> None:
        """ Store user response to the list """
        self.response.append(new_response)

    def show_results(self):
        """ Show all responses that are given """
        print(f"Survey Results")
        for eachResp in self.response:
            print(eachResp)