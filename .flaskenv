FLASK_ENV=development
FLASK_APP=hun_tool.app:create_app
SECRET_KEY=changeme
DATABASE_URI=sqlite:////tmp/hun_tool.db
CELERY_BROKER_URL=amqp://guest:guest@localhost/
CELERY_RESULT_BACKEND_URL=amqp://guest:guest@localhost/
