from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import *

import json

# obtener informacion del archivo 
from configuracion import cadena_base_datos

#conectar a la base de datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()
# leer archivo con clubs
clubs = open("data/datos_clubs.txt", "r", encoding="utf-8")
clubs = clubs.readlines()

# leer archivo con jugadores
jugadores = open("data/datos_jugadores.txt", "r", encoding="utf-8")
jugadores = jugadores.readlines()

#Tratar datos de clubs y registrarlos
for club in clubs:
    club_array = club.split('\n');
    club_array = club_array[0].split(';');
    c = Club(nombre=club_array[0], deporte=club_array[1], fundacion=club_array[2])
    session.add(c)

# obtener clubes
consulta_clubs = session.query(Club).all()

#Tratar datos de jugadores y registrarlos
for jugador in jugadores:
    jugador_array = jugador.split('\n');
    jugador_array = jugador_array[0].split(';');

    # asignar id
    for club in consulta_clubs:
        if(jugador_array[0] == club.nombre):
            id_club = club.id

    j = Jugador(nombre=jugador_array[3], dorsal=jugador_array[2], posicion=jugador_array[1], club_id=id_club)
    session.add(j)

# confirmar cambios

session.commit()
