#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  gestion.py
#
#  Copyright 2014 Felipe Hommen <felibank@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


import os
import configparser
import datetime
import uuid

base_dir = os.path.expanduser('~/.moneydero')
try:
    os.mkdir(base_dir)
except:
    pass

cuentas = configparser.ConfigParser()
cuentas.read(os.path.join(base_dir, 'cuentas.mnd'))

categorias = configparser.ConfigParser()
categorias.read(os.path.join(base_dir, 'categorias.mnd'))

apuntes = configparser.ConfigParser()
apuntes.read(os.path.join(base_dir,  'apuntes.mnd'))
        

def apunta(apunte):
    apuntes[uuid.uuid1()] = apunte
    with open(os.path.join(base_dir, 'apuntes.mnd'), 'w') as f:
        apuntes.write(f)
    
def lista_apuntes(filtro):
    respuesta = set()
    from_date = filtro['fecha_desde'] - datetime.timedelta(days=1)
    to_date = filtro['fecha_hasta'] + datetime.timedelta(days=1)
    for apunte in apuntes:
        if apunte == 'DEFAULT':
            continue
        fecha = datetime.datetime.strptime(apuntes[apunte]['fecha'], '%Y-%m-%d').date()
        if from_date < fecha and fecha < to_date:
            respuesta.update({apunte})
    return respuesta


def main():
    pass

if __name__ == "__main__":
    main()
 
