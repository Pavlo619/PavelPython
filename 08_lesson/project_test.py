import requests


base_url="https://ru.yougile.com/api-v2/projects"


headers = {'authorization': 'Bearer '}


def test_get_project():
    resp=requests.get(base_url, headers=headers )
    assert resp.status_code == 200


def test_create_project():
    body = {
    "title": "Домашняя работа 8",
    "users": {"3585e821-a3b1-4f2e-9a03-ddfe153a77f7": "worker"}
    }
    resp=requests.post(base_url, headers=headers, json=body)
    assert resp.status_code == 201

def test_edit_project():
    body = {
    "title": "Домашняя работа 8",
    "users": {"3585e821-a3b1-4f2e-9a03-ddfe153a77f7": "worker"}
    }
    resp=requests.post(base_url, headers=headers, json=body)
    assert resp.status_code == 201
    id=resp.json()["id"]
    body = {
        "title": "Домашняя работа 8 отредактированный",
        "users": {"3585e821-a3b1-4f2e-9a03-ddfe153a77f7": "worker"}
    }
    resp2=requests.put(base_url+id, headers=headers, json=body)
    assert resp2.status_code == 200

def test_get_one_project():
    body = {
    "title": "Домашняя работа 8",
    "users": {"3585e821-a3b1-4f2e-9a03-ddfe153a77f7": "worker"}
    }
    resp=requests.post(base_url, headers=headers, json=body)
    assert resp.status_code == 201
    id=resp.json()["id"]
    resp2=requests.get(base_url+id, headers=headers)
    assert resp2.status_code == 200

def test_get_negative_project():
    resp=requests.get(base_url)
    assert resp.status_code == 401

def test_create_negative_project():
    resp=requests.post(base_url, headers=headers)
    assert resp.status_code == 400

def test_edit_negative_project():
    body = {
    "title": "Домашняя работа 8",
    "users": {"3585e821-a3b1-4f2e-9a03-ddfe153a77f7": "worker"}
    }
    resp=requests.post(base_url, headers=headers, json=body)
    assert resp.status_code == 201
    id=resp.json()["id"]
    body = {
        "title": "",
        "users": {"3585e821-a3b1-4f2e-9a03-ddfe153a77f7": "worker"}
    }
    resp2=requests.put(base_url+id, headers=headers, json=body)
    assert resp2.status_code == 400