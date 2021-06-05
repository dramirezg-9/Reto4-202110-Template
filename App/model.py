"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import graph as gp
from DISClib.DataStructures import mapentry as me
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# Clasificación de datos

def connection_line_processing(line:str):
        l1 = line.split(',"')
        p0 = l1[0]
        l2 = l1[1].split('",')
        p1 = l2[0].replace(",","").replace(" km","")
        p2 = l2[1]
        l3 = l1[2].split('",')
        p3 = l3[0].replace(",  ", "|")
        p4 = l3[1]
        new_line = ",".join([p0,p1,p2,p3,p4])
        return new_line

def data_type(text:str):
    if text.isnumeric():
        return 'i'
    elif text.replace(".","").isnumeric():
        return 'f'
    else:
        return 's'

def correct_type(text:str, t: str):
    if t == 'i':
        return int(text)
    elif t == 'f':
        return float(text)
    else:
        return text

def line_types(line: str):
    params = line.replace("\n","").split(",")
    types = lt.newList(datastructure='ARRAY_LIST')
    for param in params:
        t = data_type(param)
        lt.addLast(types, t)
    return types


class landing_points:

    def add_point(self, line:str, types: list):
        params = line.replace("\n","").split(",")
        characteristics = lt.newList(datastructure='ARRAY_LIST')
        for param, t in zip(params, types):
            char = correct_type(param, t)
            lt.addLast(characteristics, char)
        id = lt.getElement(characteristics, 1)
        name = lt.getElement(characteristics, 3)
        mp.put(self.points_by_id, id, characteristics)
        mp.put(self.points_by_name, name, characteristics)
    
    def add_country(self, line: str, types: list):
        params = line.replace("\n","").split(",")
        name = params[0]
        characteristics = lt.newList(datastructure='ARRAY_LIST')
        for param, t in zip(params[1:], types[1:]):
            char = correct_type(param, t)
            lt.addLast(characteristics, char)
        mp.put(self.countries, name, characteristics)

    def add_connection(self, line:str, types: list):
        params = line.replace("\n","").split(",")
        characteristics = lt.newList(datastructure='ARRAY_LIST')
        for param, t in zip(params, types):
            char = correct_type(param, t)
            lt.addLast(characteristics, char)
        lt.addLast(self.connections_list, characteristics)

    # Funciones para creacion de datos
    
    def open_points(self, filepath: str):
        self.points_by_id = mp.newMap(numelements=1279)
        self.points_by_name = mp.newMap(numelements=1279)
        file = open(filepath, 'r')
        file.readline()
        line = file.readline()
        types = line_types(line)
        while line:
            self.add_point(line, types)
            line = file.readline()
        file.close()

    def open_connections(self, filepath: str):
        self.connections_list = lt.newList(datastructure='ARRAY_LIST')
        file = open(filepath, 'r')
        file.readline()
        line = file.readline()
        temp = connection_line_processing(line)
        types = line_types(temp)
        while line:
            line = connection_line_processing(line)
            self.add_connection(line, types)
            line = file.readline()
        file.close()

    def open_countries(self, filepath:str):
        self.countries = mp.newMap(numelements=236)
        file = open(filepath, 'r')
        file.readline()
        line = file.readline()
        types = line_types(line)
        while line:
            self.add_country(line, types)
            line = file.readline()
        file.close()

    
    # Optimizaciones de requerimientos
    def req_1_optimization(self):
        pass
    
    # Construccion de modelos
    def draw_connections(self):
        pass

    def __init__(self, filepath_points: str, filepath_connections: str, filepath_countries: str):
        self.points_by_id, self.points_by_name, self.connections_list, self.countries = None, None, None, None
        self.open_points()
        self.open_connections()
        self.open_countries()
        #self.draw_connections()
        #self.req_1_optimization()
    
    # Requerimientos
    def req_1(self, lp1, lp2):
        pass

    def req_2(self):
        pass

    def req_3(self, countryA, countryB):
        pass

    def req_4(self):
        pass

    def req_5(self, lp):
        pass

    def req_6(self, country, cable):
        pass

    def req_7(self, IP1, IP2):
        pass

# Funciones para agregar informacion al catalogo



# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
