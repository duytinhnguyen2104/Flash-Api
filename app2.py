from server.server import app
app.static_folder = 'static'
if __name__ == '__main__':
    app.run(host='localhost', port=9000, ssl_context="adhoc", debug=True)