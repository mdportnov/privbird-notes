<script setup lang="ts">
import { ElForm, ElOption } from 'element-plus'
import { ref } from 'vue'
import ABtn from '../../components/ABtn.vue'
import AInput from '../../components/form/AInput.vue'
import AExpandBtn from '../../components/AExpandBtn.vue'
import AFormCaption from '../../components/form/AFormCaption.vue'
import ASelect from '../../components/form/ASelect.vue'
import ARadioGroup from '../../components/form/ARadioGroup.vue'
import ARadio from '../../components/form/ARadio.vue'
import ACheckbox from '../../components/form/ACheckbox.vue'
import { useRouter } from 'vue-router'
import AMessageModal from '../../components/message/AMessageModal.vue'
import { useForm } from 'vee-validate'
import { ENetwork } from '@/models/notes/network'
import { EExpires } from '@/models/notes/expires'
import { INoteForm } from '@/models/notes/form'
import { useNoteFormStore } from '@/stores/noteForm'
import { INoteData } from '@/models/notes/data'

const router = useRouter()

const store = useNoteFormStore()

const showSettings = ref(false)

const { values, handleSubmit } = useForm<INoteForm>({
  validationSchema: INoteForm.validation(),
  initialValues: {
    note: {
      content: '',
      password: '',
      repeatPassword: '',
      notification: false,
    },
    fake: {
      content: '',
      password: '',
      repeatPassword: '',
      notification: false,
    },
    options: {
      network: 'HTTPS',
      expires: 'Expires.YEAR',
      email: '',
    },
  },
})

const errorMessage = ref('')
const showErrorMessage = ref(false)

const onSubmit = handleSubmit(async (form) => {
  const res = await store.create(INoteData.fromForm(form))
  if (res.error) {
    errorMessage.value = res.error.message
    showErrorMessage.value = true
  } else router.replace('/notes/create/done')
})
</script>

<template>
  <el-form class="note-create-page" autocomplete="off" @submit="onSubmit">
    <a-input
      name="note.content"
      type="textarea"
      :placeholder="$t('noteCreate.enterText')"
      :autosize="{ minRows: 8 }"
      class="note"
    />
    <div class="actions">
      <div class="options" :class="{ expanded: showSettings }">
        <div class="options__header">
          <component :is="showSettings ? 'div' : 'label'" for="advanced-expand" class="options__header__title">
            {{ $t('noteCreate.advanced') }}
          </component>
          <a-expand-btn v-model:expand="showSettings" id="advanced-expand" class="options__header__expand-btn" />
        </div>
        <transition name="advanced">
          <div v-if="showSettings" class="advanced">
            <div>
              <a-form-caption required>{{ $t('noteCreate.noteType') }}</a-form-caption>
              <a-select name="options.network">
                <el-option v-for="t of ENetwork.values" :key="t" :label="ENetwork.name(t)" :value="t" />
              </a-select>
              <a-form-caption required>{{ $t('noteCreate.advancedTitle') }}</a-form-caption>
              <a-form-caption sub>{{ $t('noteCreate.advancedInfo') }}</a-form-caption>
              <a-radio-group name="options.expires">
                <a-radio
                  v-for="l of EExpires.values"
                  :key="l"
                  v-bind="$tm(`noteCreate.${EExpires.name(l)}`)"
                  :label="l"
                />
              </a-radio-group>
            </div>
            <div>
              <a-form-caption>{{ $t('noteCreate.passwordTitle') }}</a-form-caption>
              <a-form-caption sub>{{ $t('noteCreate.passwordInfo') }}</a-form-caption>
              <a-form-caption sub>{{ $t('noteCreate.passwordInput') }}</a-form-caption>
              <a-input
                name="note.password"
                type="password"
                :placeholder="$t('noteCreate.passwordInputPlease')"
                show-password
                autocomplete="off"
              />
              <a-form-caption sub>{{ $t('noteCreate.passwordConfirmInput') }}</a-form-caption>
              <a-input
                name="note.repeatPassword"
                type="password"
                :placeholder="$t('noteCreate.passwordConfirmInputPlease')"
                show-password
                autocomplete="off"
              />
              <a-form-caption>{{ $t('noteCreate.fakeNote') }}</a-form-caption>
              <a-checkbox name="fake.enable" :label="$t('noteCreate.enableFakeNote')" />
              <a-form-caption sub>{{ $t('noteCreate.fakeInfo') }}</a-form-caption>
              <template v-if="values.fake?.enable">
                <a-input
                  name="fake.content"
                  :placeholder="$t('noteCreate.enterText')"
                  type="textarea"
                  :autosize="{ minRows: 6, maxRows: 6 }"
                />
                <a-checkbox name="fake.enablePassword" :label="$t('noteCreate.passwordFakeNote')" />
                <a-form-caption sub>
                  <span class="warning"> {{ $t('noteCreate.warning') }}</span> {{ $t('noteCreate.warningText') }}
                </a-form-caption>
                <template v-if="values.fake?.enablePassword">
                  <a-form-caption sub>{{ $t('noteCreate.passwordInput') }}</a-form-caption>
                  <a-input
                    name="fake.password"
                    type="password"
                    :placeholder="$t('noteCreate.passwordInputPlease')"
                    show-password
                    autocomplete="off"
                  />
                  <a-form-caption sub>{{ $t('noteCreate.passwordConfirmInput') }}</a-form-caption>
                  <a-input
                    name="fake.repeatPassword"
                    type="password"
                    :placeholder="$t('noteCreate.passwordConfirmInputPlease')"
                    show-password
                    autocomplete="off"
                  />
                </template>
              </template>
            </div>
            <div>
              <a-form-caption>{{ $t('noteCreate.notification') }}</a-form-caption>
              <a-checkbox name="note.notification" :label="$t('noteCreate.afterDestruction')" />
              <a-checkbox v-if="values.fake?.enable" name="fake.notification" :label="$t('noteCreate.tryingToWatch')" />
              <a-form-caption>{{ $t('noteCreate.emailTitle') }}</a-form-caption>
              <a-input name="options.email" :placeholder="$t('noteCreate.emailPlaceholder')" autocomplete="off" />
            </div>
          </div>
        </transition>
      </div>
      <a-btn gradient type="submit" :loading="store.slug.state.isLoading()" class="submit-btn">
        {{ $t('noteCreate.createNote') }}
      </a-btn>
    </div>
  </el-form>
  <a-message-modal v-model:show="showErrorMessage" type="negative">
    {{ errorMessage }}
  </a-message-modal>
