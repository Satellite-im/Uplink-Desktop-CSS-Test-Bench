from bottle import route, run, static_file, template

@route('/static/styles.css')
def styles():
	return static_file("styles.css", root='./static')

@route('/')
def hello():
	return template('index.html')

run(host='localhost', port=8080, debug=True)
