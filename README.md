# Sample Movie Recommendation System

A lightweight **movie recommendation web app** built with **Flask** that provides search and similarity-based recommendations for 20 curated films using genre and tag matching.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Movie Catalogue](#movie-catalogue)
- [Recommendation Algorithm](#recommendation-algorithm)
- [Project Structure](#project-structure)
- [API Reference](#api-reference)
- [Setup & Running](#setup--running)

---

## Overview

The system serves a catalogue of **20 hand-picked high-rated movies** with genre and tag metadata. Users can browse all movies, search by title/genre/tag, or get recommendations similar to a movie they already like — all through a REST JSON API and an HTML/CSS frontend.

---

## Features

- 20 movies with genre, year, rating, description, and tags
- Full-text search across title, genre, and tags
- Similarity-based recommendations (genre + tag overlap + rating weighting)
- REST JSON API with Flask-CORS for cross-origin support
- Clean HTML/CSS/JS frontend

---

## Tech Stack

| Component | Technology |
|---|---|
| Backend | Python, Flask |
| CORS | Flask-CORS |
| Frontend | HTML, CSS, JavaScript (`templates/`, `static/`) |
| Data Store | In-memory Python list (no database) |

---

## Movie Catalogue

| ID | Title | Year | Rating |
|---|---|---|---|
| 1 | The Shawshank Redemption | 1994 | 9.3 |
| 2 | The Godfather | 1972 | 9.2 |
| 3 | The Dark Knight | 2008 | 9.0 |
| 4 | Pulp Fiction | 1994 | 8.9 |
| 5 | Forrest Gump | 1994 | 8.8 |
| 6 | Inception | 2010 | 8.8 |
| 7 | The Matrix | 1999 | 8.7 |
| 8 | Goodfellas | 1990 | 8.7 |
| 9 | Interstellar | 2014 | 8.6 |
| 10 | The Silence of the Lambs | 1991 | 8.6 |
| ... | and 10 more | | |

---

## Recommendation Algorithm

When you request recommendations for movie `X`:

```python
for each other_movie:
    genre_match = len(X.genres ∩ movie.genres)      # genre overlap count
    tag_match   = len(X.tags ∩ movie.tags)           # tag overlap count
    score       = (genre_match × 2) + tag_match + (movie.rating / 10)

# Sort by score descending, return top 6
```

Movies with more genre and tag overlap plus a high rating score highest.

---

## Project Structure

```
sample-movie-recommendation-system/
├── app.py               # Flask app + movie database + recommendation logic
├── requirements.txt     # Dependencies (flask, flask-cors)
├── templates/
│   └── index.html       # Web UI
├── static/              # CSS / JS assets
├── .gitignore
└── README.md
```

---

## API Reference

### `GET /`
Returns the main web interface.

### `GET /api/movies`
Returns all 20 movies.
```json
{ "movies": [...], "total": 20 }
```

### `GET /api/search?query=<text>`
Search movies by title, genre, or tag.
```json
{ "movies": [...], "total": 3, "query": "sci-fi" }
```

### `GET /api/recommend/<movie_id>`
Returns up to 6 movies similar to the given movie ID.
```json
{
  "movie_title": "Inception",
  "recommendations": [...],
  "total": 6
}
```

### `GET /api/movie/<movie_id>`
Returns a single movie by ID.

---

## Setup & Running

```bash
git clone https://github.com/jaideepj2004/sample-movie-recommendation-system.git
cd sample-movie-recommendation-system
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`.
