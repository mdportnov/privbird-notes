import type { ISimpleState} from '@/utils/states/state';
import { useState, type IState } from '@/utils/states/state'

export interface ISingleState<T> {
  data: Nullable<T>
  state: IState
}

export function useSingleState<T>(defaultValue?: ISimpleState): ISingleState<T> {
  return {
    data: null,
    state: useState(defaultValue),
  }
}
