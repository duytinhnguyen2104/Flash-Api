from server.server import app

if __name__ == '__main__':
    app.run(host='192.168.10.114', port=9000, ssl_context="adhoc", debug=True)