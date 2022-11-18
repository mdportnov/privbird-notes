export const nextTick = (callback?: (...args: unknown[]) => unknown) =>
  new Promise((resolve) =>
    setTimeout(() => {
      callback?.()
      resolve(null)
    }, 0),
  )
