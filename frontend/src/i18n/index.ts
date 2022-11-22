import { createI18n } from 'vue-i18n'
import { aboutPageLocales } from './pages/about'
import { faqPageLocales } from './pages/faq'
import { homePageLocales } from './pages/home'
import { noteCreatePageLocales } from './pages/noteCreate'
import { notePageLocales } from './pages/note'
import { validationLocales } from './validation'
import { supportPageLocales } from './pages/support'
import { privacyPageLocales } from './pages/privacy'
import { notFoundPageLocales } from './pages/notFound'
import { ILocale } from '@/models/i18n/locale'

export const i18nConf = {
  legacy: false,
  warnHtmlInMessage: 'off',
  locale: ILocale.EN,
  fallbackLocale: ILocale.RU,
  messages: {
    en: {
      pages: {
        notes: 'Notes',
        about: 'About',
        privacy: 'Privacy policy',
        faq: 'FAQ',
        support: 'Support',
      },
      menu: {
        notes: 'Notes',
        files: 'File sharing',
        mail: 'One-time Mail',
        tor: 'TOR mirror',
        i2p: 'I2P mirror',
        other: 'And other projects for your privacy',
        develop: 'In developing...',
      },
      footer: {
        home: 'Home',
        about: 'About',
        privacy: 'Privacy Policy',
        faq: 'FAQ',
        support: 'Support',
      },
      ...validationLocales.en,
      ...homePageLocales.en,
      ...aboutPageLocales.en,
      ...faqPageLocales.en,
      ...noteCreatePageLocales.en,
      ...notePageLocales.en,
      ...supportPageLocales.en,
      ...privacyPageLocales.en,
      ...notFoundPageLocales.en,
    },
    ru: {
      pages: {
        notes: 'Записки',
        about: 'О нас',
        privacy: 'Политика\nконфиденциальности',
        faq: 'FAQ',
        support: 'Поддержка',
      },
      menu: {
        notes: 'Записки',
        files: 'Обмен файлами',
        mail: 'Одноразовая почта',
        tor: 'TOR зеркало',
        i2p: 'I2P зеркало',
        other: 'И другие проекты для вашей приватности',
        develop: 'В разработке...',
      },
      footer: {
        home: 'Главная',
        about: 'О нас',
        privacy: 'Политика конфиденциальности',
        faq: 'FAQ',
        support: 'Поддержка',
      },
      ...validationLocales.ru,
      ...homePageLocales.ru,
      ...aboutPageLocales.ru,
      ...faqPageLocales.ru,
      ...noteCreatePageLocales.ru,
      ...notePageLocales.ru,
      ...supportPageLocales.ru,
      ...privacyPageLocales.ru,
      ...notFoundPageLocales.ru,
    },
  },
}

export const i18n = createI18n(i18nConf)
