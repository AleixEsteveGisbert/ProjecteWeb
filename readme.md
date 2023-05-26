# Application Entry Points

This repository contains the source code for the application. Below are the main entry points and their descriptions.

## API Endpoints

The API endpoints provide access to various resources in the application.

### Ad Endpoint

- URL: `/api/ads/`
- Method: GET
- Description: Retrieves a list of all ads.
- Permissions: AllowAny
---
- URL: `/api/ads/`
- Method: POST
- Description: Creates a new ad.
- Permissions: AllowAny
---
- URL: `/api/ads/<id_ad>/`
- Method: PUT
- Description: Updates an ad.
- Permissions: IsAuthenticated

### Comment Endpoint

- URL: `/api/coments/`
- Method: POST
- Description: Creates a new comment.
- Permissions: IsAuthenticated
---
- URL: `/api/coments/<id_comment>/`
- Method: PUT
- Description: Updates a comment.
- Permissions: IsAuthenticated

### Authentication Endpoint
- URL: `/api/users/`
- Method: POST
- Description: Creates a new user.
- Permissions: AllowAny
---
- URL: `/api-token-auth/`
- Method: GET
- Description: Generates a token for the user
- Permissions: AllowAny
---
- URL: `/api/retrieve-user`
- Method: GET
- Description: Gets the info of a user using his token
- Permissions: IsAuthenticated