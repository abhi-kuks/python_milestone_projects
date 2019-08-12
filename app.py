"""
Enter 'a' to add movie, 'l' to see the movie, 'f' to find a movie and 'q' to quit:

- Add movies
- See movies
-Find a movie
-stop running the program

Tasks:
[]: Decide to where to store
[]:Show the user the main interface and get their input
[]:ALlow users to add movie
[]:show all their movies
[]:find a movie
[]:stop running the program when they type 'q'
"""

movies=[]
"""
movie={
    'name':...(str),
    'director':...(str),
    'year':...(int) 
    }
"""

def menu():
    user_input=input("Enter 'a' to add movie, 'l' to see the movies, 'f' to find a movie and 'q' to quit: ")

    while user_input != 'q':
        if user_input == "a":
            add_movies()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movies()
        else:
            print('Unknown command please try again')
        user_input = input("Enter 'a' to add movie, 'l' to see the movie, 'f' to find a movie and 'q' to quit: ")


def add_movies():
    name = input('Enter the movie name: ')
    director = input('Enter the movie director: ')
    year = input('Enter the movie year: ')

    movies.append({
        'name':name,
        'director':director,
        'year':year
    })

def show_movies(movies_list):
    for movie in movies_list:
        show_movie_details(movie)

def show_movie_details(movie):
    print(f"Name : {movie['name']}")
    print(f"Director : {movie['director']}")
    print(f"Release Year: {movie['year']}")

        # print('\n')

def find_movies():
    find_by=input("What property of the movie you are looking for? ")
    looking_for=input("What are you searching for? ")

    found_movies=find_by_attribute(movies,looking_for,lambda x:x[find_by])
    show_movies(found_movies)


def find_by_attribute(items,expected,finder):
    found=[]
    for i in items:
        if finder(i)==expected:
            found.append(i)
    return found

menu()
