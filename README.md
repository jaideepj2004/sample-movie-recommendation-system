# Movie Recommendation System

A full-stack movie recommendation system with an interactive frontend built using HTML, CSS, and JavaScript, and a robust backend powered by Python Flask.

## Features

✨ **Browse Movies** - View a collection of popular movies with ratings and descriptions

🔍 **Search Functionality** - Search movies by title, genre, or tags

🎯 **Smart Recommendations** - Get personalized movie recommendations based on genre and tag similarities

🎨 **Filter Options** - Filter movies by genre, year, and minimum rating

📱 **Responsive Design** - Beautiful gradient UI that works on all devices

## Tech Stack

### Frontend
- **HTML5** - Structure and content
- **CSS3** - Styling with gradients and animations
- **JavaScript (Vanilla)** - Dynamic functionality and API interactions

### Backend
- **Python Flask** - RESTful API server
- **Flask-CORS** - Cross-origin resource sharing support

## Project Structure

```
sample-movie-recommendation-system/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Main HTML page
├── static/
│   ├── style.css          # Stylesheet
│   └── script.js          # JavaScript logic
└── README.md              # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/jaideepj2004/sample-movie-recommendation-system.git
   cd sample-movie-recommendation-system
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## API Endpoints

### Get All Movies
```
GET /api/movies
```
Returns all movies in the database.

### Search Movies
```
GET /api/search?query={search_term}
```
Search movies by title, genre, or tags.

### Get Recommendations
```
GET /api/recommend/{movie_id}
```
Get movie recommendations based on a specific movie.

### Get Single Movie
```
GET /api/movie/{movie_id}
```
Get details of a specific movie.

## How It Works

### Recommendation Algorithm

The system uses a simple but effective content-based filtering approach:

1. **Genre Matching** - Compares genres between movies (weighted x2)
2. **Tag Matching** - Matches similar tags (themes, moods, elements)
3. **Rating Boost** - Factors in movie ratings to prioritize quality

Similarity Score = (Genre Matches × 2) + Tag Matches + (Rating / 10)

## Features in Detail

### Search & Filter
- Real-time search across titles, genres, and tags
- Filter by genre (Action, Comedy, Drama, etc.)
- Filter by year (2020-2024)
- Filter by minimum rating (7+, 8+, 9+)

### Movie Cards
- Movie posters
- Title, year, and rating
- Genre information
- Brief description
- Click to get recommendations

### Recommendations
- Click any movie to get 6 similar movies
- Smooth scroll to recommendations section
- Chain recommendations by clicking suggested movies

## Sample Movie Database

The application includes 20 carefully selected movies spanning multiple genres:
- Drama
- Action
- Sci-Fi
- Thriller
- Comedy
- Animation
- And more!

## Future Enhancements

📀 **User Ratings** - Allow users to rate movies

👤 **User Profiles** - Personalized recommendations based on viewing history

📊 **Advanced Algorithm** - Collaborative filtering using user data

🎞️ **Real API Integration** - Connect to TMDB or OMDB APIs for real movie data

💾 **Database** - Add PostgreSQL or MongoDB for persistent storage

⭐ **Favorites** - Save and manage favorite movies

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Jaideep Jaiswal**
- GitHub: [@jaideepj2004](https://github.com/jaideepj2004)

## Acknowledgments

- Movie data is sample/placeholder data for demonstration purposes
- UI inspired by modern streaming platforms
- Built as a learning project to demonstrate full-stack development skills

---

🎬 **Enjoy discovering your next favorite movie!** 🎬