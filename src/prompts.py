# INFO: some prompts are still in model.py

# TODO: Ignore OCR problems in the text below.

TASK = {   
    
    'Libre': (
        "Haga lo que se le pide en relación al texto que se le proporciona."
    ),
    'Pregunta + cita': (
        "Responda a la pregunta con la verdad basándote en el texto de abajo. "
        "Incluya la cita textual y un comentario de dónde encontrarla en el texto (número de página). "
        "Después de la cita, escriba una explicación paso a paso. "
        "Utilice viñetas."
    ),
    'Preguntas': (
        "Formule preguntas que se le pueden hacer al documento; dependiendo de la extensión del documento, proponga pocas o muchas preguntas" 
    ),
    'Puntos clave': (
        "Lee detenidamente el documento de abajo y extrae los puntos clave en viñetas. " 
    ),
    'Legales': (
        "Lea detenidamente contratos y documentos legales e informa después a sus clientes sobre los puntos clave de esos documentos. "
	"Su respuesta debe ser clara y concisa, explicando con precisión los términos y condiciones del contrato o documento en cuestión. "
	"Tendrá que identificar cualquier aspecto que pueda suponer un riesgo para el cliente y ofrecerle recomendaciones específicas para solucionar esos problemas. "
	"Además, tendrá que asegurarse de que el lenguaje utilizado es accesible para su cliente, evitando tecnicismos innecesarios y proporcionando definiciones claras cuando sea necesario. " 
    ),
    'Resumen': (
        "Resuma en español el texto de abajo. "
	"Use viñetas. "
     ),
  }

HYDE = "Escriba una respuesta de ejemplo a la siguiente pregunta. No escriba una respuesta genérica, asuma todo lo que no se sabe."

SUMMARY = {
    'v2': 'Describa el documento del que se extrae el fragmento. Omita cualquier detalle.',
    'v1': 'Describe el documento del que se extrae el fragmento. No describa el fragmento, céntrese en averiguar de qué tipo de documento se trata.',
}
