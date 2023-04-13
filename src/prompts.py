# INFO: some prompts are still in model.py

# TODO: Ignore OCR problems in the text below.

TASK = {
	'v6': (
			" Contesta con sinceridad a la pregunta basándote en el texto que aparece a continuación. "
			" Incluya la cita textual y un comentario sobre dónde encontrarla en el texto (número de página). "
			#Después de la cita, escriba una explicación paso a paso en un nuevo párrafo. "
			"Después de la cita, escriba una explicación paso a paso. "
			"Utilice viñetas. "
			#" "Después intenta reformular la pregunta original para que dé mejores resultados. "
		),
	'v5': (
			" Contesta con sinceridad a la pregunta basándote en el texto que aparece a continuación. "
			" Incluya al menos una cita textual (marcada con comillas) y un comentario sobre dónde encontrarla en el texto (es decir, el nombre de la sección y el número de página). "
			"Utilice elipsis en la cita para omitir partes irrelevantes de la misma. "
			"Después de la cita, escribe (en un nuevo párrafo) una explicación paso a paso para asegurarte de que la respuesta es correcta.
			" (utilice viñetas en líneas separadas)" #, ajuste el lenguaje para un lector joven). "
			"Después de la explicación comprueba si la Respuesta es coherente con el Contexto y no requiere conocimientos externos. "
			"En una nueva línea escriba 'AUTOCOMPROBACIÓN CORRECTA' si la comprobación ha sido correcta y 'AUTOCOMPROBACIÓN FALLIDA' si ha fallado. "
		),
	'v4':
		" Responde a la pregunta con la verdad basándote en el texto que aparece a continuación. " \
		"Incluya cita textual y un comentario de dónde encontrarla en el texto (es decir, nombre de la sección y número de página). " \
		"Después de la cita escriba una explicación (en el nuevo párrafo) para un lector joven",
	"v3": "Responda con sinceridad a la pregunta basándose en el texto siguiente. Incluye la cita textual y un comentario sobre dónde encontrarla en el texto (es decir, el nombre de la sección y el número de página).",
	v2': 'Responda a la pregunta basándose en el contexto. Las respuestas deben ser elaboradas y basarse únicamente en el contexto",
	v1': 'Responde a la pregunta basándote en el contexto',
	# 'v5':
		# "Generar una respuesta completa e informativa para una pregunta dada basándose únicamente en los fragmentos de documento proporcionados. " \
		# "Debes utilizar únicamente la información de los fragmentos proporcionados. Utilice un tono imparcial y periodístico. Combine los fragmentos en una respuesta coherente. " \
		# "No repita texto. Cite los fragmentos utilizando la notación [${number}]. Cite sólo los fragmentos más relevantes que respondan con precisión a la pregunta. " \
		# "Si distintos fragmentos se refieren a distintas entidades con el mismo nombre, escriba una respuesta distinta para cada entidad",
}

HYDE = "Write an example answer to the following question. Don't write generic answer, just assume everything that is not known."

# TODO
SUMMARY = {
	'v2':'Describe the document from which the fragment is extracted. Omit any details.',
	'v1':'Describe the document from which the fragment is extracted. Do not describe the fragment, focus on figuring out what kind document it is.',
}
