import pytest
from pages.login_page import LoginPage
from config import VALID_USER, VALID_PASSWORD, LOCKED_USER, PERFORMANCE_USER


@pytest.mark.parametrize("user, pwd", [
    (VALID_USER, VALID_PASSWORD),
    (LOCKED_USER, VALID_PASSWORD),
    (PERFORMANCE_USER, VALID_PASSWORD)
])
def test_login_scenarios(driver, user, pwd):
    login_page = LoginPage(driver)
    
    login_page.login(user, pwd)
    
    if user == LOCKED_USER:
        error_text = login_page.get_error_message().lower()
        assert "locked out" in error_text