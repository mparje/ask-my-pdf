TASK = {
   
    'v6': (
        "Responde a la pregunta con la verdad basándote en el texto de abajo. "
        "Incluya la cita textual y un comentario de dónde encontrarla en el texto (número de página). "
        #"Después de la cita escriba una explicación paso a paso en un nuevo párrafo. "
        "Después de la cita, escriba una explicación paso a paso. "
        "Utilice viñetas. "
        #" "Después intenta reformular la pregunta original para que dé mejores resultados. " 
    ),
    'v5': (
        "Responde a la pregunta con la verdad basándote en el texto que aparece a continuación. "
        " Incluya al menos una cita textual (marcada con comillas) y un comentario sobre dónde encontrarla en el texto (es decir, nombre de la sección y número de página). "
        "Utilice elipsis en la cita para omitir partes irrelevantes de la misma. "
        "Después de la cita, escribe (en un nuevo párrafo) una explicación paso a paso para asegurarte de que la respuesta es correcta."
        " (utilice viñetas en líneas separadas)" #, ajuste el lenguaje para un lector joven). "
        "Después de la explicación comprueba si la Respuesta es coherente con el Contexto y no requiere conocimientos externos. "
        "En una nueva línea escriba 'AUTOCOMPROBACIÓN CORRECTA' si la comprobación ha sido correcta y 'AUTOCOMPROBACIÓN FALLIDA' si ha fallado. " 
    ),
    'v4': (
        "Responde con la verdad a la pregunta basándote en el texto que aparece a continuación. " 
        "Incluir cita textual y un comentario de dónde encontrarla en el texto (es decir, nombre de la sección y número de página). " 
        "Después de la cita escriba una explicación (en el nuevo párrafo) para un lector joven"
    ),
    'v3': (
        "Responda con sinceridad a la pregunta basándose en el texto siguiente. "
        "Incluye la cita textual y un comentario sobre dónde encontrarla en el texto (es decir, el nombre de la sección y el número de página)."
    ),
    'v2': (
        "Responda a la pregunta basándose en el contexto. Las respuestas deben ser elaboradas y basarse únicamente en el contexto"
    ),
    'v1': (
        "Responde a la pregunta basándote en el contexto"
    ),
}

HYDE = "Escriba una respuesta de ejemplo a la siguiente pregunta. No escriba una respuesta genérica, asuma todo lo que no se sabe."

# TODO
SUMMARY = {
	'v2':'Describa el documento del que se extrae el fragmento. Omita cualquier detalle',
	'v1':'Describe el documento del que se extrae el fragmento. No describa el fragmento, céntrese en averiguar de qué tipo de documento se trata',
}
