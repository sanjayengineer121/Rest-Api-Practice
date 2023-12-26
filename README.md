# REST API HTTP Methods and Their Usage

REST APIs enable the development of various web applications, supporting all CRUD (Create, Retrieve, Update, Delete) operations. Adhering to REST guidelines involves using specific HTTP methods for different server calls. The following information helps determine the suitable HTTP method for API actions.

## Table of Contents

- [HTTP GET](#1-http-get)
- [HTTP POST](#2-http-post)
- [HTTP PUT](#3-http-put)
- [HTTP DELETE](#4-http-delete)
- [HTTP PATCH](#5-http-patch)
- [Summary](#summary)
- [Glossary](#glossary)

## 1. HTTP GET

Use GET requests to retrieve resource representation/information without modifying it. GET is considered a safe method, and it should be idempotent. The server must return HTTP response code 200 (OK) if the resource is found, 404 (NOT FOUND) if not found, and 400 (BAD REQUEST) for incorrectly formed requests.

### 1.1. GET API Response Codes

- **200 (OK):** Resource found, along with the response body (XML or JSON).
- **404 (NOT FOUND):** Resource not found.
- **400 (BAD REQUEST):** Incorrectly formed GET request.

### 1.2. Example URIs

- `HTTP GET http://127.0.0.1:5000/api/books/person`
- `HTTP GET http://127.0.0.1:5000/api/books/person/3`

import requests

url = "http://127.0.0.1:5000/api/books/person/3"
url= "https://sanjayer121.pythonanywhere.com/api/books/person/2"
data = {
    "name": "Shafali khan",
    "age": 27,
    "gender": "Male"
}

headers = {"Content-Type": "application/json"}
response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Response Content:")
print(response.json())



## 2. HTTP POST

Use POST APIs to create new subordinate resources. Responses are not cacheable, and POST is neither safe nor idempotent. Ideally, a successful creation should return HTTP response code 201 (Created).

### 2.1. POST API Response Codes

- **201 (Created):** Resource created successfully, with a Location header.
- **200 (OK) or 204 (No Content):** Appropriate response if no identifiable URI for the new resource.

### 2.2. Example URIs

- `HTTP POST http://www.appdomain.com/users`
- `HTTP POST http://www.appdomain.com/users/123/accounts`

#--------code---------------

-import requests

-url = "http://127.0.0.1:5000/api/books/person"
-url= "https://sanjayer121.pythonanywhere.com/api/books/person/2"
-data = {
-    "name": "Shafali khan",
-    "age": 27,
-    "gender": "Male"
-}

-headers = {"Content-Type": "application/json"}
-response = requests.post(url, json=data, headers=headers)

-print("Status Code:", response.status_code)
-print("Response Content:")
-print(response.json())

#------------------------------------------

## 3. HTTP PUT

Use PUT APIs to primarily update an existing resource. Responses are not cacheable. If a new resource is created, return HTTP response code 201 (Created). If an existing resource is modified, return either 200 (OK) or 204 (No Content).

### 3.1. PUT API Response Codes

- **201 (Created):** New resource created.
- **200 (OK) or 204 (No Content):** Successful modification of an existing resource.

### 3.2. Example URIs

- `HTTP PUT http://www.appdomain.com/users/123`
- `HTTP PUT http://www.appdomain.com/users/123/accounts/456`


#--------------------code
import requests

url = "http://127.0.0.1:5000/api/books/person/3"

data = {
    "name": "Shafali khan",
    "age": 27,
    "gender": "Male"
}

headers = {"Content-Type": "application/json"}
response = requests.put(url, json=data, headers=headers)

print("Status Code:", response.status_code)
print("Response Content:")
print(response.json())

#-------------------------------

*Note: PUT requests are made on a single resource, while POST requests are made on resource collections.*

## 4. HTTP DELETE

DELETE APIs delete identified resources. DELETE operations are idempotent, and responses are not cacheable. A successful response should be HTTP response code 200 (OK) with an entity describing the status, 202 (Accepted) if queued, or 204 (No Content) if performed without an entity.

### 4.1. DELETE API Response Codes

- **200 (OK):** Successful deletion with an entity describing the status.
- **202 (Accepted):** Action queued.
- **204 (No Content):** Action performed without an entity.

### 4.2. Example URIs

- `HTTP DELETE http://www.appdomain.com/users/123`
- `HTTP DELETE http://www.appdomain.com/users/123/accounts/456`

import requests

url = "http://127.0.0.1:5000/api/books/person/3"

headers = {"Content-Type": "application/json"}
response = requests.delete(url, headers=headers)

print("Status Code:", response.status_code)
print("Response Content:")
print(response.json())


## 5. HTTP PATCH

Use PATCH requests for partial updates on a resource. PATCH is suitable for updating a part of an existing resource, while PUT is used for replacing a resource entirely.

*Note: PATCH support may vary, and request payload is not as straightforward as PUT.*

---

## Summary

REST API design involves using specific HTTP methods for different actions. Understanding the guidelines for each method helps in building efficient and standardized web applications.

## Glossary

- **CRUD:** Create, Retrieve, Update, Delete
- **Idempotent:** Producing the same result every time until modified by another operation.
- **Cacheable:** Whether the response can be cached by the client.
- **URI:** Uniform Resource Identifier.
