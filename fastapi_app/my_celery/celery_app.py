from tasks import add
from celery.result import AsyncResult

a = add.delay(2, 2)
print(a.backend.url)
print(a.status)
print(a.ready())
print(AsyncResult(a))
print(a.worker)
print(a)
result = add.apply_async(args=[1, 2], wait=True)
print(result.get())