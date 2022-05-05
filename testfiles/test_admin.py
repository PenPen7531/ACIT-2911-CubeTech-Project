
# Command used to test coverage of pytest 
# pytest --cov

import pytest
from admin import Admin


def test__init__success():
    admin_test = Admin('admin', 'root', 'root_database')
    
    assert admin_test.username == 'admin'
    assert admin_test.password == 'root'
    assert admin_test.database == 'root_database'


def test_init_failure():
    with pytest.raises(TypeError):
        Admin(5, 'root', 'root_database')
    
    with pytest.raises(TypeError):
        Admin('admin', 5, 'root_database')

    with pytest.raises(TypeError):
        Admin('admin', 'root', 5)

def test_to_dict():
    test_dict = {
        "username": 'admin',
        "password": 'root',
        "database": 'root_database'
    }

    assert Admin.to_dict(Admin('admin', 'root', 'root_database')) == test_dict

