# -*- coding: utf-8 -*-
from .utils import fetch_zomato, parse_zomato

NAME = "Velorex"
URL = "https://www.zomato.com/cs/brno/velorex-kr%C3%A1lovo-pole-brno-sever/denn%C3%AD-menu"
RESTAURANT_ID = "16506807"


def parse_menu():
    zomato_json = fetch_zomato(RESTAURANT_ID)
    return parse_zomato(zomato_json)

