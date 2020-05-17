from main import controller


def test_answer():
    MyController = controller()
    assert len(MyController.surveys) == 0
