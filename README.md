## Implementing a REST API with Django using Amadeus APIs

This repository demonstrates how to build a REST API with Django to handle travel data using the Amadeus API.

## Prerequisites

To run this project locally you need to have the following:

-   [Python v3.10+](https://www.python.org/downloads/) installed on your local machine
-   A free [Amadeus for Developers account](https://developers.amadeus.com/register)
-   [Docker](https://docs.docker.com/get-started/get-docker/) installed on your local machine

## Obtaining Amadeus Credentials

All requests to the Amadeus APIs need to be authenticated with an API key and an API secret. To get these credentials:

1. Open [My Self-Service Workspace](https://developers.amadeus.com/my-apps) and select **Create a new app**:

    ![Amadeus self-service workspace](https://i.imgur.com/a022DLw.png)

2. On the "Create new app" page, provide "amadeus-django-rest-api" as the name of the app and select **Create**:

    ![Providing app details](https://i.imgur.com/r9DyC0n.png)

3. Once the app is created successfully, you will be navigated to the app details page where you will find your API key and API secret. Take note of these credentials as you will use them later:

    ![App details page](https://i.imgur.com/BR8BUUk.png)

### Running Locally

1. Clone the project and navigate into the directory:

    ```bash
    git clone https://github.com/kimanikevin254/amadeus-django-rest-api.git

    cd amadeus-django-rest-api
    ```

2. Rename the `.env.example` file and update your Amadeus credentials:

    ```bash
    mv .env.example .env
    ```

3. Start the Docker container:

    ```bash
    docker compose up -d
    ```

4. Once the container is running, test the API using Postman or cURL:

    **Using Postman:**

    - Send a GET request to:
        ```
        http://localhost:8000/api/cities/search?keyword=par
        ```
    - You should receive a JSON response containing city search results.

    **Using cURL:**

    ```bash
    curl -X GET "http://localhost:8000/api/cities/search?keyword=par"
    ```
