from time import sleep
from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

browser.open('http://todomvc.com/examples/emberjs')

def test_add():
    s('#new-todo').type('a').press_enter()
    s('#new-todo').type('b').press_enter()
    s('#new-todo').type('c').press_enter()
    sleep(2)
    assert ss('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

def test_clear_completed():
    ss('#todo-list>li').element_by(have.exact_text('b')).element('.toggle').click()
    sleep(2)
    s('#clear-completed').click()
    assert ss('#todo-list>li').should(have.exact_texts('a', 'c'))
