from app import App


@App.route('/')
def index():
    return '<h1>Привет, мир!</h1>'