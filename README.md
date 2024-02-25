## About

This app presents a mockup of my personal project I am working on, CSS Challenges. It's a web application for beginner
web developers which consists of a set of challenges to solve related to different CSS concepts and rules. User will
gain expertise in web styling by getting acquainted with CSS through these tasks. 

### Models

The app has two models:

- #### Task
- #### Category - to group together tasks related to certain concept

## API endpoints

- http://localhost:8000 -  root view of the API with links to Categories and Tasks endpoints
- http://localhost:8000/admin - admin panel to manage database through Django Admin 
- http://localhost:8000/categories - list of all categories
- http://localhost:8000/categories/{category-id} - a detailed view of one category
- http://localhost:8000/tasks - list of all tasks
- http://localhost:8000/tasks/{task-id} - a detailed view of one task