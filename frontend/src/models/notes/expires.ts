export type EExpires = typeof EExpires.values[number]

export namespace EExpires {
  export const values = ['YEAR', 'DAY', 'WEEK', 'MONTH'] as const

  export function name(expires: EExpires) {
    return {
      'DAY': 'dayRadio',
      'WEEK': 'weekRadio',
      'MONTH': 'monthRadio',
      'YEAR': 'yearRadio',
    }[expires]
  }
}
