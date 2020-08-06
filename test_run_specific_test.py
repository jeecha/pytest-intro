# class names that contain tests should start with `Test` by default
class TestClass:
    # test method names in classes should also start with `test` by default
    def test_class_method(self):
        assert True

# test method names should start with `test` by default
def test_method():
    assert True
