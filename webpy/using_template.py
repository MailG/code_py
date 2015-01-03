#!python


import web

def test_func(id):
	return "test_func"

render = web.template.render('.')
print render.test('world')

hello = web.template.frender('test.html')
print hello('world')


template = "$def with (name)\nHello $name"
hello = web.template.Template(template)
print hello('world')


