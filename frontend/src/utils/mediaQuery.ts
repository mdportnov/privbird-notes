import { onBeforeUnmount, onMounted, ref } from 'vue'
import bp from '@/css/breakpoints.module.scss'

export function useMediaQuery(query: string) {
  if (!/\(.*\)/.test(query)) query = `(${query})`

  const result = ref(true)
  const onQueryChange = (evt: MediaQueryListEvent) => (result.value = evt.matches)

  onMounted(() => {
    const queryList = window.matchMedia(query)
    result.value = queryList.matches

    queryList.addEventListener('change', onQueryChange)
    onBeforeUnmount(() => queryList.removeEventListener('change', onQueryChange))
  })

  return result
}

type EBreakpoints = keyof typeof bp

export function useMaxWidth(breakpoint: EBreakpoints) {
  return useMediaQuery(`max-width: ${bp[breakpoint]}`)
}

export function useMinWidth(breakpoint: EBreakpoints) {
  return useMediaQuery(`min-width: ${bp[breakpoint]}`)
}
