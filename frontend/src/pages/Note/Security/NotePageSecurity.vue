<script setup lang="ts">
import { useRoute } from 'vue-router'
import { ElForm } from 'element-plus'
import AInput from '../../../components/form/AInput.vue'
import AFormCaption from '../../../components/form/AFormCaption.vue'
import ABtn from '../../../components/ABtn.vue'
import { useNoteStore } from '@/stores/note'
import { useForm } from 'vee-validate'
import type { INoteData } from '@/models/notes/data'
import { INoteForm } from '@/models/notes/form'
import AMessageModal from '../../../components/message/AMessageModal.vue'
import { ref } from 'vue'

const route = useRoute()
const slug = route.params.slug as string

const store = useNoteStore()

const { handleSubmit } = useForm<INoteData.Password>({
  validationSchema: INoteForm.passValidation(),
})

const error = ref('')
const showError = ref(false)

const onSubmit = handleSubmit(async (form) => {
  const res = await store.passFetch(slug, form)
  if (res.error?.statusCode === 403) {
    error.value = res.error.message
    showError.value = true
  }
})
</script>

<template>
  <el-form @submit.prevent="onSubmit" class="note-page__security" autocomplete="off">
    <h1 class="note-page__security__title">{{ $t('note.title') }}</h1>
    <a-form-caption sub>{{ $t('note.passwordInput') }}</a-form-caption>
    <a-input name="password" type="password" show-password autocomplete="off" />
    <p class="note-page__security__caution">{{ $t('note.passwordRead') }}</p>
    <a-btn :loading="store.note.state.isLoading()" gradient>{{ $t('note.passwordButton') }}</a-btn>
    <a-message-modal v-model:show="showError" type="negative">
      {{ error }}
    </a-message-modal>
  </el-form>
</template>

<style lang="scss" scoped>
.note-page__security {
  max-width: 500px;
  margin: 0 auto;

  &__title {
    text-align: center;
    font-size: 24px;
    font-weight: 500;
    margin-bottom: var(--gap-lg);
    white-space: pre-line;
  }

  .a-form-caption {
    font-size: 20px;
  }

  &__caution {
    text-align: center;
    margin: var(--gap-lg) 0 var(--gap-lg);
  }

  .a-btn {
    width: 100%;
  }

  @media screen and (min-width: $bp-md) {
    .a-btn {
      --size: 60px;
    }
  }

  @media screen and (max-width: $bp-sm-max) {
    &__title {
      font-size: 20px;
    }

    .a-form-caption {
      font-size: 18px;
    }
  }

  @media screen and (max-width: $bp-xs-max) {
    &__title {
      font-size: 18px;
      margin-bottom: var(--gap-md);
    }

    .a-form-caption {
      font-size: 16px;
    }

    &__caution {
      font-size: 14px;
      text-align: unset;
      margin: var(--gap-md) 0 var(--gap-md);
    }
  }
}
</style>
