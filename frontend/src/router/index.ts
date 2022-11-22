import { createRouter, createWebHistory, RouterView } from 'vue-router'

import HomePage from '@/pages/Home/HomePage.vue'
import NoteCreatePage from '@/pages/NoteCreate/NoteCreatePage.vue'
import NoteCreateDonePage from '@/pages/NoteCreate/NoteCreateDonePage.vue'
import NotePage from '@/pages/Note/NotePage.vue'
import AboutPage from '@/pages/About/AboutPage.vue'
import FAQPage from '@/pages/FAQ/FAQPage.vue'
import PrivacyPage from '@/pages/Privacy/PrivacyPage.vue'
import NotFoundPage from '@/pages/NotFound/NotFoundPage.vue'

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior: () => ({ top: 0, behavior: 'smooth' }),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage,
    },
    {
      path: '/notes',
      component: RouterView,
      redirect: '/notes/create',
      children: [
        {
          path: 'create',
          component: RouterView,
          children: [
            {
              path: '',
              name: 'note-create',
              component: NoteCreatePage,
            },
            {
              path: 'done',
              name: 'note-create-done',
              component: NoteCreateDonePage,
            },
          ],
        },
        {
          path: ':slug',
          name: 'note',
          component: NotePage,
        },
        {
          path: ':slug/:key',
          name: 'note-secret',
          component: NotePage,
        },
      ],
      meta: {
        label: 'notes',
      },
    },
    {
      path: '/about',
      name: 'about',
      component: AboutPage,
      meta: {
        label: 'about',
      },
    },
    {
      path: '/privacy',
      name: 'privacy',
      component: PrivacyPage,
      meta: {
        label: 'privacy',
      },
    },
    {
      path: '/faq',
      name: 'faq',
      component: FAQPage,
      meta: {
        label: 'faq',
      },
    },
    {
      path: '/not-found',
      name: 'not-found',
      component: NotFoundPage,
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/not-found',
    },
  ],
})
