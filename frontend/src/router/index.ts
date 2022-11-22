import { createRouter, createWebHistory, RouterView } from 'vue-router'

const HomePage = () => import('@/pages/Home/HomePage.vue')
const NoteCreatePage = () => import('@/pages/NoteCreate/NoteCreatePage.vue')
const NoteCreateDonePage = () => import('@/pages/NoteCreate/NoteCreateDonePage.vue')
const NotePage = () => import('@/pages/Note/NotePage.vue')
const AboutPage = () => import('@/pages/About/AboutPage.vue')
const FAQPage = () => import('@/pages/FAQ/FAQPage.vue')
const PrivacyPage = () => import('@/pages/Privacy/PrivacyPage.vue')
const NotFoundPage = () => import('@/pages/NotFound/NotFoundPage.vue')

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
