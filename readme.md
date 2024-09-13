# Flask Web API for Web Scraping and Summarization

This project provides a Flask-based API to perform web scraping and text summarization. The API has two primary endpoints:
- `/scrape`: Triggers a web scraper to collect data and store it in a MySQL database.
- `/summarize`: Summarizes the scraped data based on a specified date using OpenAI's GPT-4.

The project is containerized using Docker for easy deployment and integration with other web services.

## Features
- **Web scraping**: Automates data collection from external sources.
- **Summarization**: Uses OpenAI's GPT-4 to summarize collected data.
- **API endpoints**: Allows web applications to trigger scraping and summarization tasks via HTTP requests.
- **Dockerized**: Easy deployment and management using Docker.

## Requirements

- Docker
- Docker Compose (optional, if using docker-compose)
- Python 3.9 (if running locally without Docker)
- MySQL database

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/news-crawler-service.git
cd news-crawler-service
```

### 2. Environment Variables
To securely store sensitive information such as database credentials and API keys, you will need to configure environment variables.

Create a .env file in the root directory:

```bash
touch .env
```
In the .env file, add the following:
```bash
# MySQL Database Connection
MYSQL_HOST=your_mysql_host
MYSQL_DATABASE=your_database_name
MYSQL_USER=your_database_user
MYSQL_PASSWORD=your_database_password

# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key
```

### 3. Build the Docker Container
To build the Docker container, run the following command:
```bash
docker build -t flask-scraper-summarizer .
```

### 4. Run the Docker Container
After building the Docker container, you can run it with:
```bash
docker run -d -p 5000:5000 --env-file .env flask-scraper-summarizer 
```
This will start the Flask API, making it available on http://localhost:5000.

### 5. Using Docker Compose (Optional)
You can also use Docker Compose to manage the application more easily. Create a docker-compose.yml file if it doesn't exist, and include the following:

```yaml
version: '3'
services:
  flask_app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - MYSQL_HOST=${MYSQL_HOST}
      - MYSQL_DATABASE=${MYSQL_DATABASE}
      - MYSQL_USER=${MYSQL_USER}
      - MYSQL_PASSWORD=${MYSQL_PASSWORD}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    env_file:
      - .env
```
Then run the application with:
```bash
docker-compose up --build -d
```

### 6. Running Locally (Without Docker)
If you want to run the Flask app locally without Docker, follow these steps:

- Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

- Set up your environment variables in a .env file.

- Start the Flask application:
    ```bash
  flask run --host=0.0.0.0 --port=5000
  ```

## API Endpoints
### 1. /scrape (POST)
Triggers the web scraper to collect data and store it in the MySQL database.

Request Example:
```bash
curl -X POST http://localhost:5000/scrape
```

Response Example:
```json
{
    "status": "success",
    "message": "Scraping completed successfully",
    "output": "Details of the scraping process"
}
```

### 2. /summarize (POST)
Triggers the summarization process for the scraped data based on the specified date.

Request Example:
```bash
curl -X POST http://localhost:5000/summarize -H "Content-Type: application/json" -d '{"date": "yesterday"}'
```

Response Example:
```json
{
    "status": "success",
    "message": "Summarization completed successfully",
    "output": "Summarized content"
}
```
## Environment Variables
These are the key environment variables required for running the app:

- MYSQL_HOST: The host of your MySQL database.
- MYSQL_DATABASE: The name of the MySQL database to use.
- MYSQL_USER: The MySQL database username.
- MYSQL_PASSWORD: The MySQL database password.
- OPENAI_API_KEY: Your OpenAI API key for GPT-4.

## Additional Notes
Ensure you have access to a working MySQL instance and that the credentials provided in the .env file are correct.
Make sure the OpenAI API key is valid and has access to the GPT-4 model.
You can modify the API routes in app.py to add more functionality or customize the response format as needed.