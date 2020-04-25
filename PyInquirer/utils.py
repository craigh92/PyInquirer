# -*- coding: utf-8 -*-
from __future__ import print_function
import json
import sys
from pprint import pprint
import asyncio
from pygments import highlight, lexers, formatters

__version__ = '0.1.2'

PY3 = sys.version_info[0] >= 3


def format_json(data):
    return json.dumps(data, sort_keys=True, indent=4)


def colorize_json(data):
    if PY3:
        if isinstance(data, bytes):
            data = data.decode('UTF-8')
    else:
        if not isinstance(data, unicode):
            data = unicode(data, 'UTF-8')
    colorful_json = highlight(data,
                              lexers.JsonLexer(),
                              formatters.TerminalFormatter())
    return colorful_json


def print_json(data):
    #colorful_json = highlight(unicode(format_json(data), 'UTF-8'),
    #                          lexers.JsonLexer(),
    #                          formatters.TerminalFormatter())
    pprint(colorize_json(format_json(data)))

def handleCallbacks(questions, answers):        
    
    for question in questions:
        
        if 'choices' in question:
            questionName = question['name']
            answer = answers[questionName]
            possibleChoices = question['choices']
            if possibleChoices is not None:
                #find the choice that matches the answer
                for opt in possibleChoices:
                    if opt['name'] == answer:
                        opt['callback'](answers)
                        
def handleFurtureCallbacks(questions, answers):
    
    for key in answers:
        ans = answers[key] 
        future = asyncio.ensure_future(ans)
        
        def on_future_done(future):
            result = future.result()
            print("result is " + result)
            #To Do, use the result to call the callback
        
        future.add_done_callback(on_future_done)