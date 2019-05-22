import random
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tornado.log import enable_pretty_logging
from .conf import PORT, APP_SETTINGS, BOOKS
from .push import init_servo, push_book, push_all


class MainHandler(RequestHandler):
    def get(self):
        self.render('main.html', books=BOOKS)

    def post(self):
        book = self.get_body_argument('book')
        if book == 'all':
            push_all()
        else:
            book = random.choice(BOOKS) if book == 'random' else book
            push_book(int(book))
        self.redirect('/')


def main():
    init_servo()
    enable_pretty_logging()
    app = Application([('/', MainHandler)], **APP_SETTINGS)
    app.listen(PORT)
    IOLoop.current().start()


if __name__ == "__main__":
    main()
