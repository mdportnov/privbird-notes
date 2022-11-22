<script setup lang="ts">
import { ILocale } from '@/models/i18n/locale'
import { useThemeStore } from '@/stores/theme'
import { useMinWidth } from '@/utils/mediaQuery'
import { useMenu } from '@/utils/menu'
import { useI18n } from 'vue-i18n'
import { RouterLink } from 'vue-router'
import ABtn from '../ABtn.vue'
import ITheme from '../icons/ITheme.vue'

const emit = defineEmits<{
  (e: 'close'): void
}>()

const links = useMenu()

const i18n = useI18n()
const themeStore = useThemeStore()

const toggleLocale = () => {
  i18n.locale.value = i18n.locale.value === ILocale.EN ? ILocale.RU : ILocale.EN
}

const isDesktop = useMinWidth('md')
</script>

<template>
  <div class="a-menu">
    <nav class="a-menu__nav">
      <component
        v-for="l of links"
        :key="l.label"
        :is="l.to ? RouterLink : 'a'"
        :to="l.to"
        @click="l.to && emit('close')"
        class="a-menu__nav__link"
        :class="{ 'a-menu__nav__link--in-develop': !l.to, 'a-menu__nav__link--desktop': isDesktop }"
      >
        <component :is="l.icon" />
        <span class="text" :develop-label="$t('menu.develop')">{{ $t(`menu.${l.label}`) }}</span>
      </component>
    </nav>
    <div v-if="!isDesktop" class="a-menu__actions">
      <a-btn @click="themeStore.toggle" square gradient><i-theme /></a-btn>
      <a-btn @click="toggleLocale" square gradient class="a-menu__actions__locale">{{ $i18n.locale }}</a-btn>
    </div>
  </div>
</template>

<style lang="scss">
.a-menu {
  width: 325px;
  border-radius: var(--border-radius-lg);
  background-color: var(--color-background);
  box-shadow: 0 0 4px 4px var(--color-shadow);
  transition: background-color $transition-theme, box-shadow $transition-theme;
  overflow: hidden;

  &__nav {
    display: flex;
    flex-direction: column;
    font-size: 2rem;

    &__link {
      text-decoration: none;
      display: grid;
      grid-template-columns: 3rem 1fr;
      align-items: center;
      padding: var(--gap-sm) var(--gap-lg);
      border-bottom: 2px solid var(--color-accent);
      cursor: pointer;
      transition: background-color $transition;

      .text {
        position: relative;
        font-size: 0.7em;
      }

      &--desktop {
        &:last-child {
          border-bottom: none;
        }
      }

      &--in-develop {
        cursor: not-allowed;

        .text::after {
          background-color: var(--color-background-mute);
          content: attr(develop-label);
          position: absolute;
          top: 0;
          right: 0;
          bottom: 0;
          left: 0;
          opacity: 0;
          transition: opacity $transition;
        }
      }

      &:focus-visible,
      &:hover {
        background-color: var(--color-background-mute);

        &.a-menu__nav__link--in-develop {
          .text::after {
            opacity: 1;
          }
        }
      }
    }
  }

  &__actions {
    padding: var(--gap-md);
    display: flex;
    justify-content: space-evenly;

    &__locale {
      text-transform: capitalize;
    }
  }
}
</style>
