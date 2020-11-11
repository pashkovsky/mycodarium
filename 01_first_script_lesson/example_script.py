from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

# ARRANGE
browser.config.hold_browser_open = True
browser.open('http://todomvc.com/examples/emberjs/')

# ACTS
s('[id="new-todo"]').type('Listen Lesson').press_enter()
s('[id="new-todo"]').type('Listen Book').press_enter()
s('[id="new-todo"]').type('Watch TV').press_enter()

# ASSERT
ss('[id="todo-list"] li').should(have.exact_texts('Listen Lesson.', 'Listen Book', 'Watch TV'))

