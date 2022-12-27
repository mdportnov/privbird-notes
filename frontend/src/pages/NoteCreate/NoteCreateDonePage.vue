<script setup lang="ts">
import { computed, onBeforeMount, ref } from 'vue'
import AClosableMessage from '../../components/message/AClosableMessage.vue'
import ABtn from '../../components/ABtn.vue'
import IClipboard from '../../components/icons/IClipboard.vue'
import AMessageModal from '../../components/message/AMessageModal.vue'
import { useNoteFormStore } from '@/stores/noteForm'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useNoteFormStore()
onBeforeMount(() => !store.url.data && router.replace('/'))

const url = computed(() => store.url.data)
const message = computed(() => url.value?.message)

const showClipboardMesage = ref(false)
const showClipboardErrorMesage = ref(false)
const copyToClipboard = async () => {
  try {
    if (!url.value?.data.url) return
    await navigator.clipboard.writeText(url.value?.data.url)
    showClipboardMesage.value = true
  } catch (_) {
    showClipboardErrorMesage.value = true
  }
}
</script>

<template>
  <div class="note-create-done-page">
    <a-closable-message type="positive">{{ message }}</a-closable-message>
    <main class="content">
      <div class="actions">
        <div class="url">
          <span class="text">{{ url?.data.url }}</span>
        </div>
        <a-btn @click="copyToClipboard" square gradient><i-clipboard /></a-btn>
        <a-message-modal v-model:show="showClipboardMesage" type="positive" :timeout="3000">
          {{ $t('noteCreate.copySuccess') }}
        </a-message-modal>
        <a-message-modal v-model:show="showClipboardErrorMesage" type="negative" :timeout="3000">
          {{ $t('noteCreate.copyError') }}
        </a-message-modal>
      </div>
      <a-btn to="/notes/create" gradient>{{ $t('noteCreate.createAnotherNote') }}</a-btn>
    </main>
  </div>
</template>

<style lang="scss" scoped>
.note-create-done-page {
  .content {
    margin: var(--gap-lg) auto 0;
    max-width: 800px;

    .actions {
      display: flex;
      gap: var(--gap-lg);
      margin-bottom: var(--gap-lg);

      .url {
        align-self: stretch;
        flex: 1 1 0;
        border-radius: var(--border-radius-lg);
        border: 2px solid currentColor;
        display: flex;
        align-items: center;
        padding: 0 var(--gap-md);
        overflow: hidden;
        font-size: 24px;

        @media screen and (max-width: $bp-sm-max) {
          font-size: 20px;
        }

        @media screen and (max-width: $bp-xs-max) {
          border-radius: var(--border-radius-md);
          font-size: 16px;
        }

        .text {
          width: 100%;
          overflow: hidden;
          text-overflow: ellipsis;
        }
      }
    }

    @media screen and (max-width: $bp-sm-max) {
      margin-top: var(--gap-md);

      .actions {
        gap: var(--gap-md);
        margin-bottom: var(--gap-md);
      }
    }
  }
}
</style>