</template>

<style lang="scss" scoped>
$transition-advanced: 0.4s;
.note-create-page {
  margin-bottom: 100px;

  &:deep(.note) {
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
  .actions {
    margin-top: var(--gap-lg);
    display: flex;
    flex-wrap: wrap;
    gap: var(--gap-lg);

    @media screen and (max-width: $bp-sm-max) {
      margin-top: var(--gap-md);
      gap: var(--gap-md);
    }

    .options {
      --size: 80px;
      font-size: calc(0.3 * var(--size));
      border-radius: var(--border-radius-lg);
      border: 2px solid var(--color-stroke);
      color: var(--color-text);
      transition: color $transition-theme, border-color $transition-theme, width $transition-advanced;
      width: calc(50% - var(--gap-lg) / 2);
      overflow: hidden;

      @media screen and (max-width: $bp-sm-max) {
        width: 100%;
        --size: 60px;
      }

      @media screen and (max-width: $bp-xs-max) {
        --size: 40px;
        border-radius: var(--border-radius-md);
        font-size: calc(0.45 * var(--size));
      }

      &__header {
        position: relative;
        display: flex;
        align-items: center;

        &__title {
          width: 100%;
          height: var(--size);
          line-height: var(--size);
          padding: 0 2em;
          text-align: center;
          cursor: pointer;
          vertical-align: baseline;
        }

        &__expand-btn {
          position: absolute;
          right: 1em;
        }
      }

      &.expanded {
        width: 100%;

        .options__header {
          &__title {
            font-weight: 600;
            cursor: unset;
          }
        }
      }

      .advanced {
        padding: var(--gap-md);
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: var(--gap-lg);

        @media screen and (max-width: 1030px) {
          display: block;
        }

        &-enter-active,
        &-leave-active {
          max-height: min(1050px, 100vh);
          transition: max-height $transition-advanced, padding $transition-advanced;

          @media screen and (max-width: $bp-md-max) {
            max-height: min(1100px, 100vh);
          }

          @media screen and (max-width: 1030px) {
            max-height: min(1700px, 100vh);
          }

          @media screen and (max-width: $bp-sm-max) {
            max-height: min(1650px, 100vh);
          }

          @media screen and (max-width: $bp-xs-max) {
            max-height: min(1820px, 100vh);
          }

          @media screen and (max-width: 330px) {
            max-height: 100vh;
          }
        }

        &-enter-from,
        &-leave-to {
          opacity: 0;
          max-height: 0;
          padding: 0;
        }

        .warning {
          color: var(--color-error);
        }
      }
    }

    .submit-btn {
      flex-grow: 1;
    }
  }
}
</style>
