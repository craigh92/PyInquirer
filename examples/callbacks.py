from PyInquirer import prompt

operations = [{
    'type' : 'list',
    'name' : 'operation1',
    'message' : 'Choose operation',
    'choices' : [
        {
            'name' : 'Say Hello',
            'callback' : lambda x: [print("Hello!")] 
        },
        {
            'name' : 'Say World',
            'callback' : lambda x: [print("World!")]
        }
    ]
},
{
    'type' : 'list',
    'name' : 'operation2',
    'message' : 'Choose operation',
    'choices' : [
        {
            'name' : 'Say Foo',
            'callback' : lambda x: [print("Foo!")]
        },
        {
            'name' : 'Say Bar',
            'callback' : lambda x: [print("Bar!")]
        }
    ]
}]

prompt(operations)