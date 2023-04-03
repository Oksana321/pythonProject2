from selene import have
from selene.support.shared import browser

completed = have.css_class('completed')
class TodoMVC:
    def __init__(self):
        self.todo_list = browser.all('#todo-list>li')

    def open(self):
        browser.open('http://todomvc4tasj.herokuapp.com/')
        app_loaded = "return $._data($('#clear-completed')[0], 'events')" \
                     ".hasOwnProperty('click')"
        browser.should(have.js_returned(True, app_loaded))
        return self

    def add(self, *todos: str):
        for todo in todos:
            browser.element()