#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def url(url, fun, name=None, **kwargs):
    return dict(rule=url, endpoint=name, view_func=fun, **kwargs)


def include(blueprint, **options):
    return (blueprint, options)


def register_url(app_blue, urlpatterns):
    """
    :param app_blue: Flask app OR Blueprint object
    :param urlpattern: dict made by url()
    :return:
    """
    for i in urlpatterns:
        target = i.pop('view_func')
        url = i.pop('rule')
        if isinstance(target, (tuple, list)):  # this is a tuple made by include()
            i.update(target[1])
            target = target[0]
            # Flask: app.register_blueprint(self, blueprint, url_prefix=None, subdomain=None)
            app_blue.register_blueprint(blueprint=target, url_prefix=url, **i)
        else:
            # Flask: app.add_url_rule(self, rule, endpoint=None, view_func=None, **options):
            app_blue.add_url_rule(rule=url, view_func=target, **i)
            # Flask's URL Rule: a resource have only one URL.
            # /test/ ->  /test/ can request directly.
            #            /test  308 PERMANENT REDIRECT to /test/
            # /test  ->  /test/ 404
            #            /test  can request directly.
            # This rule fits Representational State Transfer, widely used by Apache and other http server.
            # But, if you still want to break its rule, just use substitute in below:
            """
            if url[-1] == '/':
                app_blue.add_url_rule(rule=url, view_func=target, **i)
                app_blue.add_url_rule(rule=url[:-1], view_func=target, **i)
            else:
                app_blue.add_url_rule(rule=url, view_func=target, **i)
                app_blue.add_url_rule(rule=url+'/', view_func=target, **i)
            """
