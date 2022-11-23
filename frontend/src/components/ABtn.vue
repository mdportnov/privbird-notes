<script setup lang="ts">
import { ElProgress } from 'element-plus'
import { RouterLink } from 'vue-router'

defineProps<{
  square?: boolean
  gradient?: boolean
  to?: string
  loading?: boolean
}>()
</script>

<template>
  <component
    :is="to ? RouterLink : 'button'"
    :to="to"
    class="a-btn"
    :class="{ 'a-btn--square': square, 'a-btn--gradient': gradient }"
  >
    <slot />
    <el-progress v-if="loading" :percentage="100" indeterminate :duration="1" />
  </component>
</template>

<style lang="scss">
.a-btn {
  --size: 80px;
  position: relative;
  overflow: hidden;
  border-radius: var(--border-radius-lg);
  border: 2px solid var(--color-stroke);
  color: var(--color-text);
  height: var(--size);
  padding: var(--gap-md);
  transition: transform $transition, box-shadow $transition, color $transition-theme, border-color $transition-theme;
  font-size: calc(0.3 * var(--size));
  display: flex;
  justify-content: center;
  align-items: center;
  text-decoration: none;

  @media screen and (max-width: $bp-sm-max) {
    --size: 60px;
  }

  @media screen and (max-width: $bp-xs-max) {
    --size: 40px;
    border-radius: var(--border-radius-md);
    font-size: calc(0.4 * var(--size));
  }

  &--square {
    width: var(--size);
    font-size: calc(0.375 * var(--size));

    .i-icon {
      font-size: calc(0.5 * var(--size));
    }
  }

  &--gradient {
    background: linear-gradient(to right, var(--color-gradient-primary));
    color: var(--color-background);
    border: none;
    box-shadow: var(--box-shadow);

    &.a-btn--square {
      background: linear-gradient(to bottom, var(--color-gradient-primary));
    }
  }

  &:focus-visible,
  &:hover {
    &:not(:active) {
      transform: translateY(calc(-1 * var(--size) / 20)) scale(1.02);

      &.a-btn--gradient {
        box-shadow: var(--box-shadow-active);
      }
    }
  }

  .el-progress {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;

    .el-progress-bar__outer {
      background-color: transparent;
    }

    .el-progress-bar__inner {
      transition: background-color $transition-theme;
      background-color: var(--color-background);
      opacity: 0.4;
    }

    .el-progress__text {
      display: none;
    }
  }
}
</style>
