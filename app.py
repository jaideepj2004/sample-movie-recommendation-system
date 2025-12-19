from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Sample movie database
MOVIES = [
    {
        "id": 1,
        "title": "The Shawshank Redemption",
        "year": 1994,
        "genre": "Drama",
        "rating": 9.3,
        "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "poster": "https://via.placeholder.com/250x350?text=Shawshank",
        "tags": ["prison", "friendship", "hope", "redemption"]
    },
    {
        "id": 2,
        "title": "The Godfather",
        "year": 1972,
        "genre": "Drama, Crime",
        "rating": 9.2,
        "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "poster": "https://via.placeholder.com/250x350?text=Godfather",
        "tags": ["mafia", "family", "crime", "power"]
    },
    {
        "id": 3,
        "title": "The Dark Knight",
        "year": 2008,
        "genre": "Action, Crime, Drama",
        "rating": 9.0,
        "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests.",
        "poster": "https://via.placeholder.com/250x350?text=Dark+Knight",
        "tags": ["superhero", "action", "crime", "batman"]
    },
    {
        "id": 4,
        "title": "Pulp Fiction",
        "year": 1994,
        "genre": "Crime, Drama",
        "rating": 8.9,
        "description": "The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption.",
        "poster": "https://via.placeholder.com/250x350?text=Pulp+Fiction",
        "tags": ["crime", "violence", "nonlinear", "cult"]
    },
    {
        "id": 5,
        "title": "Forrest Gump",
        "year": 1994,
        "genre": "Drama, Romance",
        "rating": 8.8,
        "description": "The presidencies of Kennedy and Johnson, the Vietnam War, and other historical events unfold from the perspective of an Alabama man.",
        "poster": "https://via.placeholder.com/250x350?text=Forrest+Gump",
        "tags": ["inspiring", "life", "history", "heartwarming"]
    },
    {
        "id": 6,
        "title": "Inception",
        "year": 2010,
        "genre": "Action, Sci-Fi, Thriller",
        "rating": 8.8,
        "description": "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea.",
        "poster": "https://via.placeholder.com/250x350?text=Inception",
        "tags": ["dreams", "mindbending", "heist", "scifi"]
    },
    {
        "id": 7,
        "title": "The Matrix",
        "year": 1999,
        "genre": "Action, Sci-Fi",
        "rating": 8.7,
        "description": "A computer hacker learns about the true nature of his reality and his role in the war against its controllers.",
        "poster": "https://via.placeholder.com/250x350?text=The+Matrix",
        "tags": ["scifi", "action", "philosophy", "cyberpunk"]
    },
    {
        "id": 8,
        "title": "Goodfellas",
        "year": 1990,
        "genre": "Crime, Drama",
        "rating": 8.7,
        "description": "The story of Henry Hill and his life in the mob, covering his relationship with his wife and his partners in crime.",
        "poster": "https://via.placeholder.com/250x350?text=Goodfellas",
        "tags": ["mafia", "crime", "biography", "violence"]
    },
    {
        "id": 9,
        "title": "Interstellar",
        "year": 2014,
        "genre": "Adventure, Drama, Sci-Fi",
        "rating": 8.6,
        "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "poster": "https://via.placeholder.com/250x350?text=Interstellar",
        "tags": ["space", "scifi", "time", "emotional"]
    },
    {
        "id": 10,
        "title": "The Silence of the Lambs",
        "year": 1991,
        "genre": "Crime, Drama, Thriller",
        "rating": 8.6,
        "description": "A young FBI cadet must receive the help of an incarcerated cannibal killer to catch another serial killer.",
        "poster": "https://via.placeholder.com/250x350?text=Silence+Lambs",
        "tags": ["thriller", "psychological", "serial killer", "suspense"]
    },
    {
        "id": 11,
        "title": "Parasite",
        "year": 2019,
        "genre": "Comedy, Drama, Thriller",
        "rating": 8.5,
        "description": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
        "poster": "https://via.placeholder.com/250x350?text=Parasite",
        "tags": ["social", "satire", "thriller", "korean"]
    },
    {
        "id": 12,
        "title": "The Avengers",
        "year": 2012,
        "genre": "Action, Adventure, Sci-Fi",
        "rating": 8.0,
        "description": "Earth's mightiest heroes must come together to stop an alien invasion.",
        "poster": "https://via.placeholder.com/250x350?text=Avengers",
        "tags": ["superhero", "action", "marvel", "teamup"]
    },
    {
        "id": 13,
        "title": "Joker",
        "year": 2019,
        "genre": "Crime, Drama, Thriller",
        "rating": 8.4,
        "description": "In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society.",
        "poster": "https://via.placeholder.com/250x350?text=Joker",
        "tags": ["psychological", "dark", "villain", "society"]
    },
    {
        "id": 14,
        "title": "The Prestige",
        "year": 2006,
        "genre": "Drama, Mystery, Sci-Fi",
        "rating": 8.5,
        "description": "After a tragic accident, two stage magicians engage in a battle to create the ultimate illusion.",
        "poster": "https://via.placeholder.com/250x350?text=The+Prestige",
        "tags": ["magic", "mystery", "rivalry", "twist"]
    },
    {
        "id": 15,
        "title": "Gladiator",
        "year": 2000,
        "genre": "Action, Adventure, Drama",
        "rating": 8.5,
        "description": "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family.",
        "poster": "https://via.placeholder.com/250x350?text=Gladiator",
        "tags": ["historical", "action", "revenge", "epic"]
    },
    {
        "id": 16,
        "title": "The Lion King",
        "year": 1994,
        "genre": "Animation, Adventure, Drama",
        "rating": 8.5,
        "description": "Lion prince Simba flees his kingdom after the murder of his father, only to learn the true meaning of responsibility.",
        "poster": "https://via.placeholder.com/250x350?text=Lion+King",
        "tags": ["animated", "family", "disney", "coming of age"]
    },
    {
        "id": 17,
        "title": "Spider-Man: Into the Spider-Verse",
        "year": 2018,
        "genre": "Animation, Action, Adventure",
        "rating": 8.4,
        "description": "Teen Miles Morales becomes Spider-Man and joins other Spider-People from different dimensions.",
        "poster": "https://via.placeholder.com/250x350?text=Spider-Verse",
        "tags": ["animated", "superhero", "multiverse", "coming of age"]
    },
    {
        "id": 18,
        "title": "Dune",
        "year": 2021,
        "genre": "Action, Adventure, Drama",
        "rating": 8.0,
        "description": "Paul Atreides arrives on the desert planet Arrakis to oversee the spice production, but conspiracy and betrayal await.",
        "poster": "https://via.placeholder.com/250x350?text=Dune",
        "tags": ["scifi", "epic", "desert", "prophecy"]
    },
    {
        "id": 19,
        "title": "Everything Everywhere All at Once",
        "year": 2022,
        "genre": "Action, Adventure, Comedy",
        "rating": 8.1,
        "description": "An aging Chinese immigrant is swept up in an insane adventure in which she alone can save the multiverse.",
        "poster": "https://via.placeholder.com/250x350?text=EEAAO",
        "tags": ["multiverse", "comedy", "action", "family"]
    },
    {
        "id": 20,
        "title": "Top Gun: Maverick",
        "year": 2022,
        "genre": "Action, Drama",
        "rating": 8.3,
        "description": "After thirty years, Maverick is still pushing the envelope as a top naval aviator.",
        "poster": "https://via.placeholder.com/250x350?text=Top+Gun",
        "tags": ["action", "aviation", "sequel", "military"]
    }
]

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/movies', methods=['GET'])
def get_movies():
    """Get all movies"""
    return jsonify({
        'movies': MOVIES,
        'total': len(MOVIES)
    })

