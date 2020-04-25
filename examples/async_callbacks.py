#WIP

from PyInquirer import prompt
import asyncio 

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
futures = []

# An example demonstrating choices becoming disabled as a result of something happening in the background.
# While the background task is executing, the prompt can be continued to be used
# When the background task finishes (i.e, makes an option available / disabled), the prompt will refresh

def barCallback(): print("You picked Bar!")
bar = {
    'name' : 'Bar',
    'disabled' : False,
    'callback' : barCallback
}

def fooCallback(): print("You picked Foo!")
foo = {
    'name' : 'Foo',
    'disabled' : False,
    'callback' : fooCallback
}

def disableFooCallback():
    disableFoo['disabled'] = "Not Available"
    
    # Schdule a job to make the option foo disabled in 2 secconds
    async def job():
        await asyncio.sleep(2)
        foo['disabled'] = "Disabled"
        enableFoo['disabled'] = False
        
    print("Schedulng task!")
    loop.create_task(job())
    
disableFoo = {
    'name' : 'Disable Foo',
    'disabled' : False,
    'callback' : disableFooCallback
}

def enableFooCallback():
    enableFoo['disabled'] = "Not Available"
    
    # Schdule a job to make the option foo available in 2 secconds
    async def job():
        await asyncio.sleep(2)
        foo['disabled'] = False
        disableFoo['disabled'] = False

    print("Schedulng task!")
    loop.create_task(job())
        
enableFoo = {
    'name' : 'Enable Foo',
    'disabled' : "Not Available",
    'callback' : enableFooCallback
}



def exitCb(): loop.stop()
exit = {
    'name' : 'Exit',
    'disabled' : False,
    'callback' : exitCb
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
    
    future_answers_generator = prompt(options, patch_stdout = True, return_asyncio_coroutine = True, eventloop = loop, refresh_interval = 1)['choice']    
    future = asyncio.ensure_future(future_answers_generator)
    
    if len(futures) == 0:
        futures.append(future)
    else:
        futures.pop()
        futures.append(future)

# === Start Program ===

loop.create_task(myprompt())
loop.run_forever()


