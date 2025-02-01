# Django FAQ Management System

This project is a Django-based FAQ management system designed to demonstrate several advanced features:

- **Multi-language Translation Support:** Automatically translates FAQ questions and answers (using [googletrans](https://pypi.org/project/googletrans/)) into additional languages (e.g., Hindi and Bengali) during object creation.
- **Rich Text Editor Integration:** Uses [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor) for WYSIWYG editing.
- **User-Friendly Admin Interface:** Enhanced admin integration for managing FAQs.
- **Containerization with Docker:** Comes with a `Dockerfile` and `docker-compose.yml` for easy deployment.
- **Environment Configuration:** Uses a `.env` file (loaded via [python-dotenv](https://pypi.org/project/python-dotenv/)) to securely manage sensitive data.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running Locally](#running-locally)
- [Docker Setup](#docker-setup)
- [Routes & Testing](#routes--testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- **FAQ Model with Automatic Translations:**  
  The FAQ model stores a primary English question/answer pair. If additional language fields (e.g., Hindi and Bengali) are left empty, the `save()` method uses googletrans to automatically fill them in (falling back to English on error).

- **Rich Text Editing:**  
  Uses django-ckeditor to allow rich text formatting for the answer field.

- **Admin Interface:**  
  A custom Django admin configuration for FAQ allows for easy editing, searching, and filtering of FAQ entries.

- **Dockerized Environment:**  
  The provided `Dockerfile` and `docker-compose.yml` allow for containerized deployment of the app alongside a PostgreSQL database.

- **Secure Environment Configuration:**  
  Sensitive settings (like `SECRET_KEY` and database credentials) are stored in a `.env` file and loaded into Django at runtime.

## Project Structure

`image[ /mnt/c/Users/karti/Pictures/Screenshots/Screenshot 2025-02-02 003454.png]: # Path to the image file `
