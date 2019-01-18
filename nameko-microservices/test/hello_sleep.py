from time import sleep

from nameko.rpc import rpc


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        sleep(5)
        return "Hello, {}!".format(name)
"""
nameko run hello_sleep
☁  ~  nameko shell
In [3]: n.rpc.greeting_service.hello(name="mtianyan")
Out[3]: 'Hello, mtianyan!'

res = []
for i in range(5):
    hello_res = n.rpc.greeting_service.hello.call_async(name=str(i))
    res.append(hello_res)

for hello_res in res:
    print(hello_res.result())
"""