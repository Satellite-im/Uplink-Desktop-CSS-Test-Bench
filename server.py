from bottle import route, run, static_file, template

@route('/test/bbb') 
def test_bbb():
	return static_file("bbb_sunflower_1080p_30fps_stereo_arcd.mp4", root='/home/fu/Documents')

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

@route('/static/modal.css')
def add_modal_styles():
	return static_file("modal.css", root='./static')

@route('/static/webrtc.js')
def webrtc_js():
	return static_file("webrtc.js", root="./static")

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

@route('/gst-sendrcv-demo')
def gst_sendrcv_demo():
	return template("views/gst-sendrcv-demo.html")

@route('/webrtc-test1')
def webrtc_test1():
	return template("views/webrtc-test1.html")

@route('/modal')
def modal():
	return template("views/modal.html")

run(host='localhost', port=8080, debug=True)
