# FastAPI Base Project

Welcome to the FastAPI base project! This project is a simple starter template to help you build web applications using FastAPI, a modern web framework for building APIs with Python 3.7+.

This README will guide you through setting up the project with Poetry, a Python dependency management tool, and show you how to get the project running locally.

---

## Project Overview

This project is built using:

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **Tortoise ORM**: An asynchronous ORM for interacting with your database.
- **SQLite**: Used for local development; you can switch to PostgreSQL or other databases as needed.
- **Poetry**: A dependency management tool for Python that simplifies project setup and installation.

The project implements a basic `Todo` application API with CRUD (Create, Read, Update, Delete) operations and a PostgreSQL database setup. You can follow the steps below to get it running locally.

---

## Prerequisites

Before you get started, make sure you have the following tools installed:

1. **Python 3.7+**: The project is built using Python 3.7 or later. You can download Python from [here](https://www.python.org/downloads/).
2. **Poetry**: Poetry is used for managing dependencies. You can install it by following these steps:

   - On macOS/Linux:
     ```bash
     curl -sSL https://install.python-poetry.org | python3 -
     ```
   - On Windows, follow the instructions [here](https://python-poetry.org/docs/#installation).

---

## Setting Up the Project

Follow the steps below to set up the project locally.

### 1. Clone the Project Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository

