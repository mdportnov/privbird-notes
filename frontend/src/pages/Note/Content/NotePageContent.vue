<script setup lang="ts">
import { useForm } from 'vee-validate'
import AInput from '../../../components/form/AInput.vue'

const props = defineProps<{
  note: Optional<string>
}>()

useForm({ initialValues: props })
</script>

<template>
  <main class="note-page__content">
    <h1 class="note-page__content__title">{{ $t('note.noteTitle') }}</h1>
    <a-input name="note" type="textarea" readonly autosize />
    <p class="note-page__content__caution">{{ $t('note.refreshInfo') }}</p>
  </main>
</template>

<style lang="scss" scoped>
.note-page__content {
  margin-bottom: 100px;

  &__title {
    font-weight: 500;
    margin-bottom: var(--gap-md);

    @media screen and (max-width: $bp-sm-max) {
      font-size: 24px;
    }

    @media screen and (max-width: $bp-xs-max) {
      font-size: 20px;
      margin-bottom: var(--gap-sm);
    }
  }

  &:deep(.a-input) {
    font-weight: 300;
    font-size: 24px;

    @media screen and (max-width: $bp-sm-max) {
      font-size: 20px;
    }

    @media screen and (max-width: $bp-xs-max) {
      font-size: 16px;
    }

    .el-textarea__inner {
      padding: 1em 1.5em;
      border-radius: var(--border-radius-lg);

      &::-webkit-resizer {
        background-position: 30% 30%;
      }
    }
  }

  @media screen and (max-width: $bp-xs-max) {
    &__caution {
      margin-top: -0.5rem;
    }
  }
}
</style>
