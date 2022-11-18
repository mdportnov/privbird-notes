<script setup lang="ts">
import '@/css/index.scss'
import ANavbar from './components/layout/ANavbar.vue'
import AFooter from './components/layout/AFooter.vue'
import ASpacer from './components/ASpacer.vue'
import { useDocHeight } from './utils/docHeight'
import { useI18nStorage } from './utils/i18n'
import { useValidationLocale } from './utils/form'
import { useScrollOnRoute } from './utils/router'

useDocHeight()
useI18nStorage()
useValidationLocale()
useScrollOnRoute()
</script>

<template>
  <div class="layout layout--main">
    <a-navbar />
    <router-view />
    <a-spacer />
    <a-footer />
  </div>
</template>

<style lang="scss" scoped>
.layout--main {
  max-width: $bp-lg;
  min-height: var(--doc-height);
  height: 0;
  margin: 0 auto;
  padding: 0 calc(var(--gap-lg) + #{$home-offset});
  display: flex;
  flex-direction: column;

  @media screen and (max-width: #{$home-breakpoint}) {
    padding: 0 var(--gap-lg);
  }

  @media screen and (max-width: $bp-sm-max) {
    padding: 0 var(--gap-md);
  }
}
</style>
