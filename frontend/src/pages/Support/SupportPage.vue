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
  initialValues: {
    feedback:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores distinctio, fugiat facere suscipit itaque quibusdam nulla praesentium non illo. Minima pariatur enim ab veritatis corrupti nihil, omnis aspernatur tempora. Dolorum maxime dolor ex omnis accusantium vero unde sequi ullam dolorem cumque laudantium expedita id dignissimos quae, enim recusandae porro optio et suscipit sed. Accusamus reiciendis, ut tempora debitis, asperiores eius nam magni vel, suscipit itaque molestias hic eligendi? Deserunt, molestiae minima? Voluptates esse quod accusamus corrupti hic officiis corporis qui iste praesentium aliquam cupiditate quisquam, repellendus sunt placeat dicta eaque? Rem, odio ipsam. Repudiandae aliquam quaerat porro nesciunt iste ad molestias in quas, impedit, repellat doloremque ullam pariatur. Deserunt eaque, mollitia quae incidunt placeat optio cumque, atque quidem aut tempora at accusamus corporis commodi dolor. Nemo numquam sequi odit beatae dolorum modi mollitia! Quis, necessitatibus mollitia? Expedita sed ea officia quidem cupiditate corrupti aspernatur omnis doloremque. Consequuntur architecto quibusdam animi asperiores magnam voluptatum amet, sequi provident reiciendis eaque in a minima corporis veritatis maiores! Ducimus velit ab eaque provident itaque laborum delectus eveniet deleniti suscipit quo voluptates, voluptas tempora voluptatibus earum minus eligendi quibusdam impedit repellat at atque ex possimus. Et quisquam obcaecati esse aliquam, soluta eaque ad quo recusandae ex omnis dolorem. Cupiditate mollitia, ea harum eum doloremque nisi sequi, sunt fugiat maxime dolore architecto fuga sit, distinctio dolor obcaecati sint ratione amet nihil facilis corrupti accusamus iusto quae tempore et. Totam officiis, sequi voluptatum alias explicabo nihil nesciunt similique! Officiis rem et illum itaque amet consequatur voluptates, sint rerum veritatis debitis deleniti! Similique aliquam autem qui pariatur obcaecati, reiciendis quos quae illum rem saepe atque officiis praesentium earum ex consectetur? Est corporis atque ad quisquam vero sapiente beatae modi ipsa consequuntur porro libero nisi minima laborum, itaque nemo! Perspiciatis recusandae iste sint aspernatur fuga dignissimos, nesciunt maiores facere eveniet perferendis ex quibusdam earum necessitatibus voluptate odio culpa sequi dolorum voluptatum quas blanditiis. Laborum veniam, cumque nisi, architecto obcaecati iste soluta ratione quisquam saepe doloremque magni voluptatem minus nam asperiores? Quos, in odit distinctio inventore eum, ratione omnis adipisci ipsam qui molestiae repudiandae hic. Tempore eveniet laboriosam earum reprehenderit vero? Vitae ipsa similique voluptas unde dolor, saepe nulla? Amet, praesentium nobis, quibusdam quae rem molestias voluptatum aliquam eveniet fuga repellat nesciunt, tempora molestiae architecto sapiente non? Accusamus dolore tempora eum iure, laudantium officia deserunt, omnis fugiat consequatur pariatur eveniet labore officiis. Quo nobis, ducimus officiis quia itaque assumenda numquam!',
    email: '',
  },
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
