# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu.
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas:
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title: str, director: str, budget: int):
        self.title = title
        self.director = director
        self.budget = budget

    def was_expensive(self):
        if self.budget > 100000000:
            return True
        else:
            return False

Movies = []

movie1 = Movie("Filmas1", "Direktorius1", 200000)
movie2 = Movie("Filmas2", "Direktorius2", 500000000)
movie3 = Movie("Filmas3", "Direktorius3", 500)

Movies.append(movie1)
Movies.append(movie2)
Movies.append(movie3)

for Movie in Movies:
    print(Movie.title, Movie.director, Movie.budget)

print(movie1.was_expensive())
print(movie2.was_expensive())
print(movie3.was_expensive())

# ats:
# Filmas1 Direktorius1 200000
# Filmas2 Direktorius2 500000000
# Filmas3 Direktorius3 500
# False
# True
# False


