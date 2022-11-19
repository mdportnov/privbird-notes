<script setup lang="ts">
import NotePageSecurity from './Security/NotePageSecurity.vue'
import NotePageContent from './Content/NotePageContent.vue'
import { useNoteStore } from '@/stores/note'
import { useRouter } from 'vue-router'
import { onBeforeMount, ref } from 'vue'
import { vLoading } from 'element-plus'
import 'element-plus/es/components/loading/style/css'
import AMessageModal from '@/components/message/AMessageModal.vue'

const router = useRouter()

const needPassword = ref(false)

const store = useNoteStore()
onBeforeMount(async () => {
  const res = await store.fetch(router.currentRoute.value.params.slug as string)
  if (res.error?.statusCode === 403) {
    needPassword.value = true
  }
})

const error = ref('')
const showError = ref(false)
store.$onAction(({ after }) => {
  after((res) => {
    if (res.error?.statusCode === 404) {
      router.replace('/not-found')
    } else if (res.error && res.error.statusCode !== 403) {
      error.value = res.error.message
      showError.value = true
    }
  })
})
</script>

<template>
  <div v-loading.fullscreen.lock="store.note.state.isLoading()" class="note-page">
    <note-page-security v-if="needPassword && !store.note.data" />
    <note-page-content v-else-if="store.note.data" :note="store.note.data.content" />
    <a-message-modal v-model:show="showError" @close="$router.replace('/notes/create')" type="negative">
      {{ error }}
    </a-message-modal>
  </div>
</template>

<style lang="scss" scoped></style>
