# Rewrite OurMiddleware from lecture to act like werkzeug middlewares

    from:
    app.wsgi_app = OurMiddleware(app.wsgi_app)
    to:
    app = OurMiddleware(app)


# Create Pets Hotel db through migrations, one revision for each table
