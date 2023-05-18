# INFO: some prompts are still in model.py

# TODO: Ignore OCR problems in the text below.

TASK = {   
    'v6': (
        "Responde a la pregunta con la verdad basándote en el texto de abajo. "
        "Incluye la cita textual y un comentario de dónde encontrarla en el texto (número de página). "
        "Después de la cita, escribe una explicación paso a paso. "
        "Utiliza viñetas."
    ),
    'v5': (
        "Resuelve el caso que se te plantea basándote en el texto que aparece a continuación. "
        "Incluye al menos una cita textual (marcada con comillas) y un comentario sobre dónde encontrarla en el texto (es decir, número de artículo y nú,ero de página). "
    ),
    'v4': (
        "A la pregunta '¿Qué dice el artículo xx?' o 'Artículo xx', o 'art xx', responde citando textualmente al artículo en cuestión, basándote en el texto de abajo. " 
        "Incluir cita textual y un comentario de dónde encontrarla en el texto (es decir, número de artículo y número de página). " 
        "Después de la cita escriba una explicación (en el nuevo párrafo) para un lector joven."
    ),
    'v3': (
        "Lee detenidamente contratos y documentos legales e informa después a sus clientes sobre los puntos clave de esos documentos. "
	"Tu respuesta debe ser clara y concisa, explicando con precisión los términos y condiciones del contrato o documento en cuestión. "
	"Tendrás que identificar cualquier aspecto que pueda suponer un riesgo para el cliente y ofrecerle recomendaciones específicas para solucionar esos problemas. "
	"Además, tendrá que asegurarse de que el lenguaje utilizado es accesible para su cliente, evitando tecnicismos innecesarios y proporcionando definiciones claras cuando sea necesario. " 
    ),
    'v2': (
        "Review the folowing text. "
	"Reviews must be honest. The review does not have to be positive. If you didn't like the book (but still finished reading it) then give it a bad rating and a generally negative review. Please be honest. This system won't work unless others can trust the honesty of our reviews."
	"Reviews must be written with correct spelling and grammar. Make sure to both use an (1) automatic spelling and grammar checking tool AND (2) repeatedly proofread your review. Automated tools are not a substitute for human proofreading."
	"Your review must be at least 300 words."
	"In your written review, you must include your rating of the book on a scale of one to five, one being the worst and five being the best."
	"You must sufficiently explain your rating. For instance, if you rated it less than five out of five stars, you would want to explain why you deducted the stars you did. If you rated it full five out of five, you will want to thoroughly explain why it deserves such an exceptionally high rating."
	"You must list the negatives about the book (e.g. what could be changed about the book to make it even better). If there was absolutely nothing that (in your opinion) that could be done better and you have no criticisms at all even slightly, then you must explain that somehow in your own words."
	"If you notice ten or more typos/errors in a review, or if it otherwise seems the book was not professionally edited, do not give it a perfect five out of five rating."
	"If you do not notice even a single typo or grammar error in the book, then you must somehow in some way in your own words explicitly mention the amazing flawless editing. It is extremely rare for a book to not have even a single typo."
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
