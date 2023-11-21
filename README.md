# Bookmark

Bookmark README

## Description

Bookmark is a lab/challenge bookmark repo.

## Table of Contents

- [Installation](#Installation)

## Installation

To run Bookmark platform on your local machine, follow these steps:

```bash
# Clone the repository
git clone https://github.com/7arbinho/bookmark.git

# Change directory to the project folder
cd bookmark

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the development server
python manage.py runserver

# Go to swagger documentation
http://0.0.0.0:8000/swagger

# Hints:
token format: Bearer Token
you can pass it as: Bearer + your_token in Authorization

you can use this user for demo:
username: ali
password: ali@1234

in this endpoint: /bookmark/bookmarks/bookmark-item/
types are [Lab, Challenge].