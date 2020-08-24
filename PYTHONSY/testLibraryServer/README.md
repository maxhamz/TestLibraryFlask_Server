# Test Library Flask - Server

> A server-side library API, written using Python Flask, using MVC architecture format. Looking forward for a combination of simple, flexible, easy-to-maintain and dependable code.

<hr>



## Available Features by Models

1. Users:
   - Register
   - Login
   - Get All
   - Get By ID
   - Get By Username
   - Change Username
   - Update Profile Picture
   - Request Reset Password
   - Reset Password
   - Delete User
2. Books

<hr>



## USERS

### Register

Registers new user

* **URL**

  /users/register

* **Method:**

  `POST`

* **URL Params**
  None

* **Body/Form Params**<br>
  **Required**

  - `email` : string
  - `password` : string
  - `username`: string


* **Success Response:**

  * **Code:** 201 <br />
    **Content:**<br>

    `{`

     `"message": "REGISTER SUCCESS",`

     `"result": {`

      `"created_at": "Fri, 21 Aug 2020 12:30:06 GMT",`

      `"email": "jajabi2@mail.com",`

      `"id": 8,`

      `"image_file": "default.jpg",`

      `"modified_at": "Fri, 21 Aug 2020 12:30:06 GMT",`

      `"password": "$2b$10$1ch2f9OLK92IiOA.bv8ai.GbXXzdxkKzpKshpyPDXY5/zQhc8Gbdm",`

      `"username": "tesu2"`

     `},`

     `"status": 201`

    `}`

* **Error Responses:**

  * **Code:** 400 BAD REQUEST<br />
    **Content:**<br>`{`
      `"message": "BAD REQUEST",`
      `"status": 400`
    `}`

    <br>

<hr>
<br>

### **Login**

  Login user

* **URL**

  /users/login

* **Method:**

  `POST`

* **URL Params**
  None

* **Data Params**
  `{ "email" : "john_doe@sample.com", "password" : "johndoe1" }`<br>
  **Required**

  - `email` : string
  - `password` : string


* **Success Response:**

  * **Code:** 200 <br />
    **Content:**<br>
    `{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NywiZW1haWwiOiJjcmlzdGlhbm9fcm9uYWxkb0BsaXZlcnBvb2xmYy51ayIsImlhdCI6MTU4MzIzNzgwOH0.eUjWk-QOFVss77WLfbbqFvt9rKuLNCNk4xEzCSiAdYk"
    }`

* **Error Responses:**

  * **Code:** 401 ACCESS UNAUTHORIZED<br />
    **Content:**<br>`{`
      `"message": "ACCESS UNAUTHORIZED",`
      `"status": 401
    `}`

<br>

<hr>
<br>

