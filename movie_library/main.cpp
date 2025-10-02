//CS Movie Library
/*Create an application that manages your Movie Library using structures to store movie details and enumerations for menu options. Your program should persist movie data by reading from and writing to an external file in CSV format.

Main menu needs to allow our user to load the library from a file (I will use a different one than the example one I have given you), view all movies, add a movie, delete a movie, and search movies.

The search menu should allow the user to select what they would like to search by, then the specific value they would like to search. */
#include <iostream>
#include <limits>
#include <fstream>
#include <iomanip>
#include <vector>

using namespace std;

int input(){ 
    int input=0;   
    while(!(cin >> input)){
        cout<<"Please enter a number option: "<<endl;
        cin.clear();
        cin.ignore(10000);
    }
    return input;
    }


struct Movie{
    string title;
    string director;
    int year;
    string genre;
    string rating;
};

void write(const vector<Movie>& movies, string filename = "movies.csv"){
    ofstream file;
    file.open(filename); //create or open file
    if (file.is_open()){
        file << "Movie Name,Director,Year,Genre,Rating\n";
        for (Movie i:movies){
            file << i.title << "," << i.director<< ','<< i.year<< ','<< i.genre<< ','<< i.rating << "\n";
        }
    file.close();}
}

vector<Movie> read(string filename = "movies.csv"){
    ifstream file;
    string line;
    vector<Movie> movies;

    file.open(filename);

    if (file.is_open()){
        getline(file, line); //skip header line
        while(getline(file,line)){
            istringstream iss(line);
            string item;
            Movie movie;


            getline(iss, item,',');
            movie.title = item;

            getline(iss, item,',');
            movie.director = item;

            getline(iss, item,',');
            movie.year = stoi(item);

            getline(iss, item,',');
            movie.genre = item;

            getline(iss, item,',');
            movie.rating = item;

            movies.push_back(movie);
        }
        file.close();
    }
    
    return movies;
}

void add_movie(vector<Movie>& movies){
    Movie newMovie;
    cout << "Enter movie title: ";
    cin.ignore();
    getline(cin, newMovie.title);
    cout << "Enter director name: ";
    getline(cin, newMovie.director);
    cout << "Enter release year: ";
    cin >> newMovie.year;
    cin.ignore();
    cout << "Enter genre: ";
    getline(cin, newMovie.genre);
    cout << "Enter rating: ";
    getline(cin, newMovie.rating);
    movies.push_back(newMovie);
    cout << "Movie added successfully!\n\n";
}

vector<Movie> remove_movie(vector<Movie>& movies, string title){
    for (int i = 0; i < movies.size(); ++i) {
        if (movies[i].title == title) {
            movies.erase(movies.begin() + i);
            cout  << title << " removed successfully!\n\n";
            return movies;
        }
    }
}

enum SearchOption {
    Title = 1,
    Director,
    Year,
    Genre,
    Rating
};

vector<Movie> search_movies(const vector<Movie>& movies, SearchOption option, const string& value){
    vector<Movie> results;
    for (const Movie& movie : movies) {
        switch (option) {
            case Title:
                if (movie.title.find(value) != string::npos) {
                    results.push_back(movie);
                }
                break;
            case Director:
                if (movie.director.find(value) != string::npos) {
                    results.push_back(movie);
                }
                break;
            case Year:
                if (to_string(movie.year) == value) {
                    results.push_back(movie);
                }
                break;
            case Genre:
                if (movie.genre.find(value) != string::npos) {
                    results.push_back(movie);
                }
                break;
            case Rating:
                if (movie.rating.find(value) != string::npos) {
                    results.push_back(movie);
                }
                break;
        }
    }
    return results;
}

void display_movies(const vector<Movie>& movies){
    for (int i = 0; i < movies.size(); ++i) {
        cout << ", Title: " << movies[i].title 
             << ", Director: " << movies[i].director << ", Year: " << movies[i].year
             << ", Genre: " << movies[i].genre << ", Rating: " << movies[i].rating << endl;
    }
}


enum MenuOption {
    ViewMovies = 1,
    AddMovie,
    DeleteMovie,
    SearchMovies,
    Exit
};

int main(){
    vector<Movie> movies;
    string filename;
    while (true) {
    cout << "What is your Movie Library?" << endl;
    cin >> filename;
    movies = read(filename);
    if (movies.empty()){
        cout << "No movies found in the library. Starting with an empty library.\n\n";
    }
    else break;}
    int choice = 0;
    while (choice != Exit){
        cout << "Menu: \n1. View Movies\n2. Add Movie\n3. Delete Movie\n4. Search Movies\n5. Exit\nEnter your choice: ";
        choice = input();
        switch (choice){
            case ViewMovies:{
                display_movies(movies);
                break;
            }case AddMovie:{
                add_movie(movies);
                write(movies, filename);
                break;
            }case DeleteMovie:{
                string name;
                cout << "Enter movie name to delete: ";
                getline(cin, name);
                movies = remove_movie(movies, name);
                write(movies, filename);
                break;
            }case SearchMovies:{
                int search_choice;
                string search_value;
                cout << "Search by:\n1. Title\n2. Director\n3. Year\n4. Genre\n5. Rating\nEnter your choice: ";
                search_choice = input();
                cout << "Enter search value: ";
                cin.ignore();
                getline(cin, search_value);
                {
                    vector<Movie> results = search_movies(movies, static_cast<SearchOption>(search_choice), search_value);
                    if (results.empty()) {
                        cout << "No movies found matching the criteria.\n\n";
                    } else {
                        display_movies(results);
                    }
                }
                break;
            }case Exit:{
                cout << "Exiting the program. Goodbye!\n";
                break;
            }default:{
                cout << "Invalid choice. Please try again.\n\n";}
        }
    }
    
    return 0;
}