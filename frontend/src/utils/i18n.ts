import type { ILocale } from '@/models/i18n/locale'
import { watch, type ComputedRef } from 'vue'
import { useI18n } from 'vue-i18n'

export function useI18nStorage(key = 'locale') {
  const i18n = useI18n()

  const locale = localStorage.getItem(key)
  if (locale) i18n.locale.value = locale

  watch(
    () => i18n.locale.value,
    (val) => localStorage.setItem(key, val),
  )
}

export function useLocale() {
  const i18n = useI18n()
  return i18n.locale as ComputedRef<ILocale>
}
