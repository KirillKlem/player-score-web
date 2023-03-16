from main_code import db, create_app

with create_app().app_context():
    db.create_all()
