"""Tiny app module for the Jenkins/GitHub CI assignment."""


def greeting(name: str = "Jenkins") -> str:
    """Return a simple greeting that can be checked by unit tests."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greeting())
