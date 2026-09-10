def test_api_get(playwright):
    request = playwright.request.new_context()
    response = request.get("https://reqres.in/api/users/2")
    assert response.status == 200
    response = response.json()
    print(response)
    #assertions
    assert response["data"]["id"] == 2
    assert response["data"]["first_name"] == "Janet"
    assert response["data"]["last_name"] == "Weaver"
    assert response["data"]["avatar"] == "https://reqres.in/img/faces/2-image.jpg"

    request.dispose()