from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Fase Intensiva · ATpp",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "About": "ATpp · Fase Intensiva del Consejo Técnico Escolar",
    },
)

ROOT = Path(__file__).resolve().parent
HTML_FILE = ROOT / "micrositio.html"

if not HTML_FILE.exists():
    st.error("No se encontró micrositio.html en el despliegue.")
    st.stop()

html = HTML_FILE.read_text(encoding="utf-8")
components.html(html, height=960, scrolling=True)
