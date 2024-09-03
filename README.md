# FastApi - Challenge

Challenge of API with framework FastAPI -> Python!
- URL [```ApiRest - DOCS```](http://149.50.139.254:5000/docs)

![Preview Image](https://github.com/andrescuello7/pi-challenge-1/assets/72234490/38cc0f14-2d9a-439c-93bd-62fc9ef99aac)

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/andrescuello7/be_challenge_v1
    cd pi-be_challenge_v1-1/
    ```

2. **Set Up the Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    Create a `.env` file in the root directory and add the necessary environment variables. You can use the `.env.example` file as a reference.

5. **Run Migrations**

    ```bash
    flask db upgrade
    ```

6. **Run the Application**

    ```bash
    python main.py
    ```

## Docker

To build and run the application using Docker, use the provided Docker configurations:

1. **Build and Run**

    ```bash
    docker-compose -f docker/develop/docker-compose.yml up --build
    ```
    