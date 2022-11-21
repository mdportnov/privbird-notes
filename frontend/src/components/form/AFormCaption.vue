<script setup lang="ts">
defineProps<{
  sub?: boolean
  required?: boolean
}>()
</script>

<template>
  <component
    :is="sub ? 'h2' : 'h1'"
    class="a-form-caption"
    :class="{
      'a-form-caption--sub': sub,
      'a-form-caption--required': required,
    }"
  >
    <slot />
  </component>
</template>

<style lang="scss" scoped>
.a-form-caption {
  font-weight: 600;
  font-size: 20px;
  line-height: 1.4;
  margin-bottom: 0.5em;

  @media screen and (max-width: $bp-sm-max) {
    font-size: 18px;
  }

  &--sub {
    font-weight: 400;
    font-size: 16px;

    @media screen and (max-width: $bp-sm-max) {
      font-size: 14px;
    }
  }

  &--required {
    &::after {
      content: ' *';
      color: var(--color-error);
      transition: color $transition-theme;
    }
  }
}
</style>
