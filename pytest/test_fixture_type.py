import pytest
#pytest -s .\test_fixture_type.py
# Fixture avec scope="function" (par défaut)
@pytest.fixture
def fixture_function():
    print("\nCreation de la fixture (scope='function')")
    return "Donnees de test pour une fonction"

def test_function_1(fixture_function):
    assert fixture_function == "Donnees de test pour une fonction"

def test_function_2(fixture_function):
    assert fixture_function == "Donnees de test pour une fonction"

# Fixture avec scope="module"
@pytest.fixture(scope="module")
def fixture_module():
    print("\nCréation de la fixture (scope='module')")
    return "Donnees de test pour un module"

def test_module_1(fixture_module):
    assert fixture_module == "Donnees de test pour un module"

def test_module_2(fixture_module):
    assert fixture_module == "Donnees de test pour un module"

# Fixture avec scope="class"
@pytest.fixture(scope="class")
def fixture_class():
    print("\nCréation de la fixture (scope='class')")
    return "Donnees de test pour une classe"

class TestClass:
    def test_class_1(self, fixture_class):
        assert fixture_class == "Donnees de test pour une classe"

    def test_class_2(self, fixture_class):
        assert fixture_class == "Donnees de test pour une classe"

# Fixture avec scope="session"
@pytest.fixture(scope="session")
def fixture_session():
    return "Donnees de test pour toute la session"

def test_session_1(fixture_session):
    assert fixture_session == "Donnees de test pour toute la session"

def test_session_2(fixture_session):
    assert fixture_session == "Donnees de test pour toute la session"
