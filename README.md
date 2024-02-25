## About

This app presents a mockup of my personal project I am working on, CSS Challenges. It's a web application for beginner
web developers which consists of a set of challenges to solve related to different CSS concepts and rules. User will
gain expertise in web styling by getting acquainted with CSS through these tasks.

### Models

The app has two models:

- #### Task
- #### Category - to group together tasks related to certain concept

## API endpoints

- http://localhost:8000 - root view of the API with links to Categories and Tasks endpoints
- http://localhost:8000/admin - admin panel to manage database through Django Admin
- http://localhost:8000/categories - list of all categories
- http://localhost:8000/categories/{category-id} - a detailed view of one category
- http://localhost:8000/tasks - list of all tasks
- http://localhost:8000/tasks/{task-id} - a detailed view of one task

## Run locally in Docker container

1. Clone the repository
2. Navigate into the repository in the terminal
3. Run
   ```
   docker compose up
   ```
4. Open second session in the terminal and run command below to list running docker containers. Find
   the `ventiondjangotask_web`

   ```
   docker ps
   ```
5. Find the `ventiondjangotask_web` image and connect to it using `CONTAINER_ID` from list received from docker ps
   command.

   ```
   docker exec -it {CONTAINER_ID} bash
   ```

6. Run Django migration using
   ```
   python manage.py migrate
   ```

7. Create Django superuser. Use the credentials you provided to login into th browsable API and access write method.
   Unauthenticated users can only view the content.
   ```
   python manage.py createsuperuser
   ```
8. You can fill up the database with some dummy data using
   ```
   python manage.py populate_database
   ```

8. You can now view the app in http://0.0.0.0:8000 in your browser.

After this initial setup you can start the app again simply by using the `docker compose up` command.
