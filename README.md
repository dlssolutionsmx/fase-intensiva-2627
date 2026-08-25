# ATpp · Fase Intensiva

Versión inicial del micrositio interactivo del Consejo Técnico Escolar, preparada para ejecutarse en Streamlit y publicarse también como sitio estático en GitHub Pages.

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

El chatbot debe leer el texto antes del separador `|`. Se eligió un prefijo porque es más robusto que depender de un sufijo o de la posición final del mensaje.

## Publicación

Para Streamlit Community Cloud, seleccionar este repositorio, la rama `main` y el archivo `app.py`. Para la vista previa en Facebook, habilitar GitHub Pages sobre `main` y usar la URL `https://dlssolutionsmx.github.io/fase-intensiva-2627/`; `index.html` contiene metadatos Open Graph y `social-preview.png` es la tarjeta visual pública.
