from telebot import types
# from telegram_bot_pagination import InlineKeyboardPaginator
import requests

lis_ccy_en = [i["Ccy"] + " → " + i["CcyNm_EN"] for i in
              requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/").json()]
lis_ccy_ru = [i["Ccy"] + " → " + i["CcyNm_RU"] for i in
              requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/").json()]

# paginator = InlineKeyboardPaginator(8, current_page=1, data_pattern=len(lis_ccy_en))

dictionary_en = {"happy": "счастливый", "perplexed": "озадаченный",
                 "cat": "кошка", "harmony": "гармония",
                 "run": "бегать", "deceive": "обманывать",
                 "blue": "синий", "pen": "ручка",
                 "mobile": "мобильные", "exacerbate": "обострять", "serendipity": "случайность",
                 "ephemeral": "эфемерный",
                 "cap": "кепка",
                 "jump": "прыгать",
                 "encounter": "сталкиваться",
                 "benevolent": "доброжелательный",
                 "laptop": "ноутбук", "picture": "картина", "maybe": "может быть", "car": "машина"}

dictionary_ru = {value: key for key, value in dictionary_en.items()}

wikipedia_dic_en = {
    "python": "Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. It has a large standard library and a vibrant community, making it suitable for various applications, from web development and data analysis to artificial intelligence and scientific computing.",
    "java": "Java is a widely-used, object-oriented programming language developed by Sun Microsystems (now owned by Oracle Corporation) in the mid-1990s. It was designed to be platform-independent, meaning that Java programs can run on any device or operating system that has a Java Virtual Machine (JVM) installed. Java is known for its write once, run anywhere mantra, making it popular for building large-scale, enterprise-level applications, web applications, mobile apps (using Android), and more. It's also widely used in backend development, particularly in enterprise environments. Java's syntax is similar to C++, making it relatively easy for developers to transition to from other languages.",
    "js": "JavaScript (JS) is a high-level, interpreted programming language primarily used for adding interactivity and dynamic behavior to web pages. It was created by Brendan Eich at Netscape in 1995 and has since become one of the most widely used programming languages. JavaScript allows developers to manipulate HTML and CSS, handle events, create animations, and interact with web browsers. It is commonly used in frontend web development, but with the advent of technologies like Node.js, it can also be used for server-side development. JavaScript is often used alongside HTML and CSS to create modern, interactive web applications.",
    "c++": "C++ is a powerful, general-purpose programming language developed by Bjarne Stroustrup in the early 1980s. It is an extension of the C programming language with added features such as object-oriented programming (OOP) and generic programming. C++ is widely used for developing system software, game engines, desktop applications, embedded systems, and performance-critical applications. It provides a rich standard library and supports low-level programming, making it suitable for building efficient and scalable software. C++ is known for its performance and flexibility but can have a steeper learning curve compared to other languages due to its complexity.",
    "c": "C is a powerful and widely used procedural programming language developed in the early 1970s by Dennis Ritchie at Bell Labs. It is known for its efficiency, flexibility, and portability, making it suitable for a wide range of applications, including system programming, embedded systems, and developing operating systems. C is often referred to as the mother of all programming languages due to its influence on the development of many other languages. It provides low-level access to memory, making it suitable for developing software where performance and control over hardware are critical. Despite being an older language, C remains popular and relevant today, particularly in fields where performance and efficiency are paramount.",
    "assembly": "Assembly language, often referred to simply as assembly, is a low-level programming language that closely corresponds to machine code instructions for a specific computer architecture. Each assembly language instruction typically corresponds to a single machine instruction, making it a human-readable representation of machine code. Programmers use assembly language to write programs that directly control the computer's hardware at a low level. Assembly language is specific to the architecture of the target processor, meaning that programs written in assembly for one type of processor will not run on another type without modification. Despite its low-level nature and complexity, assembly language provides programmers with precise control over the hardware, allowing them to optimize code for performance-critical applications such as device drivers, real-time systems, and embedded systems. However, due to its complexity and architecture-specific nature, assembly language programming is less common than high-level programming languages in most modern software development scenarios.",
    "go": "Go, also known as Golang, is a statically typed, compiled programming language developed by Google in 2007 and released to the public in 2009. It was designed with simplicity, efficiency, and concurrency in mind, aiming to provide a modern and productive language for building scalable and reliable software systems.Go features a clean and concise syntax, garbage collection, built-in support for concurrency through goroutines and channels, and a rich standard library. It is well-suited for developing web servers, network services, cloud-native applications, and distributed systems.Go's simplicity and performance make it popular among developers for a wide range of applications, from web development to system programming. Its concurrency primitives make it particularly well-suited for writing concurrent and parallel programs, allowing developers to efficiently utilize multicore processors and handle concurrent tasks easily.",
    "ruby": "Ruby is a dynamic, object-oriented programming language with a focus on simplicity and productivity. It was designed by Yukihiro Matsumoto (Matz) in the mid-1990s and released to the public in 1995. Ruby emphasizes human-readable syntax and follows the principle of least surprise, aiming to make programming enjoyable and natural for developers.Key features of Ruby include:\n1. Object-oriented: Everything in Ruby is an object, including primitive data types. It supports classes, inheritance, and mixins.\n2. Dynamic typing: Ruby is dynamically typed, meaning that variable types are determined at runtime.\n3. Blocks and Procs: Ruby has first-class support for blocks, which are chunks of code that can be passed around like objects. Procs are Ruby's version of anonymous functions.\n4. Metaprogramming: Ruby allows for powerful metaprogramming techniques, enabling developers to write code that can modify itself at runtime.\n5. Rails: Ruby on Rails, often simply referred to as Rails, is a popular web application framework written in Ruby. It follows the convention over configuration (CoC) and don't repeat yourself (DRY) principles, allowing developers to build web applications quickly and efficiently.\nRuby's elegant syntax and focus on developer happiness have made it a favorite among web developers, particularly for building web applications and prototypes rapidly. However, its performance can be a concern for performance-critical applications, leading some developers to choose other languages for such use cases.",
    "html is not language": "HTML (Hypertext Markup Language) is the standard markup language used for creating web pages and web applications. It defines the structure and content of a webpage by using a system of tags and attributes. HTML documents consist of a series of elements, each represented by tags enclosed in angle brackets.Key features of HTML include:\n1. Tags: HTML documents are made up of tags, which define the structure and content of the page. Tags are enclosed in angle brackets (< >) and typically come in pairs, with an opening tag and a closing tag.\n2. Attributes: Tags can have attributes, which provide additional information about the element. Attributes are specified within the opening tag and typically consist of a name and a value.\n3. Structure: HTML documents have a hierarchical structure, with elements nested inside other elements to represent the layout and organization of content on the page.\n4. Semantics: HTML provides semantic elements that convey meaning about the content they contain, such as headings, paragraphs, lists, and tables. This helps improve accessibility and search engine optimization.\n5. Compatibility: HTML is supported by all modern web browsers and is compatible with various devices and platforms, making it suitable for creating cross-platform web content.\nHTML is often used in conjunction with CSS (Cascading Style Sheets) and JavaScript to create visually appealing and interactive web pages. CSS is used to style the appearance of HTML elements, while JavaScript is used to add interactivity and dynamic behavior to web pages.",
    "css is not language": "CSS (Cascading Style Sheets) is a style sheet language used to describe the presentation of a document written in HTML or XML. It controls the layout, appearance, and formatting of web pages, allowing developers to define styles such as colors, fonts, margins, and positioning.\nKey features of CSS include:\n1. Selectors: CSS selectors are patterns used to select and style HTML elements. They can target elements based on their tag name, class, ID, attributes, or relationship with other elements.\n2. Properties: CSS properties define the visual appearance of selected elements. Properties include attributes like color, font-size, width, height, margin, padding, background-color, and many others.\n3. Values: CSS properties are assigned values that specify how the selected elements should be styled. Values can be keywords, such as bold or italic, or numerical values, such as pixel measurements or percentages.\n4. Cascading: CSS follows a cascading mechanism, meaning that multiple style sheets can be applied to a single HTML document, and conflicting styles are resolved based on specificity and the order of precedence.\n5. Responsive design: CSS allows developers to create responsive layouts that adapt to different screen sizes and devices. Techniques like media queries and flexbox/grid layouts are commonly used to achieve responsive designs.\n6. Modularization: CSS can be organized into separate files and reused across multiple web pages, making it easier to maintain and update the styling of a website.\nCSS is an essential tool for web developers and designers, enabling them to create visually appealing and user-friendly web interfaces. It works seamlessly with HTML and JavaScript to enhance the presentation and functionality of web page\n"
}

wikipedia_dic_ru = {
    "python": "Python - это высокоуровневый интерпретируемый язык программирования, известный своей простотой и читаемостью. Он поддерживает несколько парадигм программирования, включая процедурное, объектно-ориентированное и функциональное программирование. Python широко используется в различных областях, таких как веб-разработка, наука о данных, искусственный интеллект, автоматизация и многое другое. У него обширная экосистема библиотек и фреймворков, что делает его универсальным и мощным для различных приложений.",
    "java": "Java - это высокоуровневый объектно-ориентированный язык программирования, который изначально разрабатывался компанией Sun Microsystems, а теперь поддерживается компанией Oracle. Он известен своей платформонезависимостью, что означает, что программы, написанные на Java, могут выполняться на разных операционных системах без изменений в их исходном коде. Java широко используется для создания корпоративных приложений, веб-приложений, мобильных приложений (с помощью платформы Android), игр и других программных продуктов. Язык Java также известен своей обширной библиотекой стандартных классов (Java API) и популярными фреймворками, такими как Spring, Hibernate и Apache Struts.",
    "js": "JavaScript (JS) - это интерпретируемый язык программирования, который чаще всего используется для создания динамических веб-сайтов и веб-приложений. Он позволяет добавлять интерактивность на веб-страницы, взаимодействие с пользователем, асинхронную загрузку данных и многое другое. JavaScript работает в браузере пользователя и может изменять содержимое веб-страницы, обрабатывать события, валидировать формы и выполнять множество других действий. Он также может использоваться на сервере с помощью платформы Node.js для создания серверных приложений и API. JavaScript является одним из наиболее популярных языков программирования в мире веб-разработки.",
    "c++": "C++ - это компилируемый язык программирования, созданный в начале 1980-х годов Бьярном Страуструпом в Bell Labs как расширение языка программирования C. C++ сочетает в себе возможности низкоуровневого программирования, характерные для C, с возможностями объектно-ориентированного программирования. Он широко используется для разработки высокопроизводительных приложений, таких как игры, операционные системы, библиотеки и фреймворки, а также для системного программирования и программирования реального времени. C++ обладает богатой стандартной библиотекой и множеством расширений и фреймворков, что делает его мощным и гибким инструментом для разработчиков.",
    "c": "C - это компилируемый язык программирования, который изначально был разработан в 1972 году Деннисом Ритчи в компании Bell Labs. Он является одним из самых важных и влиятельных языков программирования в истории компьютерной науки. C широко используется для разработки операционных систем, компиляторов, встраиваемого программного обеспечения, приложений реального времени, игр и многих других приложений. Язык C обладает низкоуровневым синтаксисом, что позволяет программистам эффективно управлять ресурсами компьютера, такими как память и процессорное время. Он также служит основой для многих других языков программирования, таких как C++ и Objective-C.",
    "assembly": "Assembly - это низкоуровневый язык программирования, который представляет собой непосредственное отражение инструкций, понятных процессору компьютера. Программы, написанные на языке ассемблера, состоят из инструкций, которые выполняют конкретные операции над данными, хранящимися в памяти или регистрах процессора. Поскольку ассемблер тесно связан с аппаратным обеспечением компьютера, он обладает непосредственным управлением над аппаратурой и может быть использован для оптимизации производительности или для доступа к особенностям аппаратного обеспечения. Однако язык ассемблера является сложным для понимания и написания, поэтому его использование ограничено в сравнении с более высокоуровневыми языками программирования.",
    "go": "Go, также известный как Golang, это открытый язык программирования, разработанный в Google. Он сочетает в себе выразительность и простоту использования динамических языков, таких как Python, с производительностью и безопасностью статически типизированных языков, таких как C++ или Java. Go был создан для создания эффективных, надежных и масштабируемых программных систем. Он обладает встроенной поддержкой параллелизма и конкурентности, что делает его особенно подходящим для написания высоконагруженных сетевых и веб-приложений. Кроме того, Go имеет компилятор, который генерирует исполняемый код для различных платформ, что делает его переносимым. Go также обладает богатой стандартной библиотекой и активным сообществом разработчиков.",
    "ruby": "Ruby - это динамический, интерпретируемый язык программирования, который был создан в Японии в конце 1990-х годов. Он известен своей простотой и элегантностью, а также своей философией программистского счастья, нацеленной на удобство программистов. Ruby часто используется для веб-разработки, в том числе для создания веб-приложений и серверных приложений. Он также популярен в кругах разработки программного обеспечения благодаря своей гибкости и возможностям метапрограммирования. Ruby обладает богатой стандартной библиотекой и активным сообществом разработчиков, которые создают и поддерживают множество библиотек и фреймворков для различных целей.",
    "html не язык програмирование": "HTML (HyperText Markup Language) - это стандартный язык разметки для создания веб-страниц и веб-приложений. С помощью HTML можно определить структуру и содержимое веб-страницы с помощью различных элементов и тегов. Каждый элемент HTML представляет собой различные части веб-страницы, такие как заголовки, параграфы, списки, ссылки, изображения и многое другое. HTML использует теги для определения начала и конца элементов, а также для применения различных свойств и атрибутов к содержимому. HTML является основой для создания содержания веб-страниц и взаимодействия с пользователем в интернете.",
    "css не язык програмирование": "CSS (Cascading Style Sheets) - это язык таблиц стилей, который используется для оформления и внешнего оформления веб-страниц и веб-приложений. CSS позволяет разработчикам определять внешний вид и расположение элементов HTML, таких как текст, изображения, кнопки и другие элементы, путем применения различных стилей и свойств. Это включает в себя задание цветов, шрифтов, размеров, отступов, границ, анимаций и многого другого. CSS используется в сочетании с HTML для создания эстетически привлекательных и пользовательских веб-интерфейсов. Он также поддерживает концепцию каскадирования, что позволяет применять стили в разных частях веб-страницы с разной приоритетностью."
}

# Dictionary for en
dictionary_lis_en = [i for i in dictionary_en.keys()]
words = ""
count = 1
for i in dictionary_en:
    words += f"{count}. {i} \n"
    count += 1
# ----------------------------------------------------------------

#   Dictionary  for russian
dictionary_lis_ru = [i for i in dictionary_ru.keys()]
words_1 = ""
count_1 = 1
for i in dictionary_ru:
    words_1 += f"{count_1}. {i} \n"
    count_1 += 1


# ----------------------------------------------------------------


def language():
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    en = types.KeyboardButton("English ")
    ru = types.KeyboardButton("Russian ")
    mark.add(en, ru)
    return mark


def ccy_button_en():
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in lis_ccy_en:
        button = types.KeyboardButton(i)
        mark.add(button)
    return mark


def ccy_button_ru():
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in lis_ccy_ru:
        button = types.KeyboardButton(i)
        mark.add(button)
    return mark


def menu_en():
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("From ... to UZS")
    button2 = types.KeyboardButton("Dictionary")
    button3 = types.KeyboardButton("Wikipedia")
    button4 = types.KeyboardButton("From UZS to ...")
    button5 = types.KeyboardButton("Info about currency")
    mark.add(button1, button4, button2, button3, button5)
    return mark


def menu_ru():
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("С ... НА UZS")
    button2 = types.KeyboardButton("Словарь")
    button3 = types.KeyboardButton("Википедия")
    button4 = types.KeyboardButton("С UZS НА ... ")
    button5 = types.KeyboardButton("Информация о валютах")
    mark.add(button1, button4, button2, button3, button5)
    return mark


def rate(money, first, second="UZS"):
    a = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/" + first + "/").json()
    total_sum = (f" 1 {first} = {a[0]["Rate"]} {second} \n"
                 f" {money} {first} = {round(float(money * float(a[0]["Rate"])), 2)} {second}")
    return total_sum


def from_uzs_to_foreign(money=14556, first="UZS", second="USD"):
    a = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/" + second + "/").json()
    total_sum = (f" 1 {second} = {a[0]["Rate"]} {first} \n"
                 f" {money} {first} = {round(float(money / float(a[0]["Rate"])), 2)} {second}")
    return total_sum


def inline_currency_en():
    # total_pages = len(lis_ccy_en)
    mar = types.InlineKeyboardMarkup(row_width=3)
    for i in requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/").json():
        button = types.InlineKeyboardButton(text=i["Ccy"] + " → " + i["CcyNm_EN"],
                                            callback_data=i["Ccy"] + " → " + i["CcyNm_EN"])
        mar.add(button)
    left_button = types.InlineKeyboardButton("←", callback_data="left")
    page_button = types.InlineKeyboardButton("1/4", callback_data="page")
    right_button = types.InlineKeyboardButton("→", callback_data="right")
    mar.add(left_button, page_button, right_button)

    return mar


def inline_currency_ru():
    mar = types.InlineKeyboardMarkup(row_width=5)
    for i in requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/").json():
        button = types.InlineKeyboardButton(text=i["Ccy"] + " → " + i["CcyNm_RU"],
                                            callback_data=i["Ccy"] + " → " + i["CcyNm_RU"])
        mar.add(button)
    return mar


def info_about_ccy_ru(ccy):
    info = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/" + ccy[:3].upper() + "/").json()
    whole_info = (f"Курс: {info[0]["Rate"]},\n"
                  f"Валюта: {info[0]["Ccy"]},\n"
                  f"Название: {info[0]["CcyNm_RU"]},\n"
                  f"Дата обнавления: {info[0]["Date"]}\n")
    return whole_info


def info_about_ccy_en(ccy):
    info = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/" + ccy[:3].upper() + "/").json()
    whole_info = (f"Rate: {info[0]["Rate"]},\n"
                  f"Currency: {info[0]["Ccy"]},\n"
                  f"Currency name: {info[0]["CcyNm_EN"]},\n"
                  f"Update date: {info[0]["Date"]}\n")
    return whole_info


def wikipedia_ru():
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in wikipedia_dic_ru.keys():
        button = types.KeyboardButton(i)
        mar.add(button)
    return mar


def wikipedia_en():
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in wikipedia_dic_en.keys():
        button = types.KeyboardButton(i)
        mar.add(button)
    return mar