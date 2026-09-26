# Границы сервисов

| Контекст | Владелец данных | Основные события |
| --- | --- | --- |
| Идентификация и оргструктура | identity-organization-service | `UserBlocked`, `RoleChanged` |
| Знания и AI-генерация | knowledge-ai-service | `DocumentIndexed`, `TestGenerated` |
| Оценивание и прохождение | assessment-testing-service | `TestPublished`, `TestAssigned`, `TestCompleted` |
| Адаптация | adaptive-learning-service | `RecommendationCreated` |
| Аналитика | analytics-service | Потребляет события, не владеет транзакционными данными |
| Отчётность и уведомления | reporting-notification-service | `ReportGenerated`, `NotificationSent` |
