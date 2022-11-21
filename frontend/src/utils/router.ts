import { useRouter } from 'vue-router'
import { nextTick } from './nextTick'

export function useScrollOnRoute() {
  useRouter().afterEach(async () => {
    await nextTick()
    window.scrollTo({
      top: 0,
      behavior: 'smooth',
    })
  })
}
