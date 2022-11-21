import { onBeforeUnmount, onMounted } from 'vue'

export function useEscape(action: (evt: KeyboardEvent) => unknown) {
  const onEscape = (evt: KeyboardEvent) => {
    if (evt.key === 'Escape') {
      action(evt)
    }
  }
  onMounted(() => addEventListener('keydown', onEscape))
  onBeforeUnmount(() => addEventListener('keydown', onEscape))
}
