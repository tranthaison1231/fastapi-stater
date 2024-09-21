from app.core.utils.signleton import singleton


@singleton
class MyClass:
    def __init__(self, value) -> None:
        self.value = value


def test_singleton_behavior():
    instance1 = MyClass(10)
    instance2 = MyClass(20)

    assert instance1 is instance2

    assert instance1.value == 10
    assert instance2.value == 10
