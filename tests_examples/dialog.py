# Фио: Цветкова Полина Анатольевна
# Дата: 14.11.2026
# Время: 16:17
# Описание: Этот код обрабатывает системное окно beforeunload, ловит событие dialog, проверяет тип и закрывает окно 
# через dismiss(), а page.close(run_before_unload=True) закрывает страницу с учётом этого события — 
# то есть сначала показывает и обрабатывает диалог, а уже потом завершает работу страницы.
def handle_dialog(dialog):
    assert dialog.type == 'beforeunload'
    dialog.dismiss()

page.on('dialog', handle_dialog)
page.close(run_before_unload=True)