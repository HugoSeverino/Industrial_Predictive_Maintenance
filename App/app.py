from App import create_app

server = create_app()

if __name__ == '__main__':
    server(debug=True)
