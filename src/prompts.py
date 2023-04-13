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
		"Answer the question truthfully based on the text below. " \
		"Include verbatim quote and a comment where to find it in the text (ie name of the section and page number). " \
		"After the quote write an explanation (in the new paragraph) for a young reader.",
	'v3': 'Answer the question truthfully based on the text below. Include verbatim quote and a comment where to find it in the text (ie name of the section and page number).',
	'v2': 'Answer question based on context. The answers sould be elaborate and based only on the context.',
	'v1': 'Answer question based on context.',
	# 'v5':
		# "Generate a comprehensive and informative answer for a given question solely based on the provided document fragments. " \
		# "You must only use information from the provided fragments. Use an unbiased and journalistic tone. Combine fragments together into coherent answer. " \
		# "Do not repeat text. Cite fragments using [${number}] notation. Only cite the most relevant fragments that answer the question accurately. " \
		# "If different fragments refer to different entities with the same name, write separate answer for each entity.",
}

HYDE = "Write an example answer to the following question. Don't write generic answer, just assume everything that is not known."

# TODO
SUMMARY = {
	'v2':'Describe the document from which the fragment is extracted. Omit any details.',
	'v1':'Describe the document from which the fragment is extracted. Do not describe the fragment, focus on figuring out what kind document it is.',
}
