from flask import Flask
from service.service_factory import ServiceFactory
from view.view_factory import ViewFactory


class Application(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service_factory = ServiceFactory()
        self.view_factory = ViewFactory(self.service_factory)
        self._register_endpoints()

    def _register_endpoints(self):
        views = [self.view_factory.get_total_view()]
        for view in views:
            self.add_url_rule(view.URL, view_func=view.dispatch_request)


app = Application(__name__)
app.run(port=5000)
