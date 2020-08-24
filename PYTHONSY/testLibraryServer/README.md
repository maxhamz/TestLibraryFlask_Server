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

**Fetch All**
----

  Fetch list of all users

* **URL**

  /users/getall

* **Method:**

  `GET`

* **URL Params**
  None

* **Body/Form Params**<br>
  None


* **Success Response:**

  * **Code:** 200 <br />
    **Content:**<br>

  `{`

   `"message": "FETCH ALL SUCCESS",`

   `"result": [`

    `{`

     `"created_at": "Mon, 20 Jul 2020 11:02:58 GMT",`

     `"email": "sample1@mail.com",`

     `"id": 4,`

     `"image_file": "default.jpg",`

     `"modified_at": "Mon, 20 Jul 2020 11:02:58 GMT",`

     `"username": "user2"`

    `},`

    `{`

     `"created_at": "Mon, 20 Jul 2020 10:53:29 GMT",`

     `"email": "sample@mail.com",`

     `"id": 2,`

     `"image_file": "19399091fd78591e.jpg",`

     `"modified_at": "Mon, 20 Jul 2020 10:53:29 GMT",`

     `"username": "user1"`

    `},`

    `{`

     `"created_at": "Fri, 21 Aug 2020 10:59:32 GMT",`

     `"email": "jajabi@mail.com",`

     `"id": 6,`

     `"image_file": "default.jpg",`

     `"modified_at": "Fri, 21 Aug 2020 10:59:32 GMT",`

     `"username": "tesu"`

    `},`

    `{`

     `"created_at": "Thu, 23 Jul 2020 12:24:58 GMT",`

     `"email": "ptsaribikamakmursejahtera@gmail.com",`

     `"id": 5,`

     `"image_file": "default.jpg",`

     `"modified_at": "Thu, 23 Jul 2020 12:24:58 GMT",`

     `"username": "user3"`

    `},`

    `{`

     `"created_at": "Fri, 21 Aug 2020 12:29:22 GMT",`

     `"email": "jajabi1@mail.com",`

     `"id": 7,`

     `"image_file": "default.jpg",`

     `"modified_at": "Fri, 21 Aug 2020 12:29:22 GMT",`

     `"username": "tesu1"`

    `},`

    `{`

     `"created_at": "Fri, 21 Aug 2020 12:30:06 GMT",`

     `"email": "jajabi2@mail.com",`

     `"id": 8,`

     `"image_file": "default.jpg",`

     `"modified_at": "Fri, 21 Aug 2020 12:30:06 GMT",`

     `"username": "tesu2"`

    `}`

   `],`

   `"status": 200`

  `}`

<br>

<hr>
<br>

**Fetch By ID**
----

  Fetch one user by ID

* **URL**

  /users/getById/<:userid>

* **Method:**

  `GET`

* **URL Params**
  `userid`: string

* **Body/Form Params**<br>
  None


* **Success Response:**

  * **Code:** 200 <br />
    **Content:**<br>

  `{`

   `"message": "SUCCESS: GET BY ID",`

   `"result": {`

    `"created_at": "Mon, 20 Jul 2020 10:53:29 GMT",`

    `"email": "sample@mail.com",`

    `"id": 2,`

    `"image_file": "19399091fd78591e.jpg",`

    `"modified_at": "Mon, 20 Jul 2020 10:53:29 GMT",`

    `"username": "user1"`

   `},`

   `"status": 200`

  `}`

* **Error Responses:**

  * **Code:** 404 NOT FOUND<br />
    **Content:**<br>`{`

     `"message": "NOT FOUND",`

     `"status": 404`

    `}`

<br>

<hr>

**Fetch By Username**
----

  Fetch one user by username

* **URL**

  /users/getById/<:username>

* **Method:**

  `GET`

