<b>SIMPLE CRUD API WITH DJANGO REST FRAMEWORK</b>

<b>REQUIREMENTS</b>
1.  django
2.  djangorestframework
3.  djangorestframework-simplejwt
4.  pyjwt
5.  psycopg2-binary


<b>STRUCTURE</b>

In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around collections and elements, both of which are resources.

In our case, we have one single resource, customerapp, so we will use the following URLS - /customerapp/api/customer and customerapp/api/customer/{id}/ for collections and elements, respectively:

URL -   http://192.168.1.9:3003/customerapp/api/customer/
<br>HTTP Method -   GET
<br>CRUD Method -   READ
<br>Description -   Get all customer data

URL -   http://192.168.1.9:3003/customerapp/api/customer/{id}/
<br>HTTP Method -   GET
<br>CRUD Method -   READ
<br>Description -   Get a single customer data

URL -   http://192.168.1.9:3003/customerapp/api/customer/
<br>HTTP Method -   POST
<br>CRUD Method -   CREATE
<br>Description -   Create new customer data

URL -   http://192.168.1.9:3003/customerapp/api/customer/{id}/
<br>HTTP Method -   PUT
<br>CRUD Method -   UPDATE
<br>Description -   Update new customer data

URL -   http://192.168.1.9:3003/customerapp/api/customer/{id}/
<br>HTTP Method -   DELETE
<br>CRUD Method -   DELETE
<br>Description -   Delete a customer data


<b>TOKEN GENERATIONS</b>

To get a token first we need to request, so we can log in

URL - http://192.168.1.9:3003/api/token/
<br>username : anuraj
<br>password : anuraj@123

after that, we get the token
<br>
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0MjI0MDM4MSwiaWF0IjoxNjQyMTUzOTgxLCJqdGkiOiJmZjczNTA4MjBiYzQ0YmE4YmE1NGVlYjc5YmJlYTljOSIsInVzZXJfaWQiOjF9",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQyMTU0MjgxLCJpYXQiOjE2NDIxNTM5ODEsImp0aSI6IjY5YWU5MTZkN2YzMzRjZWY5NzQ4YTA0MjJmNmJjZTY3IiwidXNlcl9pZCI6MX0"
}

<b>COMMANDS</b>

Get all customer
http GET http://192.168.1.9:3003/customerapp/api/customer/ "Authorization: Bearer {YOUR_TOKEN}"

Get a single customer
http GET http://192.168.1.9:3003/customerapp/api/customer/{id}/ "Authorization: Bearer {YOUR_TOKEN}"

Create a new customer
http POST http://192.168.1.9:3003/customerapp/api/customer/ "Authorization: Bearer {YOUR_TOKEN}" first_name="anuraj" last_name="kr" phone="8907794408" email="anuraj@techversantinfo.com" 

Full update a customer
http PUT http://192.168.1.9:3003/customerapp/api/customer/{id}/ "Authorization: Bearer {YOUR_TOKEN}" first_name="ajith" last_name="kr" phone="8907794407" email="ajith@techversantinfo.com" 

Delete a movie
http DELETE http://192.168.1.9:3003/customerapp/api/customer/{id}/ "Authorization: Bearer {YOUR_TOKEN}"