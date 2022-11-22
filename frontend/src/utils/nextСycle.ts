export function nextСycle(callback?: (...args: unknown[]) => unknown) {
  return new Promise((resolve) =>
    setTimeout(() => {
      callback?.()
      resolve(null)
    }, 0),
  )
}
