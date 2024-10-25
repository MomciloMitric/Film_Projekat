
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date,time
import crud, models
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/Films/")
def create_film(
                        film_name: str,
                        year_produced: str, 
                        image_url: str,
                        run_time: str,
                        imdb_rating: float,
                        description:str,
                        meta_score:float,
                        gross:float,
                        votes:int,
                        db:Session=Depends(get_db)):
    return crud.ADD_FILM (db=db,
                        film_name=film_name,
                        year_produced=year_produced,
                        image_url=image_url,
                        run_time=run_time,
                        imdb_rating=imdb_rating,
                        description=description,
                        meta_score=meta_score,
                        gross=gross,
                        votes=votes )

@app.post("/Directors/")
def create_Director(    name: str,
                        direct_desc: str, 
                        direct_award: str,
                        db:Session=Depends(get_db)):
    return crud.ADD_director(db=db,
                        name=name,
                        direct_desc=direct_desc,
                        direct_award=direct_award,)


@app.post("/Stars/")
def create_Star(
                        name: str,
                        star_description: str, 
                        highest_award: str,
                        years_active: int,
                        db:Session=Depends(get_db)):
    return crud.ADD_STAR(db=db,
                        name=name,
                        star_description=star_description,
                        highest_award=highest_award,
                        years_active=years_active,)


@app.get("/Films/")
def read_Films(db: Session = Depends(get_db)):
    FILM = crud.get_Films(db)
    print(FILM)
    return FILM


@app.get("/Stars/")
def read_Stars(db: Session = Depends(get_db)):
    Stars= crud.get_Stars(db)
    print(Stars)
    return Stars

@app.get("/Directors/")
def read_Directors(db: Session = Depends(get_db)):
    Directors= crud.get_Directors(db)
    print(Directors)
    return Directors