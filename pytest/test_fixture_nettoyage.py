import pytest 

@pytest.fixture
def file_setup_and_cleanup():
    # Création d'un fichier avant chaque test
    f = open("test_file.txt", "w")
    f.write("Test data")
    f.close()
    yield "test_file.txt"  # Ceci est renvoyé au test

    # Nettoyage après chaque test
    import os
    os.remove("test_file.txt")

def test_file_creation(file_setup_and_cleanup):
    with open(file_setup_and_cleanup, "r") as f:
        content = f.read()
    assert content == "Test data"