* **URL Params**
  `username: string

* **Body/Form Params**<br>
  None


* **Success Response:**

  * **Code:** 200 <br />
    **Content:**<br>

  `{`

   `"message": "SUCCESS: GET BY ID",`

   `"result": {`

    `"created_at": "Mon, 20 Jul 2020 10:53:29 GMT",`

    `"email": "sample@mail.com",`

    `"id": 2,`

    `"image_file": "19399091fd78591e.jpg",`

    `"modified_at": "Mon, 20 Jul 2020 10:53:29 GMT",`

    `"username": "user1"`

   `},`

   `"status": 200`

  `}`

* **Error Responses:**

  * **Code:** 404 NOT FOUND<br />
    **Content:**<br>`{`

     `"message": "NOT FOUND",`

     `"status": 404`

    `}`

<br>

<hr>



Change Username
----

  Update username 

* **URL**

  /users/changeUsername

* **Method:**

  `PUT`

* **URL Params**
  None

* **Header Params**
  `access_token`: string (required)

* **Body/Form Params**

  - `current_username`: string
  - `new_username`: string


* **Success Response:**

  * **Code:** 200 <br />
    **Content:**<br>

  `{`

   `"message": "SUCCESS: UPDATE USERNAME",`

   `"result": {`

    `"created_at": "Thu, 23 Jul 2020 12:24:58 GMT",`

    `"email": "whatever@gmail.com",`

    `"id": 5,`

    `"image_file": "b16fb297953ff9e5.jpg",`

    `"modified_at": "Thu, 23 Jul 2020 12:24:58 GMT",`

    `"username": "user_new_one"`

   `},`

   `"status": 200`

  `}`

* **Error Responses:**

  * **Code:** 422 SIGNATURE VERIFICATION FAILED<br />
    **Content:**<br>

    `{`

     `"msg": "Signature verification failed"`

    `}`

<br>

<hr>



Update Profile Picture
----

  Update user's profile picture

* **URL**

  /users/updatePropic

* **Method:**

  `PUT`

* **URL Params**
  None

* **Header Params**
  `access_token`: string (required)

* **Body/Form Params**

  - `current_username`: string
  - `new_username`: string


* **Success Response:**

  * **Code:** 200 <br />
    **Content:**<br>

  `{`

   `"message": "SUCCESS: UPDATE USERNAME",`

   `"result": {`

    `"created_at": "Thu, 23 Jul 2020 12:24:58 GMT",`

    `"email": "whatever@gmail.com",`

    `"id": 5,`

    `"image_file": "b16fb297953ff9e5.jpg",`

    `"modified_at": "Thu, 23 Jul 2020 12:24:58 GMT",`

    `"username": "user_new_one"`

   `},`

   `"status": 200`

  `}`

* **Error Responses:**

  * **Code:** 422 SIGNATURE VERIFICATION FAILED<br />
    **Content:**<br>

    `{`

     `"msg": "Signature verification failed"`

    `}`

<br>

<hr>



Request Reset Password
----

  Requesting OTP to reset password

* **URL**

  /users/requestResetPassword

* **Method:**

  `POST`

* **URL Params**
  None

* **Header Params**
  `access_token`: string (required)

* **Body/Form Params**

  - `your_email`: string


* **Success Response:**

  * **Code:** 200 <br />
    **Content:**<br>

  `{`

   `"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTgwMDkyMjgsIm5iZiI6MTU5ODAwOTIyOCwianRpIjoiYTM1OGRlNWQtYzgzOS00NTkwLTljY2UtZjMwOWYxZmFkY2M4IiwiZXhwIjoxNTk4MDEwMTI4LCJpZGVudGl0eSI6eyJ1c2VybmFtZSI6InVzZXIzIiwiZW1haWwiOiJwdHNhcmliaWthbWFrbXVyc2VqYWh0ZXJhQGdtYWlsLmNvbSIsInVzZXJpZCI6NSwicHJvcGljIjoiZGVmYXVsdC5qcGciLCJPVFAiOiI2MTM5NTUifSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.zWL0IGOaz4rcx9x9VYauBOnET7kiTAG3dfqdZtzJmW8",`

   `"message": "Reset Instructions Sent."`

  `}`

* **Error Responses:**

  * **Code:** 404 NOT FOUND<br />
    **Content:**<br>

    `{`

     `"message": "NOT FOUND",`

     `"status": 404`

    `}`

<br>

<hr>



Reset Password
----

  Reset password using OTP

* **URL**

  /users/reset_password

* **Method:**

  `PUT`

* **URL Params**
  None

* **Header Params**
  `access_token`: string (required)

* **Body/Form Params**

  - `new_password`: string
  - `confirm_new_password`: string
  - `OTP`: integer


* **Success Response:**

  * **Code:** 200 <br />
    **Content:**<br>

  `{`

   `"message": "Password reset success.",`

   `"status": 200`

  `}`

* **Error Responses:**

  * **Code:** 401 ACCESS UNAUTHORIZED<br />
    **Content:**<br>

    `{`

     `"message": "OTP not match",`

     `"status": 401`

    `}`

  * **Code:** 400 BAD REQUEST<br />
    **Content:**<br>

    `{`

     `"message": "Passwords don't match",`

     `"status": 400

    `}`

<br>

<hr>

