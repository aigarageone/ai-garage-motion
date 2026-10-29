# Maintaining the package / Підтримка пакета

## English

The repository uses Python 3.9+ and the standard library only. There is no automatic publishing workflow or background service.

```bash
python3 scripts/package.py --check
python3 scripts/package.py
```

The first command checks Python syntax, the skill entrypoint, license consistency, and local Markdown links. The second also creates deterministic skill and source ZIPs plus `SHA256SUMS.txt` in `dist/`. Existing artifacts are never overwritten. The source archive uses an explicit file set: root documentation and the `docs/`, `scripts/`, and `skills/` directories. It excludes Git history, `dist/`, bytecode, and runtime outputs. It is not a secret scanner; review every public file before publishing.

Test the installer in an isolated home or project directory. Check both agents, user/project scopes, dry runs, complete file copying, and refusal to overwrite. Test planning templates in both languages. Do not install into a contributor's real agent folder merely to test packaging.

For a release, update `VERSION` and the skill metadata together, review English and Ukrainian text, inspect the archives, and upload the three built files to the corresponding GitHub release. Keep the skill asset name `ai-garage-motion.zip` so the stable download link continues to work. The source ZIP retains its version in the name.

Keep future additions generic and free of customer data, private media, credentials, personal filesystem paths, and unlicensed assets. Add only dependencies the production workflow actually needs. State separately whether a change was structurally checked, installed in a sandbox, or evaluated through real video creation. A package test does not prove the artistic quality of future films.

## Українською

Репозиторій потребує Python 3.9+ і лише стандартної бібліотеки. Автоматичної публікації та фонових служб немає.

Перша команда вище перевіряє синтаксис Python, точку входу скіла, узгодженість ліцензій і локальні Markdown-посилання. Друга також створює відтворювані ZIP зі скілом і вихідниками та `SHA256SUMS.txt` у `dist/`. Наявні архіви не перезаписуються. Архів вихідників використовує явний набір: документацію кореня, `docs/`, `scripts/` і `skills/`. Історія Git, `dist/`, байткод і робочі результати виключені. Це не сканер секретів; перед публікацією переглянь кожен файл.

Перевіряй інсталятор в окремій тестовій домашній або проєктній папці. Перевір обох агентів, user/project, dry run, комплектність копіювання та захист від перезапису. Перевір шаблони обома мовами. Не використовуй реальні папки агента для тесту пакування.

Для нового випуску разом онови `VERSION` і метадані скіла, переглянь обидві мови, перевір архіви та завантаж три зібрані файли до відповідного GitHub release. Збережи назву `ai-garage-motion.zip` для стабільного посилання. ZIP із вихідниками містить версію в назві.

Нові матеріали мають залишатися універсальними, без клієнтських даних, приватних медіа, облікових даних, особистих шляхів і неліцензованих ресурсів. Додавай лише потрібні залежності. Розрізняй структурну перевірку, тестове встановлення та перевірку через реальне створення відео. Тести пакета не доводять художньої якості майбутніх роликів.
