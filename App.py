import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg
import tensorflow as tf

st.set_page_config(page_title="MineralScope: AI Geologist", page_icon="💎", initial_sidebar_state="collapsed")

pages = ["Home", "Analyze", "MAP", "About"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "resources", "gambar" ,"logo.svg")
urls = {}

styles = {
    "nav": {
        "display": "flex",
        "background-color": "#fbccd4", #fbccd4 #c8486f
        "justify-content": "center",
        "align-items": "center",  # Tambahkan agar elemen lebih rata vertikal
        "height": "50px",  # Kurangi tinggi navbar",
    },
    "img": {
        "height": "150px",
        "margin-left": "10px",
    },
    "span": {
        "color": "#0a0507",
        "padding": "5px",
        "cursor": "pointer",
        "text-align": "center",
        "font-size": "16px",
    },
    "active": {
        # "background-color": "#c8486f",
        "color": "#ffffff",
        "font-weight": "bold",
        #"padding": "14px",
        "padding": "8px",
        "border-bottom": "2px solid #ffffff",
    },
}

options = {
    "show_menu": True,
    "show_sidebar": False,
}

page= st_navbar (
    pages,
    logo_path=logo_path,
    urls=urls,
    styles=styles,
    options=options,
)

if not page:
    page = "Home"  # Default page

functions = {
    "Home": pg.show_home,
    "Analyze": pg.show_analyze,
    "MAP": pg.show_map,
    "About":pg.show_about,
}

go_to = functions.get(page)

if go_to:
    go_to()