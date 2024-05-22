from survey import AnonymousSurvey
import pytest

@pytest.fixture
def create_survey_obj():
    """ Fixture to create the surevey object that can be used across all the tests """
    question='Who will win this lok Sabha election in India in 2024? '
    create_survey_obj=AnonymousSurvey(question)
    return create_survey_obj

def test_store_single_response(create_survey_obj):
    """ Test to validate storing single response """

    create_survey_obj.show_question()
    create_survey_obj.store_response('bjp')

    assert 'bjp' in create_survey_obj.response
    assert len(create_survey_obj.response)==1

def test_store_3_responses(create_survey_obj):
    """ Test to validate storing 3 responses """
    create_survey_obj.show_question()

    responses=['bjp','congress','admk']
    for response in responses:
        create_survey_obj.store_response(response)
    
    for eachR in create_survey_obj.response:
        assert eachR in responses