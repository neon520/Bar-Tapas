# Bar&Tapas
Django Webpage about Bars and Tapas, based on next tutorial:
[TangoWithDjango](http://www.tangowithdjango.com/book17/)

To not use static content by myself when deploying, I did the following tutorial: [Django-assets](https://devcenter.heroku.com/articles/django-assets)

You can see the final result here in [Heroku](http://baresytapas.herokuapp.com/)

##Tutorial
First of all, I have put, from settings.py,

    DEBUG=False
    ALLOWED_HOSTS=["*"]

After this, I continue doing the previous mentioned [tutorial](https://devcenter.heroku.com/articles/django-assets).

You have to do it until the _Collectstatic during builds_ part.

After that you only need to conect your Repository to Heroku and _Enable Automatic Deploy_.

##Problems
I don't know why but highcharts node doesn't load if I use https conection. Fixing it in next version.
