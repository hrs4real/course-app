# Course-app(Backend Project)

This is an Course application built using Python FastAPI.

## Overview

This application provides an API for managing courses. It allows users to create, update, and retrieve course details. The API endpoints include:

- `/course/create`: Create a new course.
- `/course/update`: Update an existing course.
- `/course/get`: Retrieve course details.

## Running the Application with Docker Compose

To run this FastAPI application using Docker Compose:

1. Make sure you have Docker and Docker Compose installed on your system.

2. Clone this repository:

   ```bash
   git clone https://github.com/hrs4real/course-app.git

3. Navigate to the project directory:

   ```bash
   cd course-app

4. Build and start the Docker containers using Docker Compose:

   ```bash
   docker-compose up --build

5. Once the containers are up and running, you can access the FastAPI application at http://localhost:8000 or http://127.0.0.1:8000/docs in your web browser or through API clients like Postman.
