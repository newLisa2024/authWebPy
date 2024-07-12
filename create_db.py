from app import app, db
from app.models import User

# Создание всех таблиц внутри контекста приложения
with app.app_context():
    db.create_all()

print("Database initialized!")





