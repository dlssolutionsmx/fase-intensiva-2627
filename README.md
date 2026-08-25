# ATpp · Fase Intensiva

Micrositio interactivo del Consejo Técnico Escolar, preparado para ejecutarse en Streamlit y compartirse mediante una entrada social ligera en GitHub Pages.

## Estructura

| Archivo | Función |
| --- | --- |
| `index.html` | Micrositio interactivo principal con las diapositivas, anexos, botones y corrección del modal. |
| `social.html` | Entrada pública ligera para Facebook y WhatsApp; contiene Open Graph, la tarjeta visual y enlaces principales. |
| `micrositio.html` | Copia técnica del micrositio interactivo completo. |
| `app.py` | Envoltura Streamlit que carga `index.html`. |
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

`https://atpp-intensiva.streamlit.app/`

## Enlaces de publicación

La página principal, que muestra las diapositivas completas, es:

`https://dlssolutionsmx.github.io/fase-intensiva-2627/`

Para publicar en Facebook y evitar que el navegador interno falle al abrir un HTML pesado, utilizar la entrada social ligera; esta redirige automáticamente a las diapositivas completas:

`https://dlssolutionsmx.github.io/fase-intensiva-2627/social.html`

La aplicación completa en Streamlit es:

`https://atpp-intensiva.streamlit.app/`
