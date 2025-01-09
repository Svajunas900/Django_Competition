from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')
app.conf.result_backend = 'db+sqlite:///results.sqlite'


@app.task(task_ignore_result=False, track_started=True)
def add(x, y):
    return x + y
