from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Film(Base):
    __tablename__ = "films"  # Use lowercase for table names

    id = Column(Integer, primary_key=True, index=True)
    film_name = Column(String, index=True)
    year_produced = Column(String, index=True)  # Consider changing to Integer or Date
    image_url = Column(String, index=True)
    run_time = Column(String, index=True)
    imdb_rating = Column(Float, index=True)
    description = Column(String, index=True)
    meta_score = Column(Float, index=True)
    gross = Column(Float, index=True)
    votes = Column(Integer, index=True)

    movies_directors = relationship("FilmsDirectors", back_populates="film")
    films_stars = relationship("FilmsStars", back_populates="film")
    films_genres = relationship("FilmsGenres", back_populates="film")


class FilmsDirectors(Base):
    __tablename__ = "films_directors"

    film_id = Column(Integer, ForeignKey("films.id"), primary_key=True)
    directors_id = Column(Integer, ForeignKey("directors.id"), primary_key=True) 

    film = relationship("Film", back_populates="movies_directors")
    director = relationship("Director", back_populates="films_directors")


class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    direct_desc = Column(String, index=True)
    direct_award=Column(String,index=True)

    films_directors = relationship("FilmsDirectors", back_populates="director")


class FilmsStars(Base):
    __tablename__ = "films_stars"

    film_id = Column(Integer, ForeignKey("films.id"), primary_key=True)
    stars_id = Column(Integer, ForeignKey("stars.id"), primary_key=True) 

    film = relationship("Film", back_populates="films_stars")
    star = relationship("Star", back_populates="films_stars")


class Star(Base):
    __tablename__ = "stars"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    star_description = Column(String, index=True)
    highest_award = Column(String, index=True)
    years_active = Column(Integer, index=True)

    films_stars = relationship("FilmsStars", back_populates="star")


class FilmsGenres(Base):
    __tablename__ = "films_genres"

    film_id = Column(Integer, ForeignKey("films.id"), primary_key=True)
    genres_id = Column(Integer, ForeignKey("genres.id"), primary_key=True) 

    film = relationship("Film", back_populates="films_genres")
    genre = relationship("Genre", back_populates="films_genres")


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    films_genres = relationship("FilmsGenres", back_populates="genre")