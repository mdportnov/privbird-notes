import type { ILocale } from '@/models/i18n/locale'
import { watch, type ComputedRef } from 'vue'
import { useI18n } from 'vue-i18n'

const STORAGE_KEY = 'locale'

export function useI18nStorage() {
  const i18n = useI18n()

  const locale = localStorage.getItem(STORAGE_KEY)
  if (locale) i18n.locale.value = locale
  else localStorage.setItem(STORAGE_KEY, i18n.locale.value)

  watch(
    () => i18n.locale.value,
    (val) => {
      localStorage.setItem(STORAGE_KEY, val)
      document.documentElement.setAttribute('lang', val)
    },
  )
}

export function useLocale() {
  const i18n = useI18n()
  return i18n.locale as ComputedRef<ILocale>
}

export function getLocale() {
  return localStorage.getItem(STORAGE_KEY) as ILocale
}
