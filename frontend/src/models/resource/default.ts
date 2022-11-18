import type { IApiMessage } from './message'

export interface IRes<T = unknown> {
  data: T
  message: IApiMessage
}

export namespace IRes {
  export function isRes<T>(val: T | IRes<T>): val is IRes<T> {
    return val !== null && typeof val === 'object' && 'data' in val && 'message' in val
  }
}
