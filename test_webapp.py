
from fnmatch import fnmatchcase
import pytest
import webapp as webapp
from flask import session

@pytest.fixture
def client():
    client=webapp.app.test_client()
    return client

def login(client, username, password):
    return client.post('/', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def search_home(client, dep, fname):
    return client.post('/view', data=dict(
        department=dep,
        first_name=fname
    ), follow_redirects=True)

def department_search(client, dep, fname):
    return client.post('/department/Accounting', data=dict(
        department=dep,
        first_name=fname
    ), follow_redirects=True)

def name_search(client, dep, fname):
    return client.post('/fname/Barker', data=dict(
        department=dep,
        first_name=fname
    ), follow_redirects=True)

def dep_name_search(client, dep, fname):
    return client.post('/search/Barker/Accounting', data=dict(
        department=dep,
        first_name=fname
    ), follow_redirects=True)

def add_employee(client):
    return client.post('/create', data=dict(
        first_name="Jeff",
        last_name="Wang",
        employee_id="A01", 
        employee_department="Accounting",
        employee_salary=25000,
        employee_age=23
    ), follow_redirects=True)

def add_db(client, username, password, db):
    return client.post('/createAdmin', data=dict(
        username=username,
        password=password,
        database_name=db
    ), follow_redirects=True)

def delete_db(client, username, password, db):
    return client.post('/confirm', data=dict(
        username=username,
        password=password,
        database_name=db
    ), follow_redirects=True)

def edit_employee(client):
    return client.post('/edit/A01', data=dict(
        first_name="Jack",
        last_name="Mac",
        employee_id="A02", 
        employee_department="Sales",
        employee_salary=250500,
        employee_age=24
    ), follow_redirects=True)

def test_homepage(client):
    assert client.get("/").status_code == 201

def test_invalid_home(client):
    assert login(client, "NotValid", "Not_Valid_pass").status_code == 404

def test_invalid_edit(client):
    assert client.get("/edit/A01").status_code==200

def test_invalid_logout(client):
    assert client.get("/logout").status_code==404

def test_invalid_create(client):
    assert client.get("/create").status_code==404

def test_invalid_single_view(client):
    assert client.get("/view/62689cd5d662deb8a269d5dc").status_code==404

def test_invalid_view(client):
    assert client.get("/view").status_code==404

def test_invalid_department(client):
    search_home(client, "Unreal", "").status_code==404
    name_search(client, "", "").status_code==404
    

def test_invalid_delete_unauth(client):
    assert client.get("/delete/62689cd5d662deb8a269d5dc").status_code==200

def test_view(client):
    login(client, "admin", "P@ssw0rd")
    assert client.get('/view').status_code==201

def test_view_employee(client):
    login(client, "admin", "P@ssw0rd")
    assert client.get("/view/62689cd566f9aeeda66f0a0b").status_code == 201
    assert client.get("/view/62689cd55dc").status_code==404

def test_create(client):
    login(client, "admin", "P@ssw0rd")
    assert client.get("/create").status_code == 200
    assert add_employee(client).status_code == 201

def test_search_home(client):
    assert login(client, "admin", "P@ssw0rd").status_code==201
    assert client.get("/view").status_code==201
    assert search_home(client, "Accounting", "").status_code==200
    assert search_home(client, "", "A01").status_code==200
    assert search_home(client, "Accounting", "Norton").status_code==200
    
def test_name_search(client):
    assert login(client, "admin", "P@ssw0rd").status_code==201
    assert name_search(client, "Accounting", "").status_code==200
    assert name_search(client, "Accounting", "Glenn").status_code==200
    assert name_search(client, "", "Glenn").status_code==200

def test_dep_name_search(client):
    assert login(client, "admin", "P@ssw0rd").status_code==201
    assert dep_name_search(client, "Accounting", "").status_code==200
    assert dep_name_search(client, "Accounting", "Glenn").status_code==200
    assert dep_name_search(client, "", "Glenn").status_code==200


def test_edit(client):
    login(client, "admin", "P@ssw0rd")
    assert client.get("/edit/A01").status_code == 200
    assert edit_employee(client).status_code==200

def test_search_fname(client):
    login(client, "admin", "P@ssw0rd")
    assert department_search(client, "", "A01").status_code==200
    assert department_search(client, "Sales", "A02").status_code==200

def test_delete(client):
    login(client, "admin", "P@ssw0rd")
    assert client.get("/delete/A01").status_code==404
    assert client.get("/delete/A02").status_code==302
    assert client.get("/delete/A03test").status_code==404


def test_department(client):
    login(client, "admin", "P@ssw0rd")
    search_home(client, "Accounting", "")
    assert client.get("/department/Accounting").status_code==200
    assert department_search(client, "Test", "").status_code==200

def test_logout(client):
    login(client, "admin", "P@ssw0rd")
    assert client.get("/logout").status_code==302

def test_create_admin_page(client):
    assert client.get("/createAdmin").status_code==200

def test_create_admin_post(client):
    client.get("/createAdmin")
    assert add_db(client, "Test_User", "Test_Pass", "Test_DB").status_code==201

def test_invalid_admin_create(client):
    client.get("/createAdmin")
    assert add_db(client, "admin", "P@ssword", "jackdb").status_code==404
    assert add_db(client, "jack", "P@ssword", "bcit").status_code==404

def test_delete_admin(client):
    login(client, "Test_User", "Test_Pass")
    assert client.get("/confirm").status_code==200
    assert delete_db(client, "Test_User", "Test_Pass", "Test_DB").status_code==201
    assert delete_db(client, "Invalid", "Invalid", "Invalid").status_code==404
    
    


    



