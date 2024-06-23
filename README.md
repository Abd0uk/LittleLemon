# LittleLemon
# Backend Capstone Project

## Overview

This Capstone project is the final assignment of the [Backend Development Specialization](https://www.coursera.org/learn/back-end-developer-capstone/). 

The project showcases the skills and knowledge acquired throughout the course by solving a real-world problem. In this project, a Django web application is developed with multiple API endpoints and a MySQL database integration.

## Project Objectives

By completing this project, you will demonstrate the ability to:

- **Compose a backend application using multiple skills:** Implementing a full-stack backend solution.
- **Use Django to serve static HTML content:** Creating and managing web pages using Django views and templates.
- **Commit the project to a Git repository:** Version control using Git and GitHub.
- **Connect the backend to the database:** Integrating a MySQL database with Django.
- **Implement the menu and table booking APIs:** Developing RESTful APIs for menu management and table bookings.
- **Set up user registration and authentication:** Managing user accounts, including registration, login, and authentication.
- **Test the application with unit tests and Insomnia:** Ensuring the application is reliable and bug-free.
- **Synthesize the skills from this course and evaluate other learners:** Reflecting on the learning experience and providing feedback.
- **Reflect on this project's content and on the learning path that lies ahead:** Planning future learning and career steps.


## Setup and Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Abd0uk/LittleLemon.git
    cd LittleLemon
    ```

2. **Create a virtual environment:**
    ```bash
    pipenv shell
    ```

3. **Install the required dependencies:**
    ```bash
    pipenv install
    ```

4. **Configure the database:**
    - Update the `settings.py` file with your MySQL database credentials.

5. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

## Features

- **Static HTML Content Serving:** Using Django views and templates.
- **API Endpoints:**
  - Menu Management API
  - Table Booking API
- **User Authentication:** Registration, login, and authentication.
- **Unit Testing:** Using Django's testing framework.
- **API Testing:** Using Insomnia for testing API endpoints.



