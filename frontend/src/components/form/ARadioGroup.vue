<script setup lang="ts">
import { ElRadioGroup, ElFormItem } from 'element-plus'
import { useField, type ElProps } from '@/utils/form'
export interface AInputProps extends ElProps<typeof ElRadioGroup> {
  name: string
}
const props = defineProps<AInputProps>()
const { value, error, onBlur } = useField(props)
</script>

<template>
  <el-form-item :error="error">
    <el-radio-group
      v-bind="$attrs"
      v-model="value"
      @blur="onBlur"
      class="a-radio-group"
      :class="{ 'a-radio-group--error': !!error }"
    >
      <slot />
    </el-radio-group>
  </el-form-item>
</template>

<style lang="scss" scoped>
.el-form-item {
  .a-radio-group {
    width: 100%;
    border: 1px solid var(--el-input-border-color, var(--el-border-color));
    border-radius: var(--border-radius-md);
    overflow: hidden;
    flex-direction: column;
    align-items: flex-start;
    transition: border-color $transition-theme;

    &--error {
      border-color: var(--color-error);
      --el-color-primary: var(--color-error);
    }
  }
}
</style>
