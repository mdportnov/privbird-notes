<script setup lang="ts">
import { ElInput, ElFormItem } from 'element-plus'
import { useField, type ElProps } from '@/utils/form'
export interface AInputProps extends ElProps<typeof ElInput> {
  name: string
}
const props = defineProps<AInputProps>()
const { value, error, onBlur } = useField(props)
</script>

<template>
  <el-form-item :error="error">
    <el-input v-bind="$attrs" v-model="value" @blur="onBlur" class="a-input" />
  </el-form-item>
</template>

<style lang="scss">
.el-form-item {
  @mixin input-inner {
    padding: 12px 16px;
    border-radius: var(--border-radius-md);
    background-color: var(--color-background);
    transition: background-color $transition-theme;
  }

  @mixin input {
    font-weight: 600;
    color: var(--color-text-input);
    transition: color $transition-theme;

    &::placeholder {
      font-weight: 600;
    }
  }

  .a-input {
    .el-input__wrapper {
      @include input-inner();

      .el-input__inner {
        @include input();
      }
    }

    .el-textarea__inner {
      @include input-inner();
      @include input();
      transition: background-color $transition-theme, color $transition-theme;

      &::-webkit-resizer {
        background-image: url("data:image/svg+xml,%3Csvg width='7' height='7' viewBox='0 0 7 7' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M6.81676 5.74776C6.86038 6.35533 6.35528 6.86043 5.74771 6.81681L1.16585 6.48785C0.311301 6.42649 -0.0754549 5.38912 0.530361 4.78331L4.78326 0.530412C5.38907 -0.0754031 6.42644 0.311353 6.4878 1.16591L6.81676 5.74776Z' fill='%23E0E2E7' /%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-position: 40%;
      }
    }
  }
}
</style>
