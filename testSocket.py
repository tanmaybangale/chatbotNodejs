from socketIO_client import SocketIO, BaseNamespace
#import single_intent_parser

class Namespace(BaseNamespace):
    #obj = intentParser() 
	
    def on_connect(self):
        print('[Connected]')

    def on_reconnect(self):
        print('[Reconnected]')

    def on_disconnect(self):
        print('[Disconnected]')

    def on_userinput(self, *args):
	print (args[0])
        
        self.workOnResponse(args[0])
       
    def workOnResponse(self,inpt):
        import aiml
	import os

	kernel = aiml.Kernel()

	if os.path.isfile("bot_brain.brn"):
	    kernel.bootstrap(brainFile = "bot_brain.brn")
	else:
	    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
	    kernel.saveBrain("bot_brain.brn")
        
        userid = inpt.split('@')[1]            # splitting the input for socketid
        inptmsg = inpt.split('@')[0]
  	
        #rep = obj.fetch_intent()
        if rep == '':

            rep = kernel.respond(inptmsg)    #giving aiml brain to get response
	    if rep =='':
                rep = 'I did not get you ?'   
        
             
        self.emit('response_generated',"Bot :" + rep +"@" + userid  ) # sending response with socketid	    

 			         

socketIO = SocketIO('localhost', 3000, Namespace)
socketIO.wait()



