import { errorLocales } from '@/i18n/error'
import { getLocale } from '@/utils/i18n'
import type { AxiosError } from 'axios'

export interface IResourceError {
  statusCode: Optional<number>
  message: string
  original: AxiosError<IAxiosError>
}

export namespace IResourceError {
  export function build(err: AxiosError<IAxiosError>): IResourceError {
    return {
      statusCode: err.response?.status,
      message:
        (err.response?.data as IApiError)?.message ||
        errorLocales[getLocale()]['EUNEXPECTED'],
      original: err,
    }
  }
}

export interface IApiError {
  message: string
  timestamp: string
}

export type IServerError = IApiError

export type IAxiosError = IApiError | IServerError
