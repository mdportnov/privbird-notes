import type { AxiosRequestConfig } from 'axios'
import axios from 'axios'
import { useLocaleInterceptor } from './interceptors'

export const baseURLPrivnote = import.meta.env.VITE_API_URL
export const baseURLFeedback = import.meta.env.VITE_API_URL

export const axiosConfig = {
  timeout: 5000,
  timeoutErrorMessage: 'ETIMEDOUT',
}

export const axiosConfigPrivnote: AxiosRequestConfig = {
  ...axiosConfig,
  baseURL: baseURLPrivnote,
}

export const axiosConfigFeedback: AxiosRequestConfig = {
  ...axiosConfig,
  baseURL: baseURLFeedback,
}

export const $apiPrivnote = axios.create(axiosConfig)
useLocaleInterceptor($apiPrivnote)

export const $apiFeedback = axios.create(axiosConfig)
useLocaleInterceptor($apiFeedback)
