import type { IResourceError } from './error'

export type IResource<T = unknown> =
  | {
      data: T
      error?: undefined
    }
  | {
      data?: undefined
      error: IResourceError
    }
