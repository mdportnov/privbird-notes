<script setup lang="ts">
import { useMenu } from '@/utils/menu'
import { RouterLink } from 'vue-router'
import ABtn from '../../components/ABtn.vue'
import IOtherProducts from '../../components/icons/menu/IOtherProducts.vue'

const links = useMenu()
</script>

<template>
  <div class="home-page">
    <div>
      <div class="slogan">{{ $t('home.slogan') }}</div>
      <div class="actions">
        <a-btn to="/notes" gradient>{{ $t('home.actions.start') }}</a-btn>
        <a-btn to="/faq">{{ $t('home.actions.info') }}</a-btn>
      </div>
    </div>
    <nav class="products">
      <component
        v-for="l of links"
        :key="l.label"
        :is="l.to ? RouterLink : 'a'"
        :to="l.to"
        class="products__link"
        :class="{ 'products__link--in-develop': !l.to }"
      >
        <component :is="l.icon" />
        <span class="text" :develop-label="$t('menu.develop')">{{ $t(`menu.${l.label}`) }}</span>
      </component>
      <span class="products__link">
        <i-other-products />
        <span class="text other">{{ $t('menu.other') }}</span>
      </span>
    </nav>
  </div>
</template>

<style lang="scss" scoped>
.home-page {
  display: flex;
  justify-content: space-between;

  .slogan {
    font-size: 75px;
    font-weight: 600;
    line-height: 2;
    white-space: pre-line;
    color: var(--color-cyan);
    background: linear-gradient(0, var(--color-gradient-primary));
    background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1em;

    @media screen and (max-width: $bp-sm-max) {
      font-size: 60px;
    }

    @media screen and (max-width: $bp-xs-max) {
      font-size: 36px;
    }
  }

  .actions {
    display: flex;
    gap: var(--gap-lg);
    .a-btn {
      flex: 1 1 0;
    }
  }

  .products {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--gap-lg);
    height: 100%;
    width: 100%;
    max-width: 485px;
    padding-top: 40px;

    @media screen and (max-width: $bp-xs-max) {
      max-width: 350px;
      font-size: 0.7em;
    }

    &__link {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: var(--gap-sm);
      text-decoration: none;

      &:deep(.i-icon) {
        $size: 8.75em;
        box-shadow: var(--box-shadow-mute);
        border-radius: var(--border-radius-lg);
        padding: calc(0.2 * $size);
        height: $size;
        width: $size;
        z-index: 1;
        transition: box-shadow $transition;
      }

      .text {
        position: relative;
        font-size: 1.5em;
        text-align: center;

        &.other {
          font-size: 1.2em;
        }
      }

      &--in-develop {
        cursor: not-allowed;

        .text::after {
          background-color: var(--color-background);
          content: attr(develop-label);
          position: absolute;
          top: 0;
          bottom: 0;
          left: 50%;
          transform: translateX(-50%);
          min-width: 100%;
          opacity: 0;
          transition: opacity $transition;
          white-space: nowrap;
        }
      }

      &:focus-visible,
      &:hover {
        &:deep(.i-icon) {
          box-shadow: var(--box-shadow-mute-active);
        }

        &.products__link--in-develop {
          .text::after {
            opacity: 1;
          }
        }
      }
    }
  }

  @media screen and (min-width: #{$home-breakpoint + 1px}) {
    margin-right: -$home-offset;
  }

  @media screen and (max-width: $home-breakpoint) {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 40px;
  }
}
</style>
