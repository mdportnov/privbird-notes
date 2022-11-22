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
const { slug, key } = router.currentRoute.value.params as { slug: string; key?: string }

const loading = ref(true)

const store = useNoteStore()
onBeforeMount(async () => {
  await store.fetch(slug + (key ? `/${key}` : ''))
  loading.value = false
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
  <div v-loading.fullscreen.lock="loading" class="note-page">
    <template v-if="!loading">
      <note-page-security v-if="!store.note.data" />
      <note-page-content v-else :note="store.note.data.content" />
    </template>
    <a-message-modal v-model:show="showError" @close="$router.replace('/notes/create')" type="negative">
      {{ error }}
    </a-message-modal>
  </div>
</template>

<style lang="scss" scoped></style>
