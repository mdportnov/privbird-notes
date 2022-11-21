import type { AxiosRequestConfig } from 'axios'
import axios from 'axios'
import { getLocale } from '@/utils/i18n'

export const baseURL = import.meta.env.VITE_API_URL

export const axiosConfig: AxiosRequestConfig = {
  withCredentials: true,
  baseURL,
  timeout: 5000,
  timeoutErrorMessage: 'ETIMEDOUT',
}

export const $api = axios.create(axiosConfig)

$api.interceptors.request.use((config) => {
  config.headers!['Accept-Language'] = getLocale()
  return config
})
