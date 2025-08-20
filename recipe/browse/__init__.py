with app.app_context():
    from .browse import browse
    app.register_blueprint(browse.browse_blueprint)
