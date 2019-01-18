from nameko.rpc import rpc

class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)

"""
$ nameko run hello
$ nameko shell

>>> n.rpc.greeting_service.hello(name='world')
'Hello, world!'
"""        