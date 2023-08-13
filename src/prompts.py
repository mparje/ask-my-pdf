# INFO: some prompts are still in model.py

# TODO: Ignore OCR problems in the text below.

TASK = {   
    'Pregunta + cita': (
        "Responda a la pregunta con la verdad basándote en el texto de abajo. "
        "Incluya la cita textual y un comentario de dónde encontrarla en el texto (número de página). "
        "Después de la cita, escriba una explicación paso a paso. "
        "Utilice viñetas."
    ),
    'Análisis del subjuntivo': (
        "Tu tarea es identificar las oraciones en las que se utiliza el modo subjuntivo, así como las oraciones en las que se utiliza el indicativo cuando lo normal sería utilizar el subjuntivo." 
	"Debes señalar el verbo en subjuntivo en cada caso y especificar en qué tiempo se encuentra. Asegúrate de leer detenidamente los textos proporcionados y no cambiar ningún verbo."
	"También debes tener cuidado de no equivocarte al identificar un verbo en modo subjuntivo cuando en realidad está en modo indicativo. No incluyas en tu lista las oraciones que no contengan verbos en subjuntivo." 
	"Al final, indica cuántas oraciones se encuentran en modo subjuntivo y cuántas debieron haber utilizado el subjuntivo. Por favor, proporciona una respuesta clara y concisa, indicando cada oración en la que se utilice el subjuntivo y especificando el tiempo verbal."
        "Asimismo, identifica las oraciones donde se haya utilizado el indicativo en lugar del subjuntivo, señalando qué verbo debió haberse conjugado en subjuntivo."
        "Por favor, ten en cuenta que debes ser preciso y cuidadoso en tu respuesta, y asegúrate de comprender correctamente los textos proporcionados antes de identificar los verbos conjugados en modo subjuntivo."
    ),
    'Puntos clave': (
        "Lee detenidamente el documento de abajo y extrae los puntos clave en en viñetas. " 
        
    ),
    'Legales': (
        "Lea detenidamente contratos y documentos legales e informa después a sus clientes sobre los puntos clave de esos documentos. "
	"Su respuesta debe ser clara y concisa, explicando con precisión los términos y condiciones del contrato o documento en cuestión. "
	"Tendrá que identificar cualquier aspecto que pueda suponer un riesgo para el cliente y ofrecerle recomendaciones específicas para solucionar esos problemas. "
	"Además, tendrá que asegurarse de que el lenguaje utilizado es accesible para su cliente, evitando tecnicismos innecesarios y proporcionando definiciones claras cuando sea necesario. " 
    ),
    'Resumen': (
        "Resuma el texto de abajo."
	"Use viñetas. "
     ),
    'Libre': (
        "Haga lo que se le pide en relación al texto que se le proporciona."
    ),
}

HYDE = "Escriba una respuesta de ejemplo a la siguiente pregunta. No escriba una respuesta genérica, asuma todo lo que no se sabe."

SUMMARY = {
    'v2': 'Describa el documento del que se extrae el fragmento. Omita cualquier detalle.',
    'v1': 'Describe el documento del que se extrae el fragmento. No describa el fragmento, céntrese en averiguar de qué tipo de documento se trata.',
}
