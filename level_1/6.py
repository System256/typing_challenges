from constants import ___


def is_loan_amount_too_big(loan_amount_usd: float, max_loan_amount_for_user_usd: float | None) -> bool:
    pass


if __name__ == "__main__":
    assert is_loan_amount_too_big(loan_amount_usd=1000, max_loan_amount_for_user_usd=4000) is False
    assert is_loan_amount_too_big(loan_amount_usd=1000, max_loan_amount_for_user_usd=None) is False
