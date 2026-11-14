# Фио: Цветкова Полина Анатольевна
# Дата: 12.11.2026
# Время: 12:02
# Описание: Этот тест создаёт задачу через браузер, открывает страницу, заполняет поля, нажимает кнопку «Отправить»,
# а проверяет через API. Номер задачи извлекает из адреса страницы после создания, затем делает запрос к серверу и 
# убеждается, что задача действительно сохранилась и у неё правильные заголовок и описание.
def test_last_created_issue_should_be_on_the_server(api_request_context: APIRequestContext, page: Page) -> None:
    page.goto(f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/issues")
    page.locator("text=New issue").click()
    page.locator("[aria-label='Title']").fill("Bug report 1")
    page.locator("[aria-label='Comment body']").fill("Bug description")
    page.locator("text=Submit new issue").click()
    issue_id = page.url.split("/")[-1]

    new_issue = api_request_context.get(f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/issues/{issue_id}")
    assert new_issue.ok
    assert new_issue.json()["title"] == "[Bug] report 1"
    assert new_issue.json()["body"] == "Bug description"