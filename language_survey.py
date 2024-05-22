from survey import AnonymousSurvey

question='Who will win this lok Sabha election in India in 2024? '
surveyObj=AnonymousSurvey(question)

surveyObj.show_question()

while True:
    poll=input("party? / q to quit ")
    if poll=='q':
        break
    else:
        surveyObj.store_response(poll)

surveyObj.show_results()

