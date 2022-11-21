<script setup lang="ts">
import { ElForm } from 'element-plus'
import AInput from '../../components/form/AInput.vue'
import ABtn from '../../components/ABtn.vue'
import AFormCaption from '../../components/form/AFormCaption.vue'
import { useEscape } from '@/utils/escape'
import { useForm } from 'vee-validate'
import { ref } from 'vue'
import AMessageModal from '../../components/message/AMessageModal.vue'
import { IFeedbackForm } from '@/models/feedback/form'
import { useFeedbackStore } from '@/stores/feedback'
import { IFeedbackData } from '@/models/feedback/data'

defineProps<{
  show: boolean
}>()

const emit = defineEmits<{
  (e: 'update:show', val: boolean): void
}>()

const close = () => emit('update:show', false)
useEscape(close)

const store = useFeedbackStore()

const { handleSubmit } = useForm<IFeedbackForm>({
  validationSchema: IFeedbackForm.validation(),
})

const message = ref('')
const showMessage = ref(false)

const onSubmit = handleSubmit(async (form) => {
  const res = await store.send(IFeedbackData.fromForm(form))
  if (res.error) {
    message.value = res.error.message
  } else {
    message.value = res.data.message
    close()
  }
  showMessage.value = true
})
</script>

<template>
  <teleport to="#app">
    <transition name="support-modal">
      <div v-if="show" class="support-page support-modal" @click.self="close">
        <div class="support-page__content">
          <div class="support-page__content__title">{{ $t('pages.support') }}</div>
          <button class="support-modal__close-btn" @click="close">×</button>
          <p class="support-page__content__description">{{ $t('support.description') }}</p>
          <el-form @submit.prevent="onSubmit" class="support-page__content__form" autocomplete="off">
            <a-form-caption sub>{{ $t('support.describe') }}</a-form-caption>
            <a-input
              name="feedback"
              :placeholder="$t('support.inputPlaceholder')"
              type="textarea"
              :autosize="{ minRows: 8 }"
              autocomplete="off"
            />
            <a-form-caption sub>{{ $t('support.emailTitle') }}</a-form-caption>
            <a-input name="email" :placeholder="$t('support.emailPlaceholder')" autocomplete="off" />
            <a-btn type="submit" :loading="store.res.state.isLoading()" gradient>{{ $t('support.send') }}</a-btn>
            <p class="support-page__content__description support-page__content__description--contact">
              {{ $t('support.qua') }}
              <a href="mailto:support@privbird.ru" class="link"><b>support@privbird.ru</b></a>
            </p>
          </el-form>
        </div>
      </div>
    </transition>
  </teleport>
  <a-message-modal v-model:show="showMessage" :type="store.res.state.isSuccess() ? 'positive' : 'negative'">
    {{ message }}
  </a-message-modal>
</template>

<style lang="scss" scoped>
$transition-modal: 0.3s;
.support-page {
  &__content {
    position: relative;
    width: 100%;
    max-width: 800px;
    max-height: calc(var(--doc-height) - 2 * var(--gap-lg));
    background-color: var(--color-background);
    border-radius: var(--border-radius-lg);
    padding: var(--gap-lg);
    overflow-y: auto;
    transition: background-color $transition-theme;

    scrollbar-width: none;
    &::-webkit-scrollbar {
      display: none;
    }

    &__title {
      font-family: var(--font-family-secondary);
      font-weight: 600;
      font-size: 48px;
      text-align: center;

      @media screen and (max-width: $bp-sm-max) {
        font-size: 32px;
      }

      @media screen and (max-width: $bp-xs-max) {
        font-size: 24px;
      }
    }

    .support-modal__close-btn {
      $size: 2rem;
      position: absolute;
      width: $size;
      height: $size;
      line-height: $size;
      font-size: 2 * $size;
      overflow: hidden;
      top: var(--gap-sm);
      right: var(--gap-sm);
    }

    &__description {
      font-weight: 400;
      font-size: 24px;
      text-align: center;
      max-width: 600px;
      margin: var(--gap-md) auto;

      @media screen and (max-width: $bp-sm-max) {
        font-size: 20px;
      }

      @media screen and (max-width: $bp-xs-max) {
        font-size: 18px;
        text-align: unset;
      }

      &--contact {
        margin-top: var(--gap-lg);
        margin-bottom: 0;

        .link {
          text-decoration: none;

          &:hover {
            text-decoration: underline;
          }
        }
      }
    }

    &__form {
      .a-form-caption {
        font-weight: 700;
        opacity: 0.6;
      }

      .a-btn {
        margin-top: var(--gap-lg);
        width: 100%;
        --size: 60px;

        @media screen and (max-width: $bp-xs-max) {
          --size: 40px;
        }
      }
    }
  }

  &.support-modal {
    position: fixed;
    z-index: 10;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-color: var(--color-overlay);
    display: flex;
    justify-content: center;
    align-items: center;
    padding: var(--gap-lg);

    @media screen and (max-width: $bp-sm-max) {
      padding: var(--gap-md);
    }

    &-enter-active,
    &-leave-active {
      transition: opacity $transition-modal;
    }

    &-enter-from,
    &-leave-to {
      opacity: 0;
    }
  }
}
</style>
