with app.app_context():
    from .home import home
    app.register_blueprint(home.home_blueprint)
