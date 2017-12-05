import execnet
import subprocess
#import gmail

def modernize(Module, Function, ArgumentList):
    Version = 2.7
    gw = execnet.makegateway("popen//python=python%s" % Version)
    channel = gw.remote_exec("""
        from %s import %s as the_function
        channel.send(the_function(*channel.receive()))
    """ % (Module, Function))
    channel.send(ArgumentList)
    return channel.receive()

# def modernize(Module, Function

def sendEmail(message,to):
	return modernize('gmail', 'sendEmail', [message,to])

def sendFile(message,to,file):
	return modernize('gmail', 'sendFile', [message,to,file])
