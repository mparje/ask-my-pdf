# INFORMACIÓN: algunas indicaciones todavía están en model.py

# TAREAS: Ignore los problemas de OCR en el texto a continuación.

TAREA = {
	"v6": (
			"Responda la pregunta con sinceridad basada en el texto a continuación. "
			"Incluye cita literal y un comentario donde encontrarlo en el texto (número de página)".
			#"Después de la cita, escriba una explicación paso a paso en un nuevo párrafo. "
			"Después de la cita escribe una explicación paso a paso. "
			"Usa viñetas. "
			#"Después de eso, intente reformular la pregunta original para que pueda dar mejores resultados. " 
		),
	"v5": (
			"Responda la pregunta con sinceridad basada en el texto a continuación. "
			"Incluya al menos una cita literal (marcada entre comillas) y un comentario donde encontrarla en el texto (es decir, el nombre de la sección y el número de página). "
			"Use puntos suspensivos en la cita para omitir partes irrelevantes de la cita. "
			"Después de la cita escriba (en el nuevo párrafo) una explicación paso a paso para asegurarse de que tenemos la respuesta correcta"
			"(use viñetas en líneas separadas)" #, ajuste el lenguaje para un lector joven). "
			"Después de la explicación, verifique si la respuesta es consistente con el contexto y no requiere conocimiento externo".
			"En una nueva línea, escriba 'AUTOCOMPROBACIÓN OK' si la comprobación se realizó correctamente y 'AUTOCOMPROBACIÓN FALLIDA' si falló. " 
		),
	'v4':
		"Responda la pregunta con sinceridad basada en el texto a continuación. " \
		"Incluya una cita literal y un comentario donde encontrarlo en el texto (es decir, el nombre de la sección y el número de página). " \
		"Después de la cita, escriba una explicación (en el nuevo párrafo) para un lector joven.",
	'v3': 'Responda a la pregunta con sinceridad basándose en el texto a continuación. Incluya una cita literal y un comentario donde encontrarla en el texto (es decir, el nombre de la sección y el número de página).».
	'v2': 'Responder a la pregunta basada en el contexto. Las respuestas deben ser elaboradas y basarse únicamente en el contexto.».
	'v1': 'Responder a la pregunta basada en el contexto.',
	# 'v5':
		# "Generar una respuesta completa e informativa para una pregunta dada basada únicamente en los fragmentos de documentos proporcionados. " \
		# "Solo debe usar información de los fragmentos proporcionados. Utiliza un tono imparcial y periodístico. Combina fragmentos en una respuesta coherente. " \
		# "No repetir texto. Citar fragmentos usando la notación [${number}]. Solo cite los fragmentos más relevantes que respondan a la pregunta con precisión. " \
		# "Si diferentes fragmentos se refieren a diferentes entidades con el mismo nombre, escriba una respuesta separada para cada entidad.",
}

HYDE = "Escribe una respuesta de ejemplo a la siguiente pregunta. No escribas una respuesta genérica, solo asume todo lo que no se sabe".

# TODO
RESUMEN = {
	'v2':'Describe el documento del que se extrae el fragmento. Omita cualquier detalle.».
	'v1':'Describe el documento del que se extrae el fragmento. No describa el fragmento, concéntrese en averiguar qué tipo de documento es.',
}
