<script setup lang="ts">
import { ElCheckbox, ElFormItem } from 'element-plus'
import { useField, type ElProps } from '@/utils/form'
export interface AInputProps extends ElProps<typeof ElCheckbox> {
  name: string
  label: string
}
const props = defineProps<AInputProps>()
const { value, error, onBlur } = useField(props)
</script>

<template>
  <el-form-item :error="error">
    <el-checkbox v-bind="$attrs" v-model="value" :label="label" @blur="onBlur" class="a-checkbox" />
  </el-form-item>
</template>

<style lang="scss">
.el-form-item {
  .a-checkbox {
    .el-checkbox__input {
      border-radius: 2px;
      transition: box-shadow $transition-theme;

      .el-checkbox__inner {
        $size: 18px;
        width: $size;
        height: $size;
        --el-checkbox-checked-icon-color: var(--color-background);

        &::after {
          height: 0.5 * $size;
          width: 0.3 * $size;
          left: 0.3 * $size;
          top: 0.1 * $size;
        }
      }
    }

    .el-checkbox__label {
      font-size: 16px;
      font-weight: 400;
      color: var(--color-text);
      transition: color $transition-theme;
      max-width: 100%;
      white-space: pre-wrap;

      @media screen and (max-width: $bp-sm-max) {
        font-size: 14px;
      }
    }
  }

  &.is-error {
    .el-checkbox__input {
      box-shadow: 0 0 2px 2px var(--color-error) !important;
    }
  }
}
</style>
