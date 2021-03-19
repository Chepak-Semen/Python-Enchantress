from flask import Flask, request

from werkzeug.wrappers import Request, Response


class OurMiddleware():
    def __init__(self, app):
        self.app = app
        self.API_token = 'mytoken'

    def __call__(self, environ, start_response):
        request = Request(environ)
        token = request.headers.get('api_token')

        if token == self.API_token:
            environ['user'] = 'Some token user'
            return self.app(environ, start_response)

        res = Response('Wrong api_token', mimetype= 'text/plain', status=401)
        return res(environ, start_response)


app = Flask(__name__)
app.wsgi_app = OurMiddleware(app.wsgi_app)


@app.route('/')
def hello():
    user = request.environ['user']
    return f'Hi {user} authed from middleware'


if __name__ == '__main__':
    app.run(debug=True)
