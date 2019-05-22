from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tornado.log import enable_pretty_logging
from .conf import PORT, APP_SETTINGS
from .motors import move, init_servo


class MainHandler(RequestHandler):
    def get(self):
        self.render('main.html')

    def post(self):
        move(self.get_body_argument('action'))
        self.redirect('/')


def main():
    init_servo()
    enable_pretty_logging()
    app = Application([('/', MainHandler)], **APP_SETTINGS)
    app.listen(PORT)
    IOLoop.current().start()


if __name__ == "__main__":
    main()
