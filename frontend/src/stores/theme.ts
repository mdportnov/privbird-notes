import { defineStore } from 'pinia'

const isDark = !!localStorage.getItem('dark')
if (isDark) document.body.classList.add('dark')

export const useThemeStore = defineStore('theme', {
  state: () => ({
    isDark,
  }),
  getters: {
    isLight: (state) => !state.isDark,
  },
  actions: {
    dark() {
      localStorage.setItem('dark', 'true')
      document.body.classList.add('dark')
      this.isDark = true
    },
    light() {
      localStorage.removeItem('dark')
      document.body.classList.remove('dark')
      this.isDark = false
    },
    toggle() {
      this.isDark ? this.light() : this.dark()
    },
  },
})
