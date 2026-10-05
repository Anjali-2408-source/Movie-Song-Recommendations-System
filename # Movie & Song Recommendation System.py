# Movie & Song Recommendation System

print("===== Movie & Song Recommendation System =====")

print("\nAvailable Genres:")
print("1. Action")
print("2. Comedy")
print("3. Romance")
print("4. Thriller")
print("5. Science Fiction")

genre = input("\nEnter your favourite genre: ").lower()

recommendations = {
    "action": {
        "movies": ["Avengers", "John Wick", "Mission Impossible"],
        "songs": ["Believer", "Warriors", "Centuries"]
    },

    "comedy": {
        "movies": ["The Mask", "Home Alone", "Jumanji"],
        "songs": ["Happy", "Dance Monkey", "Uptown Funk"]
    },

    "romance": {
        "movies": ["The Notebook", "Titanic", "La La Land"],
        "songs": ["Perfect", "Love Story", "Photograph"]
    },

    "thriller": {
        "movies": ["Inception", "Gone Girl", "Shutter Island"],
        "songs": ["Lovely", "Demons", "Control"]
    },

    "science fiction": {
        "movies": ["Interstellar", "The Matrix", "Avatar"],
        "songs": ["Space Song", "Starman", "Midnight City"]
    }
}

if genre in recommendations:

    print("\n===== RECOMMENDATIONS =====")

    print("\nRecommended Movies:")
    for movie in recommendations[genre]["movies"]:
        print("-", movie)

    print("\nRecommended Songs:")
    for song in recommendations[genre]["songs"]:
        print("-", song)

else:
    print("\nSorry! This genre is not available.")
    print("Please choose from the available genres.")