import type { AxiosRequestConfig } from 'axios'
import axios from 'axios'
import { useLocaleInterceptor } from './interceptors'

export const baseURLPrivnote = import.meta.env.VITE_PRIVNOTE_API_URL
export const baseURLFeedback = import.meta.env.VITE_FEEDBACK_API_URL

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

export const $apiPrivnote = axios.create(axiosConfigPrivnote)
useLocaleInterceptor($apiPrivnote)

export const $apiFeedback = axios.create(axiosConfigFeedback)
useLocaleInterceptor($apiFeedback)
