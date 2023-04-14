# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from players.models import Player 


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

# admin = Admin(app, name='PLAYERS', template_mode='bootstrap3')
# admin.add_view(ModelView(Player, db.session))

# admin.add_view(ModelView(Goalkeeper, db.session))

# Goalkeeper(Player)
# Defender(Player)
# Midfielder(Player)
# Attacking(Player)