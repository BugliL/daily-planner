# FastAPI and Vue 3 Application

This project is a web application that combines a FastAPI backend with a Vue 3 frontend. It allows users to manage tasks in a daily planner format, utilizing a NoSQL database for data storage.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

- **app/**: Contains the FastAPI application code.
  - **main.py**: Entry point of the FastAPI application.
  - **models.py**: Defines data models for the NoSQL database.
  - **routes.py**: Contains route definitions for handling HTTP requests.
  - **database.py**: Manages the connection to the NoSQL database.

- **requirements.txt**: Lists the dependencies required for the backend application.

- **Dockerfile**: Instructions to build the Docker image for the backend application.

### Frontend

- **public/**: Contains static assets for the Vue 3 application.

- **src/**: Contains the source code for the Vue 3 application.
  - **App.vue**: Root component of the Vue application.
  - **main.js**: Entry point for the Vue application.
  - **components/**: Contains Vue components, including `TaskList.vue` for displaying tasks.

- **package.json**: Configuration file for npm, listing dependencies and scripts.

- **vite.config.js**: Configuration for Vite, the build tool used for the Vue application.

### Docker

- **docker-compose.yml**: Defines the services for the application, including both the backend and frontend.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd fastapi-vue-app
   ```

2. **Build and run the application using Docker**:
   ```
   docker-compose up --build
   ```

3. **Access the application**:
   - The backend API will be available at `http://localhost:8000`.
   - The frontend application will be available at `http://localhost:3000`.

## Usage

- Use the frontend interface to create, edit, and delete tasks.
- The tasks will be stored in the NoSQL database managed by the FastAPI backend.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.