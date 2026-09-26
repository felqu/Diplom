# Границы сервисов

| Контекст | Владелец данных | Основные события |
| --- | --- | --- |
| Идентификация | identity-service | `UserBlocked`, `RoleChanged` |
| Знания | knowledge-base-service | `DocumentIndexed` |
| Оценивание | assessment-service | `TestPublished` |
| Прохождение | testing-service | `TestAssigned`, `TestCompleted` |
| Адаптация | adaptive-learning-service | `RecommendationCreated` |
| Аналитика | analytics-service | Потребляет события, не владеет транзакционными данными |
