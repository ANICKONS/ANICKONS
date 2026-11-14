<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=200&section=header&text=ANICKON&fontSize=64&fontColor=ffffff&animation=fadeIn&fontAlignY=40" alt="ANICKON" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=1200&color=36BCF7&center=true&vCenter=true&width=620&height=40&lines=%D0%9F%D0%B8%D1%88%D1%83%20%D0%BA%D0%BE%D0%B4%20%D0%B8%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D1%83%D1%8E%20%D0%B5%D0%B3%D0%BE;%D0%94%D0%B5%D1%81%D0%BA%D1%82%D0%BE%D0%BF%D0%BD%D1%8B%D0%B5%20%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B8%20%D0%BC%D0%BE%D0%B4%D1%8B%20%D0%B4%D0%BB%D1%8F%20%D0%B8%D0%B3%D1%80;QA%20%D0%B8%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BE%D0%BA" alt="Пишу код и тестирую его. Десктопные приложения и моды для игр. QA и автоматизация проверок."/>

<br/>

<a href="https://vk.com/anickon"><img src="https://img.shields.io/badge/VK-0077FF?style=flat&logo=vk&logoColor=white" alt="VK"/></a>
<a href="https://t.me/An1ckon"><img src="https://img.shields.io/badge/Telegram-26A5E4?style=flat&logo=telegram&logoColor=white" alt="Telegram"/></a>
<a href="https://github.com/ANICKONS"><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white" alt="GitHub"/></a>
<a href="https://boosty.to/anickon"><img src="https://img.shields.io/badge/Boosty-F15F2C?style=flat&logo=boosty&logoColor=white" alt="Boosty"/></a>
<a href="mailto:anickon.mi@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=flat&logo=gmail&logoColor=white" alt="Email"/></a>

</div>

## Коротко о себе

Я ANICKON. Пишу десктопные приложения на Electron и React и моды для игр на C#. Тестирование для меня часть разработки, а не отдельный шаг в конце: я знаю, как всё это ломается изнутри, поэтому в своих проектах не оставляю проверку на потом.

Что из тестирования у меня уже есть в проектах:

- **Автоматические сценарии.** В MOP-REVIVAL и My-Summer-Frames есть внутриигровой тест-бот со сценариями. Отдельный скрипт ставит сборку в игру, прогоняет сессию и потом возвращает сохранение и настройки как было.
- **Замеры перед релизом.** Любое изменение производительности я проверяю в самой игре: FPS до и после, на конкретной видеокарте. Без цифр в релиз не идёт.
- **Совместимость.** Для MOP-REVIVAL есть правила под 43 других мода и публичная [страница совместимости](https://anickons.github.io/MOP-REVIVAL/), где видно, что с чем работает.
- **Багрепорты.** В моде есть кнопка «Report bug», которая сама прикладывает логи, чтобы баг было легко воспроизвести.
- **Проверка данных.** В ULTIMA редактор проверяет обязательные поля и подсвечивает ошибки в переводе, а не даёт сохранить сломанный файл.
- **Веб.** В IDELUXE-STUDIO перед выпуском прогоняю lint, проверку типов и production-сборку, плюс ручные проверки в браузере.

## Главные проекты

### [ULTIMA](https://github.com/ANICKONS/ULTIMA): редактор для перевода модов Baldur's Gate 3

Открываешь `.pak` или `.xml`, слева оригинал, справа перевод. Можно переводить через Google Translate или локальную модель через Ollama. Есть поиск и фильтры по таблице, защита от потери несохранённых изменений, история проектов и автообновление через GitHub Releases.

К нему есть набор вспомогательных инструментов, [ULTIMA_TOOLS](https://github.com/ANICKONS/ULTIMA_TOOLS): один вытаскивает строки из .NET-сборок модов и возвращает их обратно, другой переводит строки чужого мода прямо в памяти, не трогая его .dll. Сборку и выпуск релизов делает GitHub Actions.

`Electron` `React 19` `Vite` `Tailwind` `C#` `.NET`

### [IDELUXE-STUDIO](https://github.com/ANICKONS/IDELUXE-STUDIO): сайт платформы для видеомонтажёра IDELUXE

Лендинг с космическим фоном (звёзды на canvas, планета на WebGL), тарифы с оплатой через Telegram-бота, вход по почте, через Telegram и Google, каталог туториалов с плеером и прогрессом просмотра, каталог ресурсов и ИИ-ассистент для старшего тарифа. Код разложен по модулям (`features`, `content`, `config`), дизайн-система собрана на токенах.

`Next.js 16` `React 19` `TypeScript` `Tailwind 4` `Better Auth` `SQLite`

## Другие проекты

**[MOP-REVIVAL](https://github.com/ANICKONS/MOP-REVIVAL)** — мод, который повышает FPS в My Summer Car. Продолжение старого MOP, переделанное под нынешнюю версию игры. Интерфейс на английском, русском и польском.
`C#` `MSCLoader` `Unity`

**[My-Summer-Frames](https://github.com/ANICKONS/My-Summer-Frames)** — мод, который добавляет в My Summer Car DLSS, FSR, генерацию кадров и NVIDIA Reflex. Игра старая (Unity 5, DirectX 11), поэтому векторы движения я считаю сам из буфера глубины, а генерацию кадров запускаю через отдельный мост на DirectX 12. Проверял на RTX 5070 Ti.
`C#` `C++` `DirectX` `DLSS` `FSR`

**[Cyberpunk Mod Launcher](https://github.com/ANICKONS/cyberpunk-unreal-launcher)** — лаунчер для сборки модов Cyberpunk 2077 в стиле Найт-Сити. Скачивает и ставит сборку одной кнопкой, следит за версиями, запускает игру через Mod Organizer 2.
`Electron` `React` `TypeScript`

## С чем работаю

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![C#](https://img.shields.io/badge/C%23-512BD4?style=flat-square&logo=csharp&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![Electron](https://img.shields.io/badge/Electron-2B2E3A?style=flat-square&logo=electron&logoColor=9FEAF9)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=flat-square&logo=powershell&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

<details>
<summary><b>Статистика GitHub</b></summary>
<br/>
<div align="center">

<img src="https://raw.githubusercontent.com/ANICKONS/ANICKONS/main/assets/stats.svg" alt="Статистика GitHub" width="48%"/>
<img src="https://raw.githubusercontent.com/ANICKONS/ANICKONS/main/assets/langs.svg" alt="Языки" width="48%"/>

</div>
</details>

## Связаться

Почта: [anickon.mi@gmail.com](mailto:anickon.mi@gmail.com) · Telegram: [@An1ckon](https://t.me/An1ckon) · VK: [vk.com/anickon](https://vk.com/anickon)

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,100:0f2027&height=100&section=footer" alt="" width="100%"/>

</div>
