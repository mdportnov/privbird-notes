<script setup lang="ts">
import logo from '@/assets/logo.svg'
import { useThemeStore } from '@/stores/theme'
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { useRoute } from 'vue-router'
import ITheme from '../icons/ITheme.vue'
import IMenu from '../icons/IMenu.vue'
import ABtn from '../ABtn.vue'
import AMenu from './AMenu.vue'
import AContext from '../AContext.vue'
import { useMinWidth } from '@/utils/mediaQuery'
import { ILocale } from '@/models/i18n/locale'

const i18n = useI18n()
const route = useRoute()

const themeStore = useThemeStore()

const toggleLocale = () => {
  i18n.locale.value = i18n.locale.value === ILocale.EN ? ILocale.RU : ILocale.EN
}

const pageName = computed(() => (route.meta.label && i18n.t(`pages.${route.meta.label}`)) as Optional<string>)
const pageNameSm = computed(() => pageName.value?.includes('\n'))

const isHome = computed(() => route.name === 'home')
const isDesktop = useMinWidth('md')
</script>

<template>
  <header class="a-navbar" :class="{ 'a-navbar--home': isHome }">
    <router-link to="/" class="a-navbar__logo">
      <img :src="logo" alt="logo" class="logo a-navbar__logo__image" />
      <div class="a-navbar__logo__text a-navbar__text">Privbird</div>
    </router-link>
    <div class="a-navbar__page-name a-navbar__text" :class="{ 'a-navbar__page-name--sm': pageNameSm }">
      {{ pageName }}
    </div>
    <a-context :position="{ y: 'bottom', x: 'right' }" class="a-navbar__actions">
      <template #main="{ swap }">
        <template v-if="isHome || isDesktop">
          <a-btn @click="themeStore.toggle" square gradient class="a-navbar__actions__theme"><i-theme /></a-btn>
          <a-btn @click="toggleLocale" square gradient class="a-navbar__actions__locale">{{ $i18n.locale }}</a-btn>
        </template>
        <a-btn v-if="!isHome" @click="swap" square gradient class="a-navbar__actions__theme"><i-menu /></a-btn>
      </template>
      <template #context="{ swap }">
        <a-menu @close="swap" />
      </template>
    </a-context>
  </header>
</template>

<style lang="scss">
.a-navbar {
  --navbar-height: 120px;
  --logo-text-offset: calc(var(--navbar-height) / 4);
  height: var(--navbar-height);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: var(--gap-sm);
  padding-top: var(--logo-text-offset);
  margin: var(--gap-md) 0 var(--gap-lg);

  &__text {
    font-family: var(--font-family-secondary);
    font-weight: 600;
    font-size: calc(0.4 * var(--navbar-height));
  }

  &__page-name {
    text-align: center;

    &--sm {
      font-size: calc(0.3 * var(--navbar-height));
      white-space: pre-line;

      @media screen and (max-width: 400px) {
        font-size: calc(0.2 * var(--navbar-height));
      }
    }
  }

  &__logo {
    display: flex;
    align-items: center;
    margin-top: calc(-1 * var(--logo-text-offset));
    text-decoration: none;

    &__image {
      &.logo {
        aspect-ratio: 112 / 121;

        height: var(--navbar-height);
        width: calc(var(--navbar-height) * 112 / 121);
      }
    }

    &__text {
      margin-top: var(--logo-text-offset);
    }
  }

  &__actions {
    position: relative;
    display: flex;
    gap: var(--gap-md);

    &__locale {
      text-transform: capitalize;
      font-weight: 600;
    }

    .a-menu {
      position: absolute;
      bottom: 0;
      right: 0;
      transform: translateY(calc(100% + var(--gap-md)));
      z-index: 1;
    }
  }

  @media screen and (max-width: 1030px) {
    --navbar-height: 80px;

    &__actions {
      gap: var(--gap-sm);
    }
  }

  @media screen and (max-width: $bp-xs-max) {
    --navbar-height: 60px;
  }
}
</style>
