# Фио: Цветкова Полина Анатольевна
# Дата: 12.11.2026
# Время: 13:56
# Описание: этот код через фикстуру api_request_context создаёт две задачи в репозитории GitHub («request 1», затем «request 2»), открывает страницу со списком задач и проверяет, 
# что первым элементом является самая свежая задача «[Feature] request 2», 
# то есть список отсортирован по убыванию даты создания.
def test_last_created_issue_should_be_first_in_the_list(api_request_context: APIRequestContext, page: Page) -> None:
    def create_issue(title: str) -> None:
        data = {
            "title": title,
            "body": "Feature description",
        }
        new_issue = api_request_context.post(
            f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data
        )
        assert new_issue.ok
    create_issue("[Feature] request 1")
    create_issue("[Feature] request 2")
    page.goto(f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/issues")
    first_issue = page.locator("a[data-hovercard-type='issue']").first
    expect(first_issue).to_have_text("[Feature] request 2")