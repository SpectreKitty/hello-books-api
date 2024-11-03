import pytest

def test_get_all_authors_with_no_records(client):
    # Act
    response = client.get("/authors")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_authors_with_two_records(client, two_saved_authors):
    # Act
    response = client.get("/authors")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name": "Brandon Sanderson"
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Sarah J. Maas",
    }

# When we have records and a `name` query in the request arguments, `get_all_authors` returns a list containing only the `Authors`s that match the query
def test_get_all_authors_with_title_query_matching_none(client, two_saved_authors):
    # Act
    data = {'name': 'Katee Roberts'}
    response = client.get("/authors", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# When we have records and a `name` query in the request arguments, `get_all_authors` returns a list containing only the `Authors`s that match the query
def test_get_all_authors_with_title_query_matching_one(client, two_saved_authors):
    # Act
    data = {'name': 'Sarah J. Maas'}
    response = client.get("/authors", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 2,
        "name": "Sarah J. Maas"
    }

def test_get_one_author_succeeds(client, two_saved_authors):
    # Act
    response = client.get("/authors/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Brandon Sanderson"
    }

# When we call `get_one_author` with a numeric ID that doesn't have a record, we get the expected error message
def test_get_one_author_missing_record(client, two_saved_authors):
    # Act
    response = client.get("/authors/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Author 3 not found"}

# When we call `get_one_author` with a non-numeric ID, we get the expected error message
def test_get_one_author_invalid_id(client, two_saved_authors):
    # Act
    response = client.get("/authors/cat")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Author cat invalid"}


def test_create_one_author(client):
    # Act
    response = client.post("/authors", json={
        "name": "Katee Roberts"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Katee Roberts"
    }

def test_create_one_author_no_title(client):
    # Arrange
    test_data = {}

    # Act
    response = client.post("/authors", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing name'}


def test_create_one_author_with_extra_keys(client):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "name": "V.E. Schwab"
    }
    # Act
    response = client.post("/authors", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "V.E. Schwab",
    }

# def test_update_author(client, two_saved_authors):
#     # Arrange
#     test_data = {
#         "name": "New Author"
#     }

#     # Act
#     response = client.put("/authors/1", json=test_data)

#     # Assert
#     assert response.status_code == 204
#     assert response.content_length is None

# def test_update_author_with_extra_keys(client, two_saved_authors):
#     # Arrange
#     test_data = {
#         "extra": "some stuff",
#         "name": "Another New Author"
#     }

#     # Act
#     response = client.put("/authors/1", json=test_data)

#     # Assert
#     assert response.status_code == 204
#     assert response.content_length is None

# def test_update_author_missing_record(client, two_saved_authors):
#     # Arrange
#     test_data = {
#         "title": "New Author",
#         "description": "The Best!"
#     }

#     # Act
#     response = client.put("/author/3", json=test_data)
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 404
#     assert response_body == {"message": "Author 3 not found"}

# def test_update_author_invalid_id(client, two_saved_authors):
#     # Arrange
#     test_data = {
#         "title": "New New Author"
#     }

#     # Act
#     response = client.put("/authors/cat", json=test_data)
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 400
#     assert response_body == {"message": "Author cat invalid"}

# def test_delete_author(client, two_saved_authors):
#     # Act
#     response = client.delete("/authors/1")

#     # Assert
#     assert response.status_code == 204
#     assert response.content_length is None

# def test_delete_author_missing_record(client, two_saved_authors):
#     # Act
#     response = client.delete("/authors/3")
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 404
#     assert response_body == {"message": "Author 3 not found"}

# def test_delete_author_invalid_id(client, two_saved_authors):
#     # Act
#     response = client.delete("/authors/cat")
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 400
#     assert response_body == {"message": "Author cat invalid"}