@app.route('/api/search', methods=['GET'])
def search_movies():
    """Search movies by title or genre"""
    query = request.args.get('query', '').lower()
    
    if not query:
        return jsonify({'movies': MOVIES, 'total': len(MOVIES)})
    
    filtered_movies = [
        movie for movie in MOVIES
        if query in movie['title'].lower() or 
           query in movie['genre'].lower() or
           any(query in tag for tag in movie['tags'])
    ]
    
    return jsonify({
        'movies': filtered_movies,
        'total': len(filtered_movies),
        'query': query
    })

@app.route('/api/recommend/<int:movie_id>', methods=['GET'])
def recommend_movies(movie_id):
    """Get movie recommendations based on a movie ID"""
    # Find the base movie
    base_movie = next((m for m in MOVIES if m['id'] == movie_id), None)
    
    if not base_movie:
        return jsonify({'error': 'Movie not found'}), 404
    
    # Simple recommendation algorithm:
    # 1. Find movies with similar genres
    # 2. Find movies with similar tags
    # 3. Prioritize highly rated movies
    
    recommendations = []
    base_genres = set(base_movie['genre'].lower().split(', '))
    base_tags = set(base_movie['tags'])
    
    for movie in MOVIES:
        if movie['id'] == movie_id:
            continue
        
        # Calculate similarity score
        movie_genres = set(movie['genre'].lower().split(', '))
        movie_tags = set(movie['tags'])
        
        genre_match = len(base_genres & movie_genres)
        tag_match = len(base_tags & movie_tags)
        
        similarity_score = (genre_match * 2) + tag_match + (movie['rating'] / 10)
        
        if similarity_score > 0:
            recommendations.append({
                **movie,
                'similarity_score': similarity_score
            })
    
    # Sort by similarity score and return top 6
    recommendations.sort(key=lambda x: x['similarity_score'], reverse=True)
    top_recommendations = recommendations[:6]
    
    # Remove similarity score from response
    for rec in top_recommendations:
        rec.pop('similarity_score', None)
    
    return jsonify({
        'movie_title': base_movie['title'],
        'recommendations': top_recommendations,
        'total': len(top_recommendations)
    })

@app.route('/api/movie/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    """Get a specific movie by ID"""
    movie = next((m for m in MOVIES if m['id'] == movie_id), None)
    
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404
    
    return jsonify({'movie': movie})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)