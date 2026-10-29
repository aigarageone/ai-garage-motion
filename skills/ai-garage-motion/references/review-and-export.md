# Review & export / Перевірка й експорт

## English

### First assembly

Watch the entire draft at normal speed. Check whether each scene develops the message, the action feels intentional, all required text is readable, transitions connect, and the ending has enough space. Inspect shape, lighting, contact, cropping, layer conflicts, identity, blur, and focus. Listen to the complete mix and any problem layers.

Write actionable notes: `time range → visible/audible issue → likely cause → correction → recheck`. Fix substantial causes and review the changed regions with their neighbors, then the whole film. Compare against the brief after simplifying: removing required content is not a quality improvement.

### Export contract

The brief controls duration, size, fps, codecs, and sound. If unspecified, target MP4 with 1920×1080, 60 fps, H.264, yuv420p, and AAC when there is sound. Keep editable source and a reproducible render command. Record the real tool versions and required asset paths.

For a frame sequence, render exactly the chosen number of frames in order at `i / fps`. Capture after fonts, assets, and renderer state are ready. Do not use wall-clock animation or random unseeded simulation for a supposedly reproducible export.

An example encoding command for an existing 60 fps sequence and already mixed audio:

```bash
ffmpeg -n -framerate 60 -i frames/%06d.png -i mix.wav \
  -c:v libx264 -pix_fmt yuv420p -crf 18 \
  -c:a aac -b:a 192k -movflags +faststart final.mp4
```

Adjust paths, frame rate, audio length, and settings to the actual project. `-n` prevents overwriting an existing file. For explicit silence, omit the audio input and audio codec options. Do not add `-shortest` reflexively: a short audio file can truncate required video. Match the mix duration deliberately.

### Inspect the file that will be delivered

```bash
ffprobe -v error -show_entries \
  format=duration:stream=codec_type,codec_name,width,height,avg_frame_rate,pix_fmt \
  -of json final.mp4
ffmpeg -v error -i final.mp4 -f null -
```

Metadata and a full decode can reveal technical problems. They do not establish readable timing, musical quality, or a successful visual idea. Separately inspect decoded opening, closing, boundaries, and complex moments, then perform full motion playback and listening where tools permit.

Report technical checks, sampled visual inspection, and full audiovisual review separately. For unavailable checks, state the limitation and its practical effect. Stop after the brief is satisfied and material defects are repaired; keep optional alternatives out of required rework.

## Українською

### Перша збірка

Переглянь увесь чорновик на звичайній швидкості. Перевір розвиток думки, вмотивованість дій, читабельність обов'язкового тексту, зв'язність переходів і достатній час завершення. Оціни форму, світло, контакт, обрізання, конфлікти шарів, ідентичність, розмиття та фокус. Прослухай повний мікс і проблемні шари.

Записуй конкретні зауваження: `інтервал → видима/чутна проблема → імовірна причина → правка → повторна перевірка`. Виправ причини, переглянь змінені ділянки із сусідніми та весь ролик. Після спрощення звірся з брифом: вилучення потрібного змісту не є покращенням.

### Умови експорту

Тривалість, розмір, fps, кодеки та звук визначає бриф. Якщо їх не задано, орієнтир — MP4, 1920×1080, 60 fps, H.264, yuv420p і AAC за наявності звуку. Збережи редаговані вихідники, команду рендеру, фактичні версії інструментів та потрібні шляхи ресурсів.

Рендери всі кадри послідовно в момент `i / fps`, після готовності шрифтів, ресурсів і стану рушія. Відтворюваний експорт не має залежати від реального часу або випадкової симуляції без seed.

Команди вище показують кодування готової послідовності 60 fps із готовим міксом та перевірку файлу. Заміни шляхи й параметри на фактичні. `-n` захищає наявний файл від перезапису. Для тиші прибери аудіовхід і аудіопараметри. Не додавай `-shortest` автоматично: короткий звук може обрізати відео. Узгодь тривалість міксу свідомо.

### Перевірка саме фінального файлу

Метадані та повне декодування виявляють технічні дефекти, але не доводять читабельність, якість музики чи вдалу режисуру. Окремо перевір декодовані початок, кінець, межі сцен і складні моменти, потім переглянь рух і прослухай ролик повністю, якщо інструменти це дозволяють.

Розділяй технічні перевірки, вибіркову перевірку кадрів і повний аудіовізуальний перегляд. Для недоступного кроку вкажи обмеження та його наслідок. Завершуй після виконання брифу й виправлення суттєвих дефектів; необов'язкові альтернативи не мають блокувати здачу.
