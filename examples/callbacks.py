from PyInquirer import prompt

operations = {
    'type' : 'list',
    'name' : 'operation',
    'message' : 'Choose operation',
    'choices' : [
        {
            'name' : 'Say Hello',
            'callback' : lambda : [print("Hello!"), prompt(operations)] # print "Hello!", and then start the prompt again
        },
        {
            'name' : 'Say World',
            'callback' : lambda : [ print("World!") , prompt(operations)] # print "World!", and then start the prompt again
        },
        {
            'name' : 'Exit',
            'callback' : lambda : print("Goodbye!") # print "Goodbye!", but do not start the prompt again
        }
    ]
}

a = prompt(operations)