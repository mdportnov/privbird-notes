export type EExpires = typeof EExpires.values[number]

export namespace EExpires {
  export const values = ['Expires.YEAR', 'Expires.DAY', 'Expires.WEEK', 'Expires.MONTH'] as const

  export function name(expires: EExpires) {
    return {
      'Expires.DAY': 'dayRadio',
      'Expires.WEEK': 'weekRadio',
      'Expires.MONTH': 'monthRadio',
      'Expires.YEAR': 'yearRadio',
    }[expires]
  }
}
