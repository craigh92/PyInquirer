#WIP

from PyInquirer import prompt
import asyncio 

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
futures = []

# An example demonstrating choices becoming disabled as a result of something happening in the background.
# While the background task is executing, the prompt can be continued to be used
# When the background task finishes (i.e, makes an option available / disabled), the prompt will refresh

# Choices:

bar = {
    'name' : 'Bar',
    'disabled' : False,
    'callback' : lambda x : print("You picked Bar!")
}

foo = {
    'name' : 'Foo',
    'disabled' : False,
    'callback' : lambda x : print("you picked Foo!")
}

exit = {
    'name' : 'Exit',
    'disabled' : False,
    'callback' : lambda x : loop.stop()
}

def disableFooCallback(x):
    disableFoo['disabled'] = "Not Available"
    
    # Schdule a job to make the option foo disabled in 2 secconds
    async def job():
        await asyncio.sleep(2)
        foo['disabled'] = "Disabled"
        enableFoo['disabled'] = False
        
    print("Schedulng task!")
    loop.create_task(job())

def enableFooCallback(x):
    enableFoo['disabled'] = "Not Available"
    
    # Schdule a job to make the option foo available in 2 secconds
    async def job():
        await asyncio.sleep(2)
        foo['disabled'] = False
        disableFoo['disabled'] = False

    print("Schedulng task!")
    loop.create_task(job())
 
disableFoo = {
    'name' : 'Disable Foo',
    'disabled' : False,
    'callback' : disableFooCallback
}

enableFoo = {
    'name' : 'Enable Foo',
    'disabled' : "Not Available",
    'callback' : enableFooCallback
}
        
options = {
    'type': 'list',
    'name': 'choice',
    'message': 'Choose Command',
    'choices': [
        bar,
        foo,
        disableFoo,
        enableFoo,
        exit
    ]
}

async def myprompt():
    prompt(options, patch_stdout = True, return_asyncio_coroutine = True, eventloop = loop, refresh_interval = 1)['choice']    

# === Start Program ===

loop.create_task(myprompt())
loop.run_forever()

