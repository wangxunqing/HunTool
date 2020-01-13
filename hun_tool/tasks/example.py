from hun_tool.extensions import celery


@celery.task
def dummy_task():
    return "OK"
