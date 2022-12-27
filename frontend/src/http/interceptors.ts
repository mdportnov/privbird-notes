import type { AxiosInstance } from 'axios'
import { getLocale } from '@/utils/i18n'

export function useLocaleInterceptor($api: AxiosInstance) {
  $api.interceptors.request.use((config) => {
    config.headers!['Accept-Language'] = getLocale()
    return config
  })
}
