from PyInquirer import prompt

operations = {
    'type' : 'list',
    'name' : 'operation',
    'message' : 'Choose operation',
    'choices' : [
        {
            'name' : 'Say Hello',
            'callback' : lambda x: [print("Hello!"), prompt(operations)] # print "Hello!", and then start the prompt again
        },
        {
            'name' : 'Say World',
            'callback' : lambda x: [ print("World!") , prompt(operations)] # print "World!", and then start the prompt again
        },
        {
            'name' : 'Exit',
            'callback' : lambda x: print("Goodbye!") # print "Goodbye!", but do not start the prompt again
        }
    ]
}

a = prompt(operations)