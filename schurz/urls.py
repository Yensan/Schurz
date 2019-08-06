#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from utils.webcore import url, include

from apis.books.api import books

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url("/", include(hello)),
    url("/api", include(books)),

]

