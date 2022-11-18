import type { INoteData } from '@/models/notes/data'
import type { INote } from '@/models/notes/notes'
import type { IRes } from '@/models/resource/default'
import { NotesService } from '@/services/notes'
import { useSingleState } from '@/utils/states/singleState'
import { defineStore } from 'pinia'

export const useNoteFormStore = defineStore('noteForm', {
  state: () => ({
    slug: useSingleState<IRes<INote.Slug>>(),
  }),
  actions: {
    async create(data: INoteData) {
      this.slug.state.loading()
      const res = await NotesService.create(data)
      if (res.error) {
        this.slug.state.error()
      } else {
        this.slug.data = res.data
        this.slug.state.success()
      }
      return res
    },
  },
})
