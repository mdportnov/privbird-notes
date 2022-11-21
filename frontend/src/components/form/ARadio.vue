<script setup lang="ts">
import { ElRadio } from 'element-plus'

defineProps<{
  title: string
  text: string
}>()
</script>

<template>
  <el-radio label="default" class="a-radio">
    <h1 class="a-radio__title">{{ title }}</h1>
    <p class="a-radio__description">{{ text }}</p>
  </el-radio>
</template>

<style lang="scss" scoped>
.a-radio {
  height: auto;
  width: 100%;
  max-width: 100%;
  padding: var(--gap-md);
  gap: var(--gap-md);
  background-color: var(--color-background);
  transition: background-color $transition-theme;

  &.is-checked {
    background-color: var(--color-background-mute);
  }

  $indicator-size: 18px;
  --el-radio-input-width: #{$indicator-size};
  --el-radio-input-height: #{$indicator-size};

  &:deep(.el-radio__inner) {
    &::after {
      $size: calc(4 / 9 * $indicator-size);
      width: $size;
      height: $size;
    }
  }

  &:deep(.el-radio__label) {
    padding: 0;
  }

  @mixin text {
    line-height: 1.2;
    white-space: pre-wrap;
    transition: color $transition-theme;
  }

  &__title {
    @include text();
    font-size: 16px;
    font-weight: 700;
    color: var(--color-text);
    margin-bottom: var(--gap-xs);
    @media screen and (max-width: $bp-sm-max) {
      font-size: 14px;
      margin-bottom: var(--gap-xs);
    }
  }

  &__description {
    @include text();
    font-size: 14px;
    font-weight: 400;
    color: var(--color-text-input);
    transition: color $transition-theme;

    @media screen and (max-width: $bp-sm-max) {
      font-size: 12px;
    }
  }
}
</style>
