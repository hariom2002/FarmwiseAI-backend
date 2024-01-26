# Bookstore Management System API Documentation

## Introduction

Welcome to the Bookstore Management System API documentation! This API is designed to facilitate the management of a bookstore by providing a set of RESTful endpoints for adding, retrieving, updating, and deleting book information. Whether you are a developer integrating with our system or an administrator looking to understand the functionalities, this documentation will guide you through the process.

## Key Features

- **Book Management:** Easily add, retrieve, update, and delete book details such as title, author, ISBN, price, and quantity.
- **Authentication:** Secure your API with basic authentication.
- **Database Integration:** A well-designed database schema ensures efficient storage and retrieval of book information.
- **Testing:** Comprehensive unit tests are provided to ensure the reliability of the API endpoints.

## Getting Started

To begin using the Bookstore Management System API, follow the installation instructions in the Installation section. Familiarize yourself with the database schema in Database Schema, and explore the available API endpoints detailed in API Endpoints.

### Installation

#### Prerequisites

Ensure that you have the following prerequisites installed on your system:

- **Python 3.9+:** The API is built using Python, so make sure you have a compatible version installed. You can download Python from [python.org](https://www.python.org/).

- **Virtual Environment (Optional but recommended):** It is good practice to use a virtual environment to isolate the API dependencies. Install it using the following command:

```bash
# Example command for virtual environment setup
python3 -m venv venv
```

Activate the virtual environment:

- **On Windows:**

```bash
venv\Scripts\activate
```

- **On macOS and Linux:**

```bash
source venv/bin/activate
```

#### Clone the Repository

Clone the Bookstore Management System API repository from GitHub:

```bash
git clone https://github.com/Amanpatel2002-g/bookstore
```


#### Run the API

Start the API server using the following command:

```bash
# Example command for running the API
python manage.py runserver
```

### Database Schema

The Bookstore Management System API uses a well-defined database schema to store information about books. Below is the schema:

#### Table: books

- **title (string)**
- **author (string)**
- **isbn (string, unique)**
- **price (float)**
- **quantity (integer)**

The `books` table holds the core information about each book, including title, author, ISBN, price, and quantity.

### API Endpoints

#### 4.1 Adding a New Book

**Endpoint:** POST /bookStore/books/

**Request:**
```json
{
  "title": "Example Book",
  "author": "John Doe",
  "isbn": "1234567890",
  "price": 19.99,
  "quantity": 50
}
```
**Response:** 201 Created

#### 4.2 Retrieving All Books

**Endpoint:** GET /bookStore/books/

**Request Header:**
```
Authorization: Token {your_token_here}
```

**Response:**
```json
[
  {
    "title": "Example Book",
    "author": "John Doe",
    "isbn": "1234567890",
    "price": 19.99,
    "quantity": 50
  },
  // ... other books
]
```

#### 4.3 Retrieving a Specific Book by ISBN

**Endpoint:** GET /bookStore/books/{isbn}

**Request Header:**
```
Authorization: Token {your_token_here}
```

**Response:**
```json
{
  "title": "Example Book",
  "author": "John Doe",
  "isbn": "1234567890",
  "price": 19.99,
  "quantity": 50
}
```

#### 4.4 Updating Book Details

**Endpoint:** PATCH /bookStore/books/{isbn}

**Request:**
```json
{
  "title": "Updated Example Book",
  "author": "Jane Doe",
  "price": 24.99,
  "quantity": 60
}
```
**Request Header:**
```
Authorization: Token {your_token_here}
```
**Response:** 200 OK

#### 4.5 Deleting a Book

**Endpoint:** DELETE /bookStore/books/{isbn}

**Request Header:**
```
Authorization: Token {your_token_here}
```

**Response:** 204 No Content

## Authentication

The API implements basic authentication to restrict access to certain endpoints. Users are required to include valid credentials when accessing protected resources.

To authenticate, register yourself at [http://127.0.0.1:8000/account/register/](http://127.0.0.1:8000/account/register/), obtain a token, and include it in the `Authorization` header when making API requests.
## Testing

To ensure the reliability of the API, comprehensive unit tests have been provided. Before running the tests, ensure that you turn off authentication. Follow the steps below:

1. Open the file `C:\Users\apoff\Desktop\farmwise_python\BookStore\book_store\api\views.py`.

   - In both functions, comment out the line containing the permission class.

     Example:

     ```python
     # Comment out the following line in both functions
     # permission_classes = [IsAuthenticated]
     ```

2. Open the file `settings.py`.

   - Comment out the line containing `'rest_framework.authentication.TokenAuthentication',`.

     Example:

     ```python
     # Comment out the following line
     # 'rest_framework.authentication.TokenAuthentication',
     ```

Now you can run the tests using the following command:

```bash
python manage.py test
```

## Conclusion

Thank you for exploring the Bookstore Management System API, a powerful tool designed to streamline the management of your bookstore. This API enables users to seamlessly add, retrieve, update, and delete book details, providing a robust solution for bookstore administrators and developers alike.

## Project Overview

The Bookstore Management System API is built on a foundation of efficiency and reliability. Leveraging the power of Python and Django, it combines a well-structured database schema with RESTful API endpoints to deliver a seamless experience in managing your bookstore's inventory.

## Technology Stack

- **Backend Framework:** Django
- **Programming Language:** Python

## How to Get Involved

Whether you are an administrator seeking to optimize your bookstore operations or a developer looking to integrate with our system, we invite you to get involved. Feel free to explore the comprehensive documentation, run the provided tests, and contribute to the ongoing development of this project.

Thank you for choosing the Bookstore Management System API. We look forward to seeing how it enhances your bookstore management experience!