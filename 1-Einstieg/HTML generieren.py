import html
# Zusammenarbeit mit folgenden Teilnehmern:
def createHtmlElement(type, classname=None, id=None, style=None, content=None, text=None):
	string = "<" + type

	if classname is not None:
		string += " class=" + "\"" + classname + "\""
	if id is not None:
		string += " id=" + "\"" + id + "\""
	if style is not None:
		string += " style=" + "\"" + style + "\""
	string += ">"
	if content is not None:
		string += content
	if text is not None:
		string += html.escape(text)
	string += "</" + type + ">"
	return string