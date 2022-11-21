export function useDocHeight() {
  const set = () => document.body.style.setProperty('--doc-height', window.innerHeight + 'px')
  window.addEventListener('resize', set, { passive: true })
  set()
}
