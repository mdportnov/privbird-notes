export const noteCreatePageLocales = {
  en: {
    noteCreate: {
      advanced: 'Advanced settings',
      advancedTitle: 'Unread note lifetime:',
      advancedInfo: 'The unread note will automatically be deleted:',
      monthRadio: {
        title: 'After 1 month',
        text: 'Even if no one reads the post, it will be destroyed after 1 month',
      },
      weekRadio: {
        title: 'After 1 week',
        text: 'Even if no one reads the post, it will be destroyed after 1 week',
      },
      dayRadio: {
        title: 'After 24 hours',
        text: 'Even if no one reads the post, it will be destroyed after 24 hours',
      },
      yearRadio: {
        title: 'Default',
        text: 'The maximum lifetime of a note is 365 days',
      },
      passwordTitle: 'Password settings:',
      passwordInput: 'Password:',
      passwordConfirmInput: 'Confirm password:',
      passwordInputPlease: 'Please input password',
      passwordConfirmInputPlease: 'Please confirm password',
      fakeNote: 'Fake note:',
      fakeInfo:
        'When someone follows the link a second time, they will see a false note. After that, even it will be deleted',
      enterText: 'Enter text here...',
      afterDestruction: 'After destruction of the main note',
      tryingToWatch: 'After reading the fake note',
      emailTitle: 'E-mail:',
      emailPlaceholder: 'Enter E-mail here',
      emailValidator: "Oops. It doesn't look like an E-mail.",
      createNote: 'Create note',
      notification: 'Notifications:',
      error: 'There was an error.\nTry again or contact support!',
      success:
        'The note has been successfully created.\nThe note will be destroyed after reading it!\nDon’t forget to copy the link!',
      enableFakeNote: 'Enable fake note',
      passwordFakeNote: 'Set a password for a fake note',
      warning: 'WARNING!',
      warningText:
        'if you set different passwords for the fake note and the main ' +
        'note, both will be deleted after the first reading ' +
        'of either one! If identical passwords are set, the first time the ' +
        'main note is opened, the second time the fake note is opened',
      noteType: 'Note type:',
      passwordInfo: 'Send the link and password through different communication channels!',
      copyError: 'Something went wrong. Try again',
      copySuccess: 'Copied to clipboard!',
      createAnotherNote: 'Create another note',
    },
  },
  ru: {
    noteCreate: {
      advanced: 'Настройки',
      advancedTitle: 'Авто-удаление непрочитанной записки через:',
      advancedInfo: 'Непрочитанная записка будет автоматически удалена:',
      monthRadio: {
        title: 'После 1 месяца',
        text: 'Записка будет удалена через месяц, даже если ее никто не прочитал',
      },
      weekRadio: {
        title: 'После 1 недели',
        text: 'Записка будет удалена через неделю, даже если ее никто не прочитал',
      },
      dayRadio: {
        title: 'После 24 часов',
        text: 'Записка будет удалена через 24 часа, даже если ее никто не прочитал',
      },
      yearRadio: {
        title: 'По умолчанию',
        text: 'Максимальное время до удаления - 365 дней',
      },
      passwordTitle: 'Настройки пароля:',
      passwordInput: 'Пароль:',
      passwordConfirmInput: 'Подтвердите пароль:',
      passwordInputPlease: 'Введите пароль',
      passwordConfirmInputPlease: 'Подтвердите пароль',
      fakeNote: 'Фальшивая записка',
      fakeInfo: 'При открытии ссылки второй раз будет отображена фальшивая записка. Далее обе записки будут удалены',
      enterText: 'Введите текст...',
      afterDestruction: 'После удаления основной записки',
      tryingToWatch: 'После прочтения фальшивой записки',
      emailTitle: 'E-mail:',
      emailPlaceholder: 'Введите E-mail здесь',
      emailValidator: 'Упс. Это не похоже на E-mail',
      createNote: 'Создать записку',
      notification: 'Уведомления:',
      error: 'Произошла ошибка.\nПопробуйте еще раз или свяжитесь с поддержкой!',
      success: 'Записка успешна создана.\nЗаписка будет удалена после прочтения!\nНе забудьте скопировать ссылку!',
      enableFakeNote: 'Создать фальшивую записку',
      warning: 'ВНИМАНИЕ!',
      warningText:
        'При установке разных паролей на фальшивую и основную записку после первого прочтения любой удаляются обе! При установке идентичных паролей - при первом открытии будет предоставлена основная записка, при втором - фальшивая',
      noteType: 'Тип записки',
      passwordInfo: 'Рекомендуем отправлять ссылку и пароль по разным каналам связи',
      copyError: 'Что-то не так. Попробуйте еще раз',
      copySuccess: 'Скопировано в буфер обмена!',
      passwordFakeNote: 'Установить пароль для фальшивой записки',
      createAnotherNote: 'Создать ещё одну записку',
    },
  },
}
