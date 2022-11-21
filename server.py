from bottle import route, run, static_file, template

@route('/static/tools.css')
def tools_styles():
	return static_file("tools.css", root='./static')

@route('/static/chats-sidebar.css')
def chats_sidebar_styles():
	return static_file("chats-sidebar.css", root='./static')

@route('/static/files-sidebar.css')
def files_sidebar_styles():
	return static_file("files-sidebar.css", root='./static')

@route('/static/favorites.css')
def favorites_styles():
	return static_file("favorites.css", root='./static')

@route('/static/add-favorites.css')
def add_favorites_styles():
	return static_file("add-favorites.css", root='./static')

@route('/')
def hello():
	return template('index.html')

@route('/chats-sidebar')
def chats_sidebar():
	return template('views/chats-sidebar.html')

@route('/files-sidebar')
def files_sidebar():
	return template('views/files-sidebar.html')

@route('/favorites')
def view_favorites():
	return template('views/favorites.html')

@route('/add-favorites')
def add_favorites():
	return template('views/add-favorites.html')

@route('/play-video')
def play_video():
	return template('views/video.html')

run(host='localhost', port=8080, debug=True)
