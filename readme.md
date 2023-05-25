# Application Entry Points

This repository contains the source code for the application. Below are the main entry points and their descriptions.

## API Endpoints

The API endpoints provide access to various resources in the application.

### Product Endpoint

- URL: `/api/product/`
- Method: GET
- Description: Retrieves a list of products.
- Permissions: AllowAny

### User Endpoint

- URL: `/api/user/`
- Method: GET
- Description: Retrieves a list of users.
- Permissions: IsAuthenticated

## Web Interface

The web interface allows users to interact with the application using a graphical user interface.

### Home Page

- URL: `/`
- Description: Displays the home page of the application.
- Permissions: AllowAny

### Product Details Page

- URL: `/product/{product_id}`
- Description: Displays the details of a specific product.
- Permissions: AllowAny

### User Profile Page

- URL: `/user/{user_id}/profile`
- Description: Displays the profile of a specific user.
- Permissions: AllowAny

### Create Product Page

- URL: `/product/create`
- Description: Allows authenticated users to create a new product.
- Permissions: IsAuthenticated