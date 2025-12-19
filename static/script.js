const API_URL = '/api';

let currentMovies = [];

// DOM Elements
const searchInput = document.getElementById('searchInput');
const searchBtn = document.getElementById('searchBtn');
const genreFilter = document.getElementById('genreFilter');
const yearFilter = document.getElementById('yearFilter');
const ratingFilter = document.getElementById('ratingFilter');
const moviesGrid = document.getElementById('moviesGrid');
const recommendationsSection = document.getElementById('recommendationsSection');
const recommendationsGrid = document.getElementById('recommendationsGrid');
const loadingDiv = document.getElementById('loading');
const errorDiv = document.getElementById('error');

// Event Listeners
searchBtn.addEventListener('click', searchMovies);
searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        searchMovies();
    }
});

genreFilter.addEventListener('change', applyFilters);
yearFilter.addEventListener('change', applyFilters);
ratingFilter.addEventListener('change', applyFilters);

// Initialize
loadMovies();

async function loadMovies() {
    showLoading(true);
    hideError();
    try {
        const response = await fetch(`${API_URL}/movies`);
        if (!response.ok) throw new Error('Failed to load movies');
        
        const data = await response.json();
        currentMovies = data.movies;
        displayMovies(currentMovies);
    } catch (error) {
        showError('Failed to load movies. Please try again later.');
        console.error('Error loading movies:', error);
    } finally {
        showLoading(false);
    }
}

async function searchMovies() {
    const query = searchInput.value.trim();
    if (!query) {
        loadMovies();
        return;
    }
    
    showLoading(true);
    hideError();
    try {
        const response = await fetch(`${API_URL}/search?query=${encodeURIComponent(query)}`);
        if (!response.ok) throw new Error('Search failed');
        
        const data = await response.json();
        currentMovies = data.movies;
        displayMovies(currentMovies);
    } catch (error) {
        showError('Search failed. Please try again.');
        console.error('Error searching movies:', error);
    } finally {
        showLoading(false);
    }
}

function applyFilters() {
    const genre = genreFilter.value;
    const year = yearFilter.value;
    const rating = parseFloat(ratingFilter.value);
    
    let filtered = [...currentMovies];
    
    if (genre !== 'all') {
        filtered = filtered.filter(movie => 
            movie.genre.toLowerCase().includes(genre.toLowerCase())
        );
    }
    
    if (year !== 'all') {
        filtered = filtered.filter(movie => movie.year.toString() === year);
    }
    
    if (rating > 0) {
        filtered = filtered.filter(movie => movie.rating >= rating);
    }
    
    displayMovies(filtered);
}

function displayMovies(movies) {
    if (movies.length === 0) {
        moviesGrid.innerHTML = '<p style="color: white; text-align: center; grid-column: 1/-1;">No movies found.</p>';
        return;
    }
    
    moviesGrid.innerHTML = movies.map(movie => `
        <div class="movie-card" onclick="getRecommendations(${movie.id})">
            <img src="${movie.poster || 'https://via.placeholder.com/250x350?text=No+Poster'}" 
                 alt="${movie.title}" 
                 class="movie-poster"
                 onerror="this.src='https://via.placeholder.com/250x350?text=No+Poster'">
            <div class="movie-info">
                <h3 class="movie-title">${movie.title}</h3>
                <div class="movie-meta">
                    <span class="movie-year">${movie.year}</span>
                    <span class="movie-rating">⭐ ${movie.rating.toFixed(1)}</span>
                </div>
                <p class="movie-genre">${movie.genre}</p>
                <p class="movie-description">${movie.description}</p>
            </div>
        </div>
    `).join('');
}

async function getRecommendations(movieId) {
    showLoading(true);
    hideError();
    try {
        const response = await fetch(`${API_URL}/recommend/${movieId}`);
        if (!response.ok) throw new Error('Failed to get recommendations');
        
        const data = await response.json();
        displayRecommendations(data.recommendations, data.movie_title);
        
        // Scroll to recommendations
        recommendationsSection.scrollIntoView({ behavior: 'smooth' });
    } catch (error) {
        showError('Failed to get recommendations. Please try again.');
        console.error('Error getting recommendations:', error);
    } finally {
        showLoading(false);
    }
}

function displayRecommendations(movies, baseTitle) {
    recommendationsSection.style.display = 'block';
    document.querySelector('.recommendations-section h2').textContent = 
        `Recommended movies based on "${baseTitle}"`;
    
    if (movies.length === 0) {
        recommendationsGrid.innerHTML = '<p style="color: white; text-align: center; grid-column: 1/-1;">No recommendations found.</p>';
        return;
    }
    
    recommendationsGrid.innerHTML = movies.map(movie => `
        <div class="movie-card" onclick="getRecommendations(${movie.id})">
            <img src="${movie.poster || 'https://via.placeholder.com/250x350?text=No+Poster'}" 
                 alt="${movie.title}" 
                 class="movie-poster"
                 onerror="this.src='https://via.placeholder.com/250x350?text=No+Poster'">
            <div class="movie-info">
                <h3 class="movie-title">${movie.title}</h3>
                <div class="movie-meta">
                    <span class="movie-year">${movie.year}</span>
                    <span class="movie-rating">⭐ ${movie.rating.toFixed(1)}</span>
                </div>
                <p class="movie-genre">${movie.genre}</p>
                <p class="movie-description">${movie.description}</p>
            </div>
        </div>
    `).join('');
}

function showLoading(show) {
    loadingDiv.style.display = show ? 'block' : 'none';
}

function showError(message) {
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
}

function hideError() {
    errorDiv.style.display = 'none';
}