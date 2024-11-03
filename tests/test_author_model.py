from app.models.author import Author
import pytest

def test_from_dict_returns_author():
    # Arrange
    author_data = {
        "name": "Brandon Sanderson",
    }

    # Act
    new_author = Author.from_dict(author_data)

    # Assert
    assert new_author.name == "Brandon Sanderson"

def test_from_dict_with_no_name():
    # Arrange
    author_data = {}

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_author = Author.from_dict(author_data)

def test_from_dict_with_extra_keys():
    # Arrange
    author_data = {
        "name": "Brandon Sanderson",
        "extra": "extra value"
    }

    # Act
    new_author= Author.from_dict(author_data)

    # Assert
    assert new_author.name == "Brandon Sanderson"

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Author(id = 1,
                    name="Sarah J. Maas",
                    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 2
    assert result["id"] == 1
    assert result["name"] == "Sarah J. Maas"

def test_to_dict_missing_id():
    # Arrange
    test_data = Author(name="Katee Roberts")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 2
    assert result["id"] is None
    assert result["name"] == "Katee Roberts"

def test_to_dict_missing_title():
    # Arrange
    test_data = Author(id=1,)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 2
    assert result["id"] == 1
    assert result["name"] is None
