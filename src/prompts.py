# INFO: some prompts are still in model.py

# TODO: Ignore OCR problems in the text below.

TASK = {   
    'v6': (
        "Responde a la pregunta con la verdad basándote en el texto de abajo. "
        "Incluya la cita textual y un comentario de dónde encontrarla en el texto (número de página). "
        "Después de la cita, escriba una explicación paso a paso. "
        "Utilice viñetas."
    ),
    'v5': (
        "Responde a la pregunta con la verdad basándote en el texto que aparece a continuación. "
        "Incluya al menos una cita textual (marcada con comillas) y un comentario sobre dónde encontrarla en el texto (es decir, nombre de la sección y número de página). "
        "Utilice elipsis en la cita para omitir partes irrelevantes de la misma. "
        "Después de la cita, escribe (en un nuevo párrafo) una explicación paso a paso para asegurarte de que la respuesta es correcta."
        "Utilice viñetas en líneas separadas."
        "Después de la explicación comprueba si la respuesta es coherente con el contexto y no requiere conocimientos externos. "
        "En una nueva línea escriba 'AUTOCOMPROBACIÓN CORRECTA' si la comprobación ha sido correcta y 'AUTOCOMPROBACIÓN FALLIDA' si ha fallado. "
    ),
    'v4': (
        "Responde con la verdad a la pregunta basándote en el texto que aparece a continuación. " 
        "Incluir cita textual y un comentario de dónde encontrarla en el texto (es decir, nombre de la sección y número de página). " 
        "Después de la cita escriba una explicación (en el nuevo párrafo) para un lector joven."
    ),
    'v3': (
        "Responda con sinceridad a la pregunta basándose en el texto siguiente. "
        "Incluye la cita textual y un comentario sobre dónde encontrarla en el texto (es decir, el nombre de la sección y el número de página)."
    ),
    'v2': (
        "Review the folowing text. "
	"Reviews must be honest. The review does not have to be positive. If you didn't like the book (but still finished reading it) then give it a bad rating and a generally negative review. Please be honest. This system won't work unless others can trust the honesty of our reviews."
	"Reviews must be written with correct spelling and grammar. Make sure to both use an (1) automatic spelling and grammar checking tool AND (2) repeatedly proofread your review. Automated tools are not a substitute for human proofreading."
	"Your review must be at least 300 words."
	"In your written review, you must include your rating of the book on a scale of one to five, one being the worst and five being the best."
     ),
    'v1': (
        "Haga lo que se le pide con relación al texto."
    ),
}

HYDE = "Escriba una respuesta de ejemplo a la siguiente pregunta. No escriba una respuesta genérica, asuma todo lo que no se sabe."

SUMMARY = {
    'v2': 'Describa el documento del que se extrae el fragmento. Omita cualquier detalle.',
    'v1': 'Describe el documento del que se extrae el fragmento. No describa el fragmento, céntrese en averiguar de qué tipo de documento se trata.',
}
