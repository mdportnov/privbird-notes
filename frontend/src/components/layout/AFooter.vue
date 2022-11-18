<script setup lang="ts">
import { useFooter } from '@/utils/menu'
import { ref } from 'vue'
import SupportPage from '../../pages/Support/SupportPage.vue'

const links = useFooter()

const showSupport = ref(false)
</script>

<template>
  <footer class="a-footer">
    <span class="a-footer__item">Copyright © {{ new Date().getFullYear() }} Privbird</span>
    <div class="a-footer__item" v-for="l of links" :key="l.label">
      <router-link :to="l.to" class="router-link">
        {{ $t(`footer.${l.label}`) }}
      </router-link>
    </div>
    <div class="a-footer__item">
      <button @click="showSupport = true">{{ $t('footer.support') }}</button>
    </div>
  </footer>
  <support-page v-model:show="showSupport" />
</template>

<style lang="scss" scoped>
.a-footer {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-items: center;
  gap: var(--gap-xs) var(--gap-md);
  margin-top: var(--gap-lg);
  padding-bottom: var(--gap-lg);

  &__item {
    font-size: 18px;
    font-weight: 300;
    text-align: center;

    .router-link {
      text-decoration: none;
    }

    @media screen and (max-width: $bp-sm-max) and (min-width: 380px) {
      &:first-child {
        flex-basis: 100%;
      }

      &:nth-child(3) {
        flex-basis: calc(20% - 2 / 3 * var(--gap-md));
      }

      &:nth-child(2),
      &:nth-child(4) {
        flex-basis: calc(40% - 2 / 3 * var(--gap-md));
      }
    }

    @media screen and (max-width: $bp-xs-max) {
      font-size: 16px;
    }
  }
}
</style>
