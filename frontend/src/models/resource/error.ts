import type { AxiosError } from 'axios'

export interface IResourceError {
  statusCode: Optional<number>
  message: {
    en: string
    ru: string
  }
  original: AxiosError<IAxiosError>
}

export namespace IResourceError {
  export function build(err: AxiosError<IAxiosError>): IResourceError {
    return {
      statusCode: err.response?.status,
      message:
        (err.response?.data as IApiError)?.message ||
        (err.message === 'ETIMEDOUT'
          ? {
              en: 'The server does not respond!',
              ru: 'Сервер не отвечает!',
            }
          : {
              en: 'Unexpected error!',
              ru: 'Неизвестная ошибка!',
            }),
      original: err,
    }
  }
}

export interface IApiError {
  message: {
    en: string
    ru: string
  }
  status_code: number
}

export type IServerError = IApiError

export type IAxiosError = IApiError | IServerError
