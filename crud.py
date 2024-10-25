from sqlalchemy.orm import Session
import models
from datetime import date,time

#DODAVANJE CLANOVA FILMOVA, SCENARISTA I FILMSKIH ZVIJEZDA

def ADD_FILM(db: Session,
               film_name: str,
               year_produced: str, 
               image_url: str,
               run_time: time,
               imdb_rating: float,
               description:str,
                meta_score:float,
                gross:float,
                votes:int
             ):
    
    # Kreira instancu novog filma
    db_Film = models.Film(film_name=film_name,
                        year_produced=year_produced,
                        image_url=image_url,
                        run_time=run_time,
                        imdb_rating=imdb_rating,
                        description=description,
                        meta_score=meta_score,
                        gross=gross,
                        votes=votes )

    
    # Dodaje novog filma u sesiju baze podataka
    db.add(db_Film)
    db.commit()     # Sačuva promene u bazi podataka, tako da novi film postane trajni unos
    db.refresh(db_Film) # Ažurira objekat film s informacijama iz baze, npr. ID koji generiše baza

    return db_Film


def ADD_STAR(db: Session,
               name: str,
               star_description: str, 
               highest_award: str,
                years_active: int,
             ):
    DB_Star=models.Star(name=name,
                        star_description=star_description,
                        highest_award=highest_award,
                        years_active=years_active)
    db.add(DB_Star)
    db.commit()     # Sačuva promene u bazi podataka, tako da novi film postane trajni unos
    db.refresh(DB_Star) # Ažurira objekat film s informacijama iz baze, npr. ID koji generiše baza

    return DB_Star

def ADD_director(db: Session,
               name: str,
               direct_desc: str, 
               direct_award:str,
               ):
    DB_Director=models.Director(name=name,
                        direct_desc=direct_desc,
                        direct_award=direct_award)
    db.add(DB_Director)
    db.commit()     # Sačuva promene u bazi podataka, tako da novi film postane trajni unos
    db.refresh(DB_Director) # Ažurira objekat film s informacijama iz baze, npr. ID koji generiše baza

    return DB_Director

#QUERY ZA SVE FILMOVE SCENARISTE I ZVIJEZDE

def get_Films(db: Session):
    # Vraća sve Filmove
    return db.query(models.Film).all()


def get_Stars(db: Session):
    # Vraća sve Glumce
    return db.query(models.Star).all()

def get_Directors(db: Session):
    # Vraća sve Rezisere
    return db.query(models.Director).all()


# quweri za posebne glumce,directore i filmove.
def get_Film(db:Session,name:str):
     QUERY=db.query(models.Film).filter(Film.film_name==name).first()
     return QUERY

def get_Star(db:Session,name:str):
     QUERY=db.query(models.Star).filter(Star.name==name).first()
     return QUERY

def get_Director(db:Session,name:str):
     QUERY=db.query(models.Director).filter(Director.name==name).first()
     return QUERY