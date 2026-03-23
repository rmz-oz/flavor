# flavor

A Django web app for browsing and reviewing restaurants. Built as a course project.

## What it does

- Browse restaurants by category, location, and price range
- Search by name or description
- View restaurant details and customer reviews
- Star ratings (1-5) with average displayed per restaurant
- Admin panel for managing restaurant/category data

## Tech

- Django 6
- SQLite
- Plain HTML/CSS templates

## Running locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # then fill in SECRET_KEY
python manage.py migrate
python manage.py runserver
```

## Models

- `Restaurant` — name, description, address, phone, price range, category, location
- `Category` — e.g. Italian, Turkish, Fast Food
- `Location` — city + district
- `Review` — author, rating, text, linked to a restaurant
