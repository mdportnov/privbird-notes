export type ENetwork = typeof ENetwork.values[number]

export namespace ENetwork {
  export const values = ['HTTPS', 'TOR', 'I2P'] as const

  export function name(network: ENetwork) {
    return {
      HTTPS: 'HTTPS',
      TOR: '.onion (TOR network)',
      I2P: '.i2p (I2P network)',
    }[network]
  }
}
