from bottle import route, run, static_file, template

@route('/static/chats-sidebar.css')
def chats_sidebar_styles():
	return static_file("chats-sidebar.css", root='./static')

@route('/static/files-sidebar.css')
def files_sidebar_styles():
	return static_file("files-sidebar.css", root='./static')

@route('/')
def hello():
	return template('index.html')

@route('/chats-sidebar')
def files_sidebar():
	return template('views/chats-sidebar.html')

@route('/files-sidebar')
def files_sidebar():
	return template('views/files-sidebar.html')

run(host='localhost', port=8080, debug=True)
