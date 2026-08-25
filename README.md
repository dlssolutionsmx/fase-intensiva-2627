# ATpp · Fase Intensiva

Micrositio interactivo del Consejo Técnico Escolar, preparado para ejecutarse en Streamlit y compartirse mediante una entrada web ligera en GitHub Pages.

## Estructura

| Archivo | Función |
| --- | --- |
| `index.html` | Entrada pública ligera para Facebook y WhatsApp; contiene Open Graph, la tarjeta visual y los enlaces principales. |
| `micrositio.html` | Micrositio interactivo completo con presentación, anexos, botones y corrección del modal. |
| `app.py` | Envoltura Streamlit que carga `micrositio.html`. |
| `social-preview.png` | Imagen Open Graph de 1200×630 para las publicaciones sociales. |
| `requirements.txt` | Dependencia de Streamlit. |

## Ejecución local

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Códigos para el chatbot

Los botones de WhatsApp anteponen un código estable al mensaje para que el chatbot pueda clasificar la solicitud:

| Botón | Código | Mensaje enviado |
| --- | --- | --- |
| Descargar Presentación | `ATPP-FI-PRESENTACION` | `ATPP-FI-PRESENTACION | Quiero la presentación.` |
| Descargar Anexos | `ATPP-FI-ANEXOS` | `ATPP-FI-ANEXOS | Quiero los Anexos` |
| Descargar Presentación y Notas Metodológicas para Directivos | `ATPP-FI-DIRECTIVOS` | `ATPP-FI-DIRECTIVOS | Solicito la presentación y las notas metodológicas para directivos.` |

El chatbot debe leer el texto antes del separador `|`. Se eligió un prefijo porque es más robusto que depender de un sufijo o de la posición final del mensaje.

## Botón principal de micrositio

El botón `¿IA & Docencia? ATpp lo Reinventa!` dirige a:

`https://atpp-intensive-eydzt2zlv9eu4kzcjhpb6o.streamlit.app/`

## Publicación y enlaces

Para Streamlit Community Cloud, seleccionar este repositorio, la rama `main` y el archivo `app.py`. Para compartir en Facebook, utilizar la entrada ligera de GitHub Pages:

`https://dlssolutionsmx.github.io/fase-intensiva-2627/`

La entrada carga rápidamente, entrega los metadatos Open Graph y dirige al visitante al micrositio interactivo. La aplicación completa en Streamlit queda disponible en:

`https://faseintensiva2627.streamlit.app/`
