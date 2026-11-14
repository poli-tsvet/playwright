# Фио: Цветкова Полина Анатольевна
# Дата: 14.11.2026
# Время: 21:52
# Описание: Этот код берёт данные из sessionStorage одной страницы, сохраняет их в переменную, 
# а потом в другом контексте восстанавливает через скрипт при запуске страницы. 
# Верхний блок - код, нижний - альтернатива, но с await. 

import os
# Get session storage and store as env variable
session_storage = page.evaluate("() => JSON.stringify(sessionStorage)")
os.environ["SESSION_STORAGE"] = session_storage

# Set session storage in a new context
session_storage = os.environ["SESSION_STORAGE"]
escaped_session_storage = session_storage.replace("\\", "\\\\").replace("'", "\\'")
context.add_init_script("""(storage => {
  if (window.location.hostname === 'example.com') {
    const entries = JSON.parse(storage)
    for (const [key, value] of Object.entries(entries)) {
      window.sessionStorage.setItem(key, value)
    }
  }
})('""" + escaped_session_storage + "')")

import os
# Get session storage and store as env variable
session_storage = await page.evaluate("() => JSON.stringify(sessionStorage)")
os.environ["SESSION_STORAGE"] = session_storage

# Set session storage in a new context
session_storage = os.environ["SESSION_STORAGE"]
escaped_session_storage = session_storage.replace("\\", "\\\\").replace("'", "\\'")
await context.add_init_script("""(storage => {
  if (window.location.hostname === 'example.com') {
    const entries = JSON.parse(storage)
    for (const [key, value] of Object.entries(entries)) {
      window.sessionStorage.setItem(key, value)
    }
  }
})('""" + escaped_session_storage + "')")