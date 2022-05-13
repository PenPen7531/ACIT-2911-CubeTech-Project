
import pytest
from login import Login
from admin import Admin
from crypto import Crypto
from unittest.mock import mock_open, patch


JSON_FILE = """[
  {
    "username": "admin1",
    "password": "b03ddf3ca2e714a6548e7495e2a03f5e824eaac9837cd7f159c67b90fb4b7342",
    "database": "admin1db"
  },
  {
    "username": "admin2",
    "password": "8a3dff779c20f435fbe76de5ecabec0d64313f2105f8681fc49315dfe87a37db",
    "database": "admin2db"
  },
  {
    "username": "admin3",
    "password": "2e0b8d61fa2a6959d254b6ff5d0fb512249329097336a35568089933b49abdde",
    "database": "admin3db"
  }

]"""


@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=JSON_FILE)
def bcit(mock_file):
    return Login()


@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_open(mock_file):
    admin = Login()
    mock_file.assert_called_once()
    assert "data/logins.json" in mock_file.call_args[0]


def test_find_login_by_username(bcit):
    admin = bcit.find_login_by_username("admin1")
    assert type(admin) is Admin
    assert admin.username == "admin1"

    admin = bcit.find_login_by_username("test")
    assert admin == None


def test_add_login(bcit):
    hareem = Admin(admin_username="hareem",
                   admin_password="hareem", admin_database="test_hareem")
    bcit.add_login(hareem)
    bcit.save()
    assert hareem in bcit.login


def test_delete_admin(bcit):
    f = open("./data/admin1db.json", "w")
    f.write("test")
    f.close()
    remove_admin = bcit.delete_admin("admin1")
    assert remove_admin is True
    for login in bcit.login:
        assert login.username != "admin1"

    remove_admin = bcit.delete_admin("test")
    assert remove_admin is False


def test_check_database_name(bcit):
    admin = bcit.check_database_name("admin1db")
    assert admin is True
    admin = bcit.check_database_name("test")
    assert admin is False


def test_login_authenticate(bcit):
    admin1 = bcit.login_authenticate("admin1", "P@ssw0rd")
    assert admin1 is True
    # enc_password = Crypto.enc_pass("P@ssw0rd")
    for login in bcit.login:
        assert login.username != "test1"
        assert login.password != "P@ssw0rd"
    false_admin = bcit.login_authenticate("test1", "testing")
    assert false_admin is False


@patch("builtins.open", new_callable=mock_open)
def test_save(mock_file, bcit):
    bcit.save()
    mock_file.assert_called_once_with("data/logins.json", "w")
