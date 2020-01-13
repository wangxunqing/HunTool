from hun_tool.app import init_celery

app = init_celery()
app.conf.imports = app.conf.imports + ('hun_tool.tasks',)
