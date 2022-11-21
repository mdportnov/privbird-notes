export type ISimpleState = 'unset' | 'loading' | 'success' | 'error'
export interface IState {
  readonly value: ISimpleState
  get(): ISimpleState
  loading(): void
  success(): void
  error(): void
  isLoading(): boolean
  isSuccess(): boolean
  isError(): boolean
}

export function useState(defaultValue: ISimpleState = 'unset'): IState {
  const state: Writable<IState> = {
    value: defaultValue,
    get() {
      return this.value
    },
    loading() {
      this.value = 'loading'
    },
    success() {
      this.value = 'success'
    },
    error() {
      this.value = 'error'
    },
    isLoading() {
      return this.value === 'loading'
    },
    isSuccess() {
      return this.value === 'success'
    },
    isError() {
      return this.value === 'error'
    },
  }

  return state
}
