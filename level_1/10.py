import uuid

from constants import ___


def stringify(value: int | str | float | None | uuid.UUID) -> str:
    pass


if __name__ == "__main__":
    assert stringify(value="12") == "12"
    assert stringify(value=15) == "15"
    assert stringify(value=.5) == "0.5"
    assert stringify(value=None) == "None"
