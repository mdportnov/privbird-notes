<script setup lang="ts">
import IClose from '../icons/IClose.vue'

export interface AMessageProps {
  type: 'positive' | 'negative'
}

defineProps<AMessageProps>()

const emit = defineEmits<{
  (e: 'close'): void
}>()
</script>

<template>
  <div class="a-message" :class="`a-message--${type}`">
    <button type="button" class="close-btn" @click="emit('close')"><i-close /></button>
    <slot />
  </div>
</template>

<style lang="scss" scoped>
.a-message {
  position: relative;
  border-radius: var(--border-radius-lg);
  padding: var(--gap-lg);
  font-size: 24px;
  font-weight: 600;
  text-align: center;
  white-space: pre-line;
  transition: background-color $transition-theme, color $transition-theme;

  @media screen and (max-width: $bp-sm-max) {
    font-size: 20px;
    padding: 1.4em;
  }

  @media screen and (max-width: $bp-xs-max) {
    font-size: 16px;
  }

  .close-btn {
    position: absolute;
    font-size: 1rem;
    width: 1em;
    height: 1em;
    overflow: hidden;
    top: var(--gap-sm);
    right: var(--gap-sm);
  }

  &--negative {
    background-color: var(--color-negative);
    color: var(--color-text-negative);
  }

  &--positive {
    background-color: var(--color-positive);
    color: var(--color-text-positive);
  }

  &::before {
    content: '';
    z-index: -1;
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    border-radius: inherit;
    background-color: var(--color-background);
    transition: background-color $transition-theme;
  }
}
</style>
