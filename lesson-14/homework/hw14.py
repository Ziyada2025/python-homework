1. Task: JSON Parsing
o	write a Python script that reads the students.jon JSON file and prints details of each student.

import json 
path='C:\\Users\\Ziyada\\Desktop\\student.json'
with open(path, 'r') as file: 
    json_data=json.load(file) 
print(json_data) 
for student in  json_data['students']: 
    print(f'Students id is {student['id']}, name is {student['name']}, age is {student['age']}, grade is {student['grade']}')

2. Task: Weather API
i.	Use this url : https://openweathermap.org/
ii.	Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
import requests 
import json 
API_KEY = "8fe54f896563d13b091371916aaee90e"  
CITY_NAME = "Tashkent" 
URL=f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric"
response=requests.get(URL) 
data=response.json() 
print(data)

3.  Task: JSON Modification
i.	Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.

import json
import os

class BookManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.books = self.load_books()
    
    def load_books(self):
        """Load books from JSON file and fix data structure if needed"""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    
                # Fix the data structure if it contains strings instead of dictionaries
                fixed_books = []
                for item in data:
                    if isinstance(item, dict):
                        # It's already a book dictionary - good!
                        fixed_books.append(item)
                    elif isinstance(item, str):
                        # It's a string - convert it to a book dictionary
                        fixed_books.append({
                            'title': item,
                            'author': 'Unknown',
                            'year': 'Unknown',
                            'genre': 'Unknown',
                            'isbn': 'Unknown'
                        })
                
                # Save the fixed structure back to file
                if fixed_books != data:
                    with open(self.file_path, 'w', encoding='utf-8') as file:
                        json.dump(fixed_books, file, indent=4)
                    print("⚠️  Fixed book data structure automatically!")
                
                return fixed_books
            else:
                # Create file with empty list if it doesn't exist
                with open(self.file_path, 'w', encoding='utf-8') as file:
                    json.dump([], file)
                return []
                
        except (json.JSONDecodeError, Exception) as e:
            print(f"Error loading books: {e}")
            # Return empty list if there's any error
            return []
    
    def save_books(self):
        """Save books to JSON file"""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(self.books, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving books: {e}")
            return False
    
    def display_books(self):
        """Display all books"""
        if not self.books:
            print("No books available.")
            return
        
        print("\n" + "="*50)
        print("📚 BOOK COLLECTION")
        print("="*50)
        
        for i, book in enumerate(self.books, 1):
            # Safe display - handle both dictionary and string formats
            if isinstance(book, dict):
                print(f"{i}. Title: {book.get('title', 'N/A')}")
                print(f"   Author: {book.get('author', 'N/A')}")
                print(f"   Year: {book.get('year', 'N/A')}")
                print(f"   Genre: {book.get('genre', 'N/A')}")
                print(f"   ISBN: {book.get('isbn', 'N/A')}")
            else:
                # If it's still a string (shouldn't happen after fix, but just in case)
                print(f"{i}. Title: {book}")
                print(f"   Author: Unknown")
                print(f"   Year: Unknown")
                print(f"   Genre: Unknown")
                print(f"   ISBN: Unknown")
            print("-" * 30)
    
    def add_book(self):
        """Add a new book"""
        print("\n➕ ADD NEW BOOK")
        print("-" * 20)
        
        title = input("Enter book title: ").strip()
        if not title:
            print("Error: Title is required!")
            return
        
        author = input("Enter author: ").strip()
        year = input("Enter publication year: ").strip()
        genre = input("Enter genre: ").strip()
        isbn = input("Enter ISBN: ").strip()
        
        # Check if book with same title already exists
        for book in self.books:
            book_title = book.get('title', '') if isinstance(book, dict) else str(book)
            if book_title.lower() == title.lower():
                print(f"Error: Book '{title}' already exists!")
                return
        
        new_book = {
            'title': title,
            'author': author or 'Unknown',
            'year': year or 'Unknown',
            'genre': genre or 'Unknown',
            'isbn': isbn or 'Unknown'
        }
        
        self.books.append(new_book)
        if self.save_books():
            print(f"✅ Book '{title}' added successfully!")
        else:
            print("❌ Failed to save book!")
    
    def update_book(self):
        """Update existing book information"""
        if not self.books:
            print("No books available to update.")
            return
        
        self.display_books()
        
        try:
            book_num = int(input("\nEnter book number to update: ")) - 1
            if 0 <= book_num < len(self.books):
                book = self.books[book_num]
                
                # If book is a string, convert it to dictionary first
                if isinstance(book, str):
                    book = {
                        'title': book,
                        'author': 'Unknown',
                        'year': 'Unknown',
                        'genre': 'Unknown',
                        'isbn': 'Unknown'
                    }
                    self.books[book_num] = book
                
                print(f"\nUpdating: {book['title']}")
                print("Leave field empty to keep current value.")
                
                new_title = input(f"New title [{book['title']}]: ").strip()
                new_author = input(f"New author [{book['author']}]: ").strip()
                new_year = input(f"New year [{book['year']}]: ").strip()
                new_genre = input(f"New genre [{book['genre']}]: ").strip()
                new_isbn = input(f"New ISBN [{book['isbn']}]: ").strip()
                
                # Update only if new value provided
                if new_title:
                    book['title'] = new_title
                if new_author:
                    book['author'] = new_author
                if new_year:
                    book['year'] = new_year
                if new_genre:
                    book['genre'] = new_genre
                if new_isbn:
                    book['isbn'] = new_isbn
                
                if self.save_books():
                    print("✅ Book updated successfully!")
                else:
                    print("❌ Failed to update book!")
            else:
                print("❌ Invalid book number!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def delete_book(self):
        """Delete a book"""
        if not self.books:
            print("No books available to delete.")
            return
        
        self.display_books()
        
        try:
            book_num = int(input("\nEnter book number to delete: ")) - 1
            if 0 <= book_num < len(self.books):
                # Get book title for confirmation message
                book_to_delete = self.books[book_num]
                book_title = book_to_delete.get('title', '') if isinstance(book_to_delete, dict) else str(book_to_delete)
                
                confirm = input(f"Are you sure you want to delete '{book_title}'? (y/n): ").lower()
                
                if confirm == 'y':
                    deleted_book = self.books.pop(book_num)
                    deleted_title = deleted_book.get('title', '') if isinstance(deleted_book, dict) else str(deleted_book)
                    
                    if self.save_books():
                        print(f"✅ Book '{deleted_title}' deleted successfully!")
                    else:
                        print("❌ Failed to delete book!")
                else:
                    print("Deletion cancelled.")
            else:
                print("❌ Invalid book number!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def search_books(self):
        """Search books by title or author"""
        if not self.books:
            print("No books available to search.")
            return
        
        search_term = input("Enter title or author to search: ").strip().lower()
        found_books = []
        
        for book in self.books:
            if isinstance(book, dict):
                book_title = book.get('title', '').lower()
                book_author = book.get('author', '').lower()
            else:
                book_title = str(book).lower()
                book_author = 'unknown'
            
            if search_term in book_title or search_term in book_author:
                found_books.append(book)
        
        if found_books:
            print(f"\n🔍 Found {len(found_books)} book(s):")
            for i, book in enumerate(found_books, 1):
                if isinstance(book, dict):
                    print(f"{i}. {book.get('title', 'Unknown')} by {book.get('author', 'Unknown')}")
                else:
                    print(f"{i}. {book} by Unknown")
        else:
            print("❌ No books found matching your search.")

def main():
    file_path = 'C:\\Users\\Ziyada\\Desktop\\books.json'
    manager = BookManager(file_path)
    
    while True:
        print("\n" + "="*40)
        print("📖 BOOK MANAGEMENT SYSTEM")
        print("="*40)
        print("1. 📚 Display all books")
        print("2. ➕ Add new book")
        print("3. ✏️ Update book")
        print("4. 🗑️ Delete book")
        print("5. 🔍 Search books")
        print("6. 🚪 Exit")
        print("-" * 40)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            manager.display_books()
        elif choice == '2':
            manager.add_book()
        elif choice == '3':
            manager.update_book()
        elif choice == '4':
            manager.delete_book()
        elif choice == '5':
            manager.search_books()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    main()

4. Task: Movie Recommendation System
i.	Use this url http://www.omdbapi.com/ to fetch information about movies.
ii.	Create a program that asks users for a movie genre and recommends a random movie from that genre.

import requests
import random
import json

class MovieRecommendationSystem:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://www.omdbapi.com/"
        self.genres = [
            "action", "adventure", "animation", "comedy", "crime", 
            "documentary", "drama", "family", "fantasy", "horror",
            "musical", "mystery", "romance", "sci-fi", "thriller", 
            "war", "western", "biography", "history", "sport"
        ]
    
    def search_movies_by_genre(self, genre, page=1):
        """Search for movies by genre using OMDB API"""
        try:
            params = {
                'apikey': self.api_key,
                's': genre,
                'type': 'movie',
                'page': page
            }
            
            print(f"🔍 Searching for {genre} movies...")
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('Response') == 'True':
                movies = data['Search']
                print(f"✅ Found {len(movies)} movies on page {page}")
                return movies
            else:
                error_msg = data.get('Error', 'Unknown error')
                print(f"❌ API Error: {error_msg}")
                return []
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error: {e}")
            return []
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return []
    
    def get_movie_details(self, imdb_id):
        """Get detailed information about a specific movie"""
        try:
            params = {
                'apikey': self.api_key,
                'i': imdb_id,
                'plot': 'full'
            }
            
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('Response') == 'True':
                return data
            else:
                return None
                
        except Exception as e:
            print(f"❌ Error fetching movie details: {e}")
            return None
    
    def get_random_movie_from_genre(self, genre):
        """Get a random movie from the specified genre"""
        print(f"\n🎬 Looking for {genre.upper()} movies...")
        
        # Try multiple pages to get more results
        all_movies = []
        for page in range(1, 4):  # Try first 3 pages
            movies = self.search_movies_by_genre(genre, page)
            if movies:
                all_movies.extend(movies)
            else:
                break
        
        if not all_movies:
            print(f"❌ No movies found for genre: '{genre}'")
            print("💡 Try these popular genres instead:")
            popular_genres = ["action", "comedy", "drama", "thriller", "romance", "horror"]
            for g in popular_genres:
                if g in self.genres:
                    print(f"   • {g.title()}")
            return None
        
        print(f"📊 Total movies found: {len(all_movies)}")
        
        # Select a random movie
        random_movie = random.choice(all_movies)
        print(f"🎲 Selected: {random_movie.get('Title', 'Unknown')}")
        
        # Get detailed information
        print("📖 Fetching movie details...")
        movie_details = self.get_movie_details(random_movie['imdbID'])
        
        return movie_details if movie_details else random_movie
    
    def display_movie_recommendation(self, movie):
        """Display the movie recommendation in a nice format"""
        print("\n" + "="*70)
        print("🎉 YOUR MOVIE RECOMMENDATION!")
        print("="*70)
        
        if isinstance(movie, dict) and 'Title' in movie:
            # Detailed movie information
            print(f"🎬 Title: {movie.get('Title', 'N/A')}")
            print(f"📅 Year: {movie.get('Year', 'N/A')}")
            print(f"⭐ IMDB Rating: {movie.get('imdbRating', 'N/A')}/10")
            print(f"⏱️ Runtime: {movie.get('Runtime', 'N/A')}")
            print(f"🎭 Genre: {movie.get('Genre', 'N/A')}")
            print(f"📝 Director: {movie.get('Director', 'N/A')}")
            print(f"🎭 Cast: {movie.get('Actors', 'N/A')}")
            print(f"🏆 Awards: {movie.get('Awards', 'N/A')}")
            
            # Display plot (truncated if too long)
            plot = movie.get('Plot', 'N/A')
            if plot != 'N/A' and len(plot) > 200:
                plot = plot[:200] + "..."
            print(f"📖 Plot: {plot}")
            
            # Display poster URL if available
            poster_url = movie.get('Poster')
            if poster_url and poster_url != 'N/A':
                print(f"🖼️ Poster: {poster_url}")
            
            print(f"🔗 IMDB ID: {movie.get('imdbID', 'N/A')}")
            
        else:
            # Basic movie information
            print(f"🎬 Title: {movie.get('Title', 'N/A')}")
            print(f"📅 Year: {movie.get('Year', 'N/A')}")
            print(f"🔗 IMDB ID: {movie.get('imdbID', 'N/A')}")
            print("\n💡 Limited details available for this movie.")
        
        print("="*70)
    
    def show_available_genres(self):
        """Display available genres"""
        print("\n📚 AVAILABLE GENRES:")
        print("-" * 40)
        genres_per_line = 4
        for i in range(0, len(self.genres), genres_per_line):
            line = ""
            for j in range(genres_per_line):
                if i + j < len(self.genres):
                    genre = self.genres[i + j]
                    line += f"• {genre.title():<12}"
            print(line)
        print("-" * 40)
    
    def search_movie_by_title(self):
        """Search for a specific movie by title"""
        title = input("\nEnter movie title to search: ").strip()
        if not title:
            print("❌ Please enter a movie title.")
            return
        
        try:
            params = {
                'apikey': self.api_key,
                't': title,
                'plot': 'short'
            }
            
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('Response') == 'True':
                print("\n" + "="*50)
                print("🔍 MOVIE FOUND!")
                print("="*50)
                print(f"🎬 Title: {data.get('Title', 'N/A')}")
                print(f"📅 Year: {data.get('Year', 'N/A')}")
                print(f"⭐ IMDB Rating: {data.get('imdbRating', 'N/A')}/10")
                print(f"🎭 Genre: {data.get('Genre', 'N/A')}")
                print(f"📖 Plot: {data.get('Plot', 'N/A')}")
            else:
                print(f"❌ Movie not found: {data.get('Error', 'Unknown error')}")
                
        except Exception as e:
            print(f"❌ Search error: {e}")
    
    def run(self):
        """Main program loop"""
        print("🎬 WELCOME TO MOVIE RECOMMENDATION SYSTEM!")
        print(f"⭐ Using OMDB API | Genres available: {len(self.genres)}")
        print("💡 Discover your next favorite movie!")
        
        while True:
            print("\n" + "="*50)
            print("1. 🎲 Get random movie by genre")
            print("2. 📚 Show all available genres")
            print("3. 🔍 Search for specific movie")
            print("4. 🚪 Exit")
            print("="*50)
            
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                self.show_available_genres()
                genre = input("\nEnter your preferred genre: ").strip().lower()
                
                if genre in self.genres:
                    movie = self.get_random_movie_from_genre(genre)
                    if movie:
                        self.display_movie_recommendation(movie)
                        
                        # Ask if user wants another recommendation
                        another = input("\nWould you like another recommendation? (y/n): ").strip().lower()
                        if another != 'y':
                            print("👋 Happy movie watching!")
                            break
                    else:
                        print("❌ Could not find a movie recommendation. Please try another genre.")
                else:
                    print("❌ Invalid genre! Please choose from the available genres.")
            
            elif choice == '2':
                self.show_available_genres()
            
            elif choice == '3':
                self.search_movie_by_title()
            
            elif choice == '4':
                print("👋 Thanks for using Movie Recommendation System! Goodbye!")
                break
            
            else:
                print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")

def main():
    # Your API key
    API_KEY = "14131f36"
    
    print("🔑 API Key detected! Starting Movie Recommendation System...")
    print("🌐 Connecting to OMDb API...")
    
    # Test the API connection
    try:
        test_params = {'apikey': API_KEY, 'i': 'tt3896198'}
        response = requests.get("http://www.omdbapi.com/", params=test_params)
        if response.status_code == 200:
            print("✅ Successfully connected to OMDb API!")
        else:
            print("❌ Failed to connect to OMDb API")
    except:
        print("❌ Network error - please check your internet connection")
        return
    
    # Start the movie recommendation system
    movie_system = MovieRecommendationSystem(API_KEY)
    movie_system.run()

if __name__ == "__main__":
    main()

