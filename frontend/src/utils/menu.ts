import type { Component } from 'vue'
import IFileSharing from '@/components/icons/menu/IFileSharing.vue'
import II2PMirror from '@/components/icons/menu/II2PMirror.vue'
import INotes from '@/components/icons/menu/INotes.vue'
import IOneTimeMail from '@/components/icons/menu/IOneTimeMail.vue'
import ITorMirror from '@/components/icons/menu/ITorMirror.vue'

interface IMenuItem {
  to?: string
  icon: Component
  label: string
}

export function useMenu(): IMenuItem[] {
  return [
    {
      to: '/notes',
      label: 'notes',
      icon: INotes,
    },
    {
      label: 'files',
      icon: IFileSharing,
    },
    {
      label: 'mail',
      icon: IOneTimeMail,
    },
    {
      label: 'i2p',
      icon: II2PMirror,
    },
    {
      label: 'tor',
      icon: ITorMirror,
    },
  ]
}

interface IFooterItem {
  label: string
  to: string
}

export function useFooter(): IFooterItem[] {
  return [
    {
      label: 'home',
      to: '/',
    },
    {
      label: 'about',
      to: '/about',
    },
    {
      label: 'privacy',
      to: '/privacy',
    },
    {
      label: 'faq',
      to: '/faq',
    },
  ]
}
