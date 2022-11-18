import type { i18nConf } from '@/i18n/index'

export type ILocale = keyof typeof i18nConf['messages']
