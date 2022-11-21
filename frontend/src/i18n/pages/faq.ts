export const faqPageLocales = {
  en: {
    faq: [
      {
        title:
          'Is my data (notes / files, etc.) really hidden from strangers (including employees of your company, data center, and others)?',
        text: '<p>Yes, your data is protected as much as possible and is inaccessible to third  parties (neither our company employees, nor potential intruders among the employees  of the data center, provider, or any other persons).</p> <p>All services are implemented with DevSecOps best practices. Multiple  encryption (including end-to-end), traffic encapsulation in TOR and I2P, its masking,  cascading with proxy servers and virtual private networks, as well as innovative  cybersecurity methods allow you to provide the maximum level of protection for your data.</p> <p>We do NOT: collect any logs, collect metrics, statistics about users and have access to user information; we DO bring decentralization to every process. In  addition to multiple encryption, when deleting data, we stochastically overwrite the  data on the data carrier seven times with zeros and ones, leveling the risks even in  case of stealing our equipment or finding an intruder from the data center.</p> <p>Our services preserve your anonymity and ensure the highest possible security of your data.</p>',
      },
      {
        title: 'What types of notes may I create?',
        text: '<p>You can create secret notes as HTTPS links (regular web links that can be opened in any browser) / .onion (links in the TOR overlay network that can only be opened using a TOR browser or TOR mirror) / .i2p (links in the I2P overlay network that can only be opened using an I2P browser or through an I2P mirror).</p> <p>By default, you create a main secret note, but through advanced settings you can create a fake note with misinformation. At the first access, the main note will be opened (after reading it will be permanently destroyed), at the second access - a fake note (after reading it will also be permanently destroyed). On next clicks on the link, the message "The requested page does not exist or the note has already been successfully read;)" will be displayed. The same page opens when going to nonexistent addresses,  which increases the level of anonymity.</p>',
      },
      {
        title: 'Is it necessary to set a password for a note?',
        text: '<p>No, setting a password is optional. <b><i>But pay attention: if you have set a password for one of the notes (for fake or main note) setting a password for the second note is obligatory</i></b>. For convenience and higher speed of communication, you can create only the main note without password. But do not forget that the first time you read the note, the data will be destroyed. If you communicate via a communication channel controlled by an attacker, then there is a risk that he will have time to read it first. To avoid such problems, we recommend setting a password and transmitting it via an alternative communication channel. And also use fake notes to misinform the attacker.</p>',
      },
      {
        title: 'What is the best way to send a link to a note and a password to the recipient?',
        text: '<p>It is better to send a link to the created note through different communication channels in order to diversify the risks when communication channels are compromised. For example, you can use different messengers, E-mail or other tools.</p>',
      },
      {
        title: 'Is it possible to know when the note was read?',
        text: '<p>Yes, you can receive an e-mail notification when a note has been read. We will indicate in the letter only the last four characters of the note, so that you understand which note it is. In some cases, when you do not want an attacker to even potentially establish a correlation between a note and your mail, we strongly recommend that you do not use your personal mail.</p>',
      },
      {
        title: 'Can I view a recently read note multiple times?',
        text: '<p>No, the note can only be read once! If you are worried about the compromise of the communication channel, you can additionally create a fake note as disinformation, which will be opened by the attacker on the second reading attempt. Of course, he will not find out that this is only the second note opening and the note is fake. You can set up a notification of the second access attempt (reading a fake note) by e-mail. On next clicks on the link, the message "The requested page does not exist or the note has already been successfully read;)" will be displayed. The same page opens when going to non-existent addresses, which increases the level of anonymity.</p>',
      },
      {
        title: 'How long are unread notes stored on the server?',
        text: '<p>By default, the unread message lifetime is 365 days. But through the advanced settings, you can set it to 24 hours/week/month or 365 days.</p>',
      },
      {
        title: 'Why may I need fake notes? ',
        text: '<p>Fake notes can be useful for disinforming an attacker who has potentially gained access to a communication channel. This allows you to keep the content of the main note secret.</p> <p>By default, you create a main secret note, but through advanced settings you can create a fake note with misinformation. At the first access, the main note will be opened (after reading it will be permanently destroyed), at the second access - the fake one (after reading it will also be permanently destroyed). On next clicks on the link, the message "The requested page does not exist or the note has already been successfully read;)" will be displayed. The same page opens when going to nonexistent addresses, which increases the level of anonymity.</p>',
      },
      {
        title: 'Are the main and fake notes available through the same link?',
        text: '<p>Yes, the main and fake notes are available at the same link. This is the meaning of misinformation an attacker if your communication channel is compromised.</p>',
      },
      {
        title:
          'Is it possible to find out if there was a second attempt to read the note (a fake note has been opened)?',
        text: '<p>Yes, you can receive an e-mail notification that there was a second attempt to  read the note (a fake note has been opened). We will indicate in the letter only the last  four characters of the note, so that you understand which note it is. In some cases,  when you do not want an attacker to even potentially establish a correlation between  a note and your mail, we strongly recommend that you do not use your personal mail.</p>',
      },
      {
        title: 'How does the service work when creating a main and fake note without  passwords?',
        text: '<p>When creating a main and fake note without passwords, the main note will  open on the first access (it will be permanently destroyed after reading), on the  second access the fake one (it will be permanently destroyed after reading). On next  clicks on the link, the message "The requested page does not exist or the note has  already been successfully read;)" will be displayed. The same page opens when going  to non-existent addresses, which increases the level of anonymity.</p>',
      },
      {
        title: 'How does the service work when creating a main note and a fake note with  identical passwords?',
        text: '<p>When setting identical passwords for the main and fake notes, at the first  opening the main note will be provided (it will be permanently destroyed after  reading), at the second the fake one (it will be permanently destroyed after reading).  On next clicks on the link, the message "The requested page does not exist or the note  has already been successfully read;)" will be displayed. The same page opens when  going to non-existent addresses, which increases the level of anonymity.</p>',
      },
      {
        title: 'How does the service work when creating a main note and a fake note with  different passwords?',
        text: '<p>When setting different passwords for the main and fake notes, after the first  reading of any, both are permanently deleted, because there is only one link, and the  attacker should not deanomize you even by indirect signs. On next clicks on the link,  the message "The requested page does not exist or the note has already been  successfully read;)" will be displayed. The same page opens when going to nonexistent addresses, which increases the level of anonymity.</p>',
      },
      {
        title: 'Does the service keep logs, collect metrics and statistics about users?',
        text: '<p>We do NOT: collect any logs, collect metrics, statistics about users and have  access to user information; we DO bring decentralization to every process. In  addition to multiple encryption, when deleting data, we stochastically overwrite the  data on the data carrier seven times with zeros and ones, leveling the risks even in  case of stealing our equipment or finding an intruder from the data center.</p> <p>Our services preserve your anonymity and ensure the highest possible security  of your data.</p> ',
      },
      {
        title: 'In case of physical access to your servers or their theft - will my data  remain confidential?',
        text: '<p>Yes, your data will remain confidential.<p> <p>All services are implemented with DevSecOps best practices. Multiple  encryption (including end-to-end), traffic encapsulation in TOR and I2P, its masking,  cascading with proxy servers and virtual private networks, as well as innovative  cybersecurity methods allow you to provide the maximum level of protection for  your data.</p> <p>We do NOT: collect any logs, collect metrics, statistics about users and have  access to user information; we DO bring decentralization to every process. In  addition to multiple encryption, when deleting data, we stochastically overwrite the  data on the data carrier seven times with zeros and ones, leveling the risks even in  case of stealing our equipment or finding an intruder from the data center.</p> <p>Our services preserve your anonymity and ensure the highest possible security  of your data.</p>',
      },
    ],
  },
  ru: {
    faq: [
      {
        title:
          'Действительно ли мои данные (записки / файлы и т.д.) скрыты от посторонних (в том числе от сотрудников Вашей компании, датацентра и других лиц)?',
        text: '<p>Да, Ваши данные максимально защищены и недоступны третьим лицам (ни сотрудникам нашей компании, ни потенциальным злоумышленникам из числа сотрудников датацентра, провайдера, ни каким-либо другим лицам).</p> <p>Все сервисы реализуются с соблюдением лучших практик DevSecOps.  Множественное шифрование (в том числе сквозное), инкапсуляция трафика в TOR и I2P, его маскировка, каскадирование с прокси-серверами и виртуальными частными сетями, а также инновационные методы кибербезопасности позволяют обеспечить максимальный уровень защиты Ваших данных. </p> <p>Мы не собираем никакие логи, не ведем сбор метрик, статистик о пользователях, не имеем доступ к пользовательской информации, привносим децентрализацию в каждый процесс. В дополнение к множественному шифрованию при удалении данных мы семикратно стохастически перезаписываем данные на информационном носителе нулями и единицами,  нивелируя риски при краже нашего оборудования и даже нахождении злоумышленника со стороны датацентра.</p> <p>Наши сервисы сохраняют Вашу анонимность и обеспечивают максимально возможную безопасность Ваших данных.</p>',
      },
      {
        title: 'Какие типы записок можно создавать?',
        text: '<p>Вы можете создавать секретные записки в виде ссылок HTTPS (обычные ссылки в Интернете, которые могут быть открыты в любом браузере) / .onion  (ссылки в оверлейной сети TOR, которые могут быть открыты только с использованием TOR браузера или через TOR зеркала) / .i2p (ссылки в оверлейной сети I2P, которые могут быть открыты только с использованием I2P  браузера или через I2P зеркала).</p> <p>По умолчанию Вы создаете основную секретную записку, но через расширенные настройки можете создать и фальшивую записку с дезинформацией. При первом доступе откроется основная записка (после прочтения она будет безвозвратно уничтожена), при втором доступе - фальшивая (после прочтения она также безвозвратно уничтожится). При последующих переходах по ссылке будет выдано сообщение «Запрашиваемой страницы не существует или записка уже была успешно прочитана ;)». Такая же страница открывается и при переходе на несуществующие адреса, что повышает уровень анонимности.</p>',
      },
      {
        title: 'Обязательно ли устанавливать пароль на записку?',
        text: '<p>Нет, установка пароля не является обязательной. <b><i>Однако, обратите внимание, что при установке пароля на одну из записок (фальшивую или основную) обязательно необходимо будет задать пароль и для второй</i></b>. Для удобства и скорости коммуникации Вы можете создавать только основную записку и не задавать для нее пароль. Но не забывайте, что при первом прочтении данные будут уничтожены. Если Вы общаетесь по подконтрольному злоумышленнику каналу связи, то есть риск, что он успеет прочитать ее первым. Во избежание подобных проблем рекомендуем устанавливать пароль и передавать его по альтернативному каналу связи. А также использовать фальшивые записки для дезинформации злоумышленника.</p>',
      },
      {
        title: 'Как лучше передавать получателю ссылку на записку и пароль?',
        text: '<p>Ссылку на созданную записку лучше передавать через разные каналы связи, чтобы диверсифицировать риски при компрометации каналов связи.  Например, Вы можете использовать разные мессенджеры, электронную почту или другие инструменты.<p>',
      },
      {
        title: 'Можно ли узнать, когда записка была прочтена?',
        text: '<p>Да, Вы можете получить на e-mail уведомление о прочтении записки. Мы укажем в письме только последние четыре символа записки, чтобы Вы поняли,  о какой записке идет речь. В некоторых случаях, когда Вы не хотите, чтобы злоумышленник даже потенциально установил корреляцию между запиской и Вашей почтой, категорически не рекомендуем указывать Вашу личную почту.</p>',
      },
      {
        title: 'Можно ли просмотреть недавно прочтенную записку несколько раз?',
        text: '<p>Нет, записка может быть прочитана только один раз! Если Вы переживаете о компрометации канала связи, то можете дополнительно создать фальшивую записку с де зинформацией, которая будет открыт а злоумышленником при втором прочтении. Разумеется, он не будет знать, что это - лишь второе открытие, и ему предоставлена дезинформация. О второй попытке доступа (прочтении фальшивой записки) Вы можете настроить уведомление себе на e-mail. При последующих переходах по ссылке будет выдано сообщение «Запрашиваемой страницы не существует или записка уже была успешно прочитана ;)». Такая же страница открывается и при переходе на несуществующие адреса, что повышает уровень анонимности.</p>',
      },
      {
        title: 'Как долго хранятся непрочтенные записки на сервере?',
        text: '<p>По умолчанию срок жизни непрочитанных сообщений составляет 365  дней. Но через расширенные настройки Вы можете установить его на 24 часа /  неделю / месяц или 365 дней.</p>',
      },
      {
        title: 'Зачем нужны фальшивые записки?',
        text: '<p>Фальшивые записки могут Вам пригодится для дезинформации злоумышленника, потенциально получившего доступ к каналу связи. Это позволяет сохранить в секрете содержание основной записки.</p> <p>По умолчанию Вы создаете основную секретную записку, но через расширенные настройки можете создать и фальшивую записку с дезинформацией. При первом доступе откроется основная записка (после прочтения она будет безвозвратно уничтожена), при втором доступе - фальшивая (после прочтения она также безвозвратно уничтожится). При последующих переходах по ссылке будет выдано сообщение «Запрашиваемой страницы не существует или записка уже была успешно прочитана ;)». Такая же страница открывается и при переходе на несуществующие адреса, что повышает уровень анонимности.</p>',
      },
      {
        title: 'Основная и фальшивая записки доступны по одной ссылке?',
        text: '<p>Да, основная и фальшивая записки доступны по одной ссылке. В этом смысл дезинформации злоумышленника, если Ваш канал связи с получателем информации будет скомпроментирован.</p>',
      },
      {
        title: 'Можно ли узнать, была ли повторная попытка прочтения записки (открытие фальшивой записки)?',
        text: '<p>Да, Вы можете получить на e-mail уведомление о повторной попытке прочтения записки (открытие фальшивой записки). Мы укажем в письме только последние четыре символа записки, чтобы Вы поняли, о какой записке идет речь. В некоторых случаях, когда Вы не хотите, чтобы злоумышленник даже потенциально установил корреляцию между запиской и Вашей почтой,  категорически не рекомендуем указывать Вашу линчую почту.</p>',
      },
      {
        title: 'Как работает сервис при создании основной и фальшивой записки без паролей?',
        text: '<p>При создании основной и фальшивой записки без паролей при первом доступе откроется основная записка (после прочтения безвозвратно уничтожится), при втором доступе - фальшивая (после прочтения безвозвратно уничтожится). При последующих переходах по ссылке будет выдано сообщение «Запрашиваемой страницы не существует или записка уже была успешно прочитана ;)». Такая же страница открывается и при переходе на несуществующие адреса, что повышает уровень анонимности.</p>',
      },
      {
        title: 'Как работает сервис при создании основной и фальшивой записки с идентичными паролями?',
        text: '<p>При установке идентичных паролей на основную и фальшивую записки - при первом открытии будет предоставлена основная записка (после прочтения безвозвратно уничтожится), при втором - фальшивая (после прочтения безвозвратно уничтожится). При последующих переходах по ссылке будет выдано сообщение «Запрашиваемой страницы не существует или записка уже была успешно прочитана ;)». Такая же страница открывается и при переходе на несуществующие адреса, что повышает уровень анонимности.</p>',
      },
      {
        title: 'Как работает сервис при создании основной и фальшивой записки с разными паролями?',
        text: '<p>При установке разных паролей на основную и фальшивую записки после первого прочтения любой безвозвратно удаляются обе, т. к. ссылка одна, и злоумышленник не должен Вас деаномизировать даже по косвенным признакам. При последующих переходах по ссылке будет выдано сообщение «Запрашиваемой страницы не существует или записка уже была успешно прочитана ;)». Такая же страница открывается и при переходе на несуществующие адреса, что повышает уровень анонимности.</p>',
      },
      {
        title: 'Ведет ли сервис логи, собирает ли метрику и статистику о пользователях?',
        text: '<p>Мы не собираем никакие логи, не ведем сбор метрик, статистик о пользователях, не имеем доступ к пользовательской информации, привносим децентрализацию в каждый процесс. В дополнение к множественному шифрованию при удалении данных мы семикратно стохастически перезаписываем данные на информационном носителе нулями и единицами,  нивелируя риски при краже нашего оборудования и даже нахождении злоумышленника со стороны датацентра.</p> <p>Наши сервисы сохраняют Вашу анонимность и обеспечивают максимально возможную безопасность Ваших данных.</p>',
      },
      {
        title:
          'В случае физического доступа к Вашим серверам или их кражи - останутся ли мои данные конфиденциальными?',
        text: '<p>Да, Ваши данные останутся конфиденциальными.</p> <p>Все сервисы реализуются с соблюдением лучших практик DevSecOps.  Множественное шифрование (в том числе сквозное), инкапсуляция трафика в TOR и I2P, его маскировка, каскадирование с прокси-серверами и виртуальными частными сетями, а также инновационные методы кибербезопасности позволяют обеспечить максимальный уровень защиты Ваших данных.</p> <p>Мы не собираем никакие логи, не ведем сбор метрик, статистик о пользователях, не имеем доступ к пользовательской информации, привносим децентрализацию в каждый процесс. В дополнение к множественному шифрованию при удалении данных мы семикратно стохастически перезаписываем данные на информационном носителе нулями и единицами,  нивелируя риски при краже нашего оборудования и даже нахождении злоумышленника со стороны датацентра.</p> <p>Наши сервисы сохраняют Вашу анонимность и обеспечивают максимально возможную безопасность Ваших данных.</p>',
      },
    ],
  },
}
