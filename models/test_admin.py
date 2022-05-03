
# Command used to test coverage of pytest 
# pytest --cov

import pytest
import admin


def test__init__success():
    admin_test = admin.Admin('admin', 'root', 'root_database')
    
    assert admin_test.username == 'admin'
    assert admin_test.password == 'root'
    assert admin_test.database == 'root_database'


def test_init_failure():
    with pytest.raises(TypeError):
        admin.Admin(5, 'root', 'root_database')
    
    with pytest.raises(TypeError):
        admin.Admin('admin', 5, 'root_database')

    with pytest.raises(TypeError):
        admin.Admin('admin', 'root', 5)

def test_to_dict():
    test_dict = {
        "username": 'admin',
        "password": 'root',
        "database": 'root_database'
    }

    assert admin.Admin.to_dict(admin.Admin('admin', 'root', 'root_database'))

