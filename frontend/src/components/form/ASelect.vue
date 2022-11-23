<script setup lang="ts">
import { ElSelect, ElFormItem } from 'element-plus'
import { useField, type ElProps } from '@/utils/form'
import { useThemeStore } from '@/stores/theme'
export interface AInputProps extends ElProps<typeof ElSelect> {
  name: string
}
const props = defineProps<AInputProps>()
const { value, error, onBlur } = useField(props)

const themeStore = useThemeStore()
</script>

<template>
  <el-form-item :error="error">
    <el-select
      v-bind="$attrs"
      v-model="value"
      @blur="onBlur"
      class="a-select"
      :class="{ 'a-select--dark': themeStore.isDark }"
    >
      <slot />
    </el-select>
  </el-form-item>
</template>

<style lang="scss">
.el-form-item {
  .a-select {
    .el-input__wrapper {
      padding: 12px 16px;
      border-radius: var(--border-radius-md);
      box-shadow: 0 0 0 2px var(--el-input-border-color, var(--el-border-color)) inset;
      background-color: var(--color-background);
      transition: background-color $transition-theme;

      .el-input__inner {
        font-size: 1rem;
        font-weight: 400;
        color: var(--color-text);
        transition: color $transition-theme, opacity $transition-theme;
      }
    }

    &:not(&--dark) {
      .el-input__wrapper {
        .el-input__inner {
          opacity: 0.8;
        }
      }
    }

    .el-input {
      &.is-focus {
        .el-input__wrapper {
          box-shadow: 0 0 0 2px var(--el-select-input-focus-border-color) inset !important;
        }
      }

      &.is-error {
        .el-input__wrapper {
          box-shadow: 0 0 0 2px var(--el-color-danger) inset;
        }
      }
    }
  }
}
</style>
