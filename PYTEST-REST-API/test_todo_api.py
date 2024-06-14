import requests
import uuid

ENDPOINT = "https://todo.pixegami.io"

def create_task(payload):
    """ Helper function to create a task by using the given payload """
    
    ct_response = requests.put(ENDPOINT+"/create-task",json=payload)
    return ct_response

def update_task(payload):
    """ Helper function to update a task by using the given payload """
    
    ut_response = requests.put(ENDPOINT+"/update-task",json=payload)
    return ut_response

def get_task(task_id):
    """ Helper function to get a task by using the given task id """
    
    gt_response = requests.get(ENDPOINT+"/get-task/"+task_id)
    return gt_response

def list_tasks(user_id):
    """ Helper function to list the tasks for a given user input """
    
    lst_response = requests.get(ENDPOINT+"/list-tasks/"+user_id)
    return lst_response

def delete_task(task_id):
    """ Helper funtion to delete a given task based on the task id """
    
    dt_response = requests.delete(ENDPOINT+"/delete-task/"+task_id)
    return dt_response

def new_task_payload():
    """ Helper to generate a payload for a new task """
    
    user_id = uuid.uuid4().hex
    contentStr = uuid.uuid4().hex

    payload = {
        "content": "Make "+contentStr,
        "user_id": "ole"+user_id,
        "task_id": "12345",
        "is_done": False
    }
    return payload

# Actual Pytests starting with test_

def test_can_create_task():
    """ Test to verify if a task can be created using a PUT call against the endpoint 
    create -> get """
    
    payload = new_task_payload()
    ct_response = create_task(payload=payload)
    assert ct_response.status_code == 200
    data=ct_response.json()
    
    task_id = data['task']['task_id']

    gt_response = get_task(task_id=task_id)
    data = gt_response.json()

    assert gt_response.status_code == 200
    assert payload['user_id'] == data['user_id']
    assert payload["content"] == data['content']

def test_can_update_task():
    """ Test to verify if a task can be updated
    create -> update -> get """

    payload = new_task_payload()

    ct_response = create_task(payload=payload)
    assert ct_response.status_code == 200
    tid = ct_response.json()['task']['task_id']

    upd_payload = {
        "content": "Make Hay while the sun shines",
        "user_id": payload['user_id'],
        "task_id": tid,
        "is_done": True
    }

    ut_response = update_task(payload=upd_payload)
    assert ut_response.status_code == 200

    upd_task_id=ut_response.json()

    gt_response = get_task(upd_task_id['updated_task_id'])
    gt_data=gt_response.json()

    assert gt_data['content'] == upd_payload['content']
    assert gt_data['is_done'] == upd_payload['is_done']
    assert gt_data['content'] != payload['content']

def test_can_list_tasks_per_user():
    """ Test to verify if all the tasks for a given user can be listed """
    n=10
    nt_payload = new_task_payload()

    for _ in range(n):
        
        ct_response = create_task(payload=nt_payload)
        assert ct_response.status_code == 200

    lst_response = list_tasks(user_id=nt_payload['user_id'])
    resp=lst_response.json()
    assert len(resp['tasks']) == n

def test_can_delete_task():
    """ Test to verify if a given task can be deleted using the delete api """
    payload = new_task_payload()

    ct_response = create_task(payload=payload)
    assert ct_response.status_code == 200
    tid = ct_response.json()['task']['task_id']

    dt_response = delete_task(tid)
    assert dt_response.status_code == 200

    gt_response=get_task(tid)
    assert gt_response.status_code == 404