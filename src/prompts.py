# INFO: some prompts are still in model.py

# TODO: Ignore OCR problems in the text below.

TASK = {   
    'v6': (
        "Responda a la pregunta con la verdad basándote en el texto de abajo. "
        "Incluya la cita textual y un comentario de dónde encontrarla en el texto (número de página). "
        "Después de la cita, escriba una explicación paso a paso. "
        "Utilice viñetas."
    ),
    'v5': (
        "Resuelva el caso que se te plantea basándose en el texto que aparece a continuación. "
        "Incluya al menos una cita textual (marcada con comillas) y un comentario sobre dónde encontrarla en el texto (es decir, número de artículo y número de página). "
    ),
    'v4': (
        "A la pregunta '¿Qué dice el artículo xx?' o 'Artículo xx', o 'art xx', responda citando textualmente al artículo en cuestión, basándose en el texto de abajo. " 
        "Incluir cita textual y un comentario de dónde encontrarla en el texto (es decir, número de artículo y número de página). " 
        "Después de la cita escriba una explicación (en el nuevo párrafo) para un lector joven."
    ),
    'v3': (
        "Leadetenidamente contratos y documentos legales e informa después a sus clientes sobre los puntos clave de esos documentos. "
	"Su respuesta debe ser clara y concisa, explicando con precisión los términos y condiciones del contrato o documento en cuestión. "
	"Tendrá que identificar cualquier aspecto que pueda suponer un riesgo para el cliente y ofrecerle recomendaciones específicas para solucionar esos problemas. "
	"Además, tendrá que asegurarse de que el lenguaje utilizado es accesible para su cliente, evitando tecnicismos innecesarios y proporcionando definiciones claras cuando sea necesario. " 
    ),
    'v2': (
        "Resuma el texto de abajo."
	"Use viñetas. "
     ),
    'v1': (
        "Haga lo que se le pide en relación al texto."
    ),
}

HYDE = "Escriba una respuesta de ejemplo a la siguiente pregunta. No escriba una respuesta genérica, asuma todo lo que no se sabe."

SUMMARY = {
    'v2': 'Describa el documento del que se extrae el fragmento. Omita cualquier detalle.',
    'v1': 'Describe el documento del que se extrae el fragmento. No describa el fragmento, céntrese en averiguar de qué tipo de documento se trata.',
}
