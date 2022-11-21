import type { INoteData } from '@/models/notes/data'
import type { INote } from '@/models/notes/notes'
import { NotesService } from '@/services/notes'
import { useSingleState } from '@/utils/states/singleState'
import { defineStore } from 'pinia'

export const useNoteStore = defineStore('note', {
  state: () => ({
    note: useSingleState<INote>(),
  }),
  actions: {
    async fetch(slug: INote.Slug['slug']) {
      this.note.state.loading()
      const res = await NotesService.fetch(slug)
      if (res.error) {
        this.note.state.error()
      } else {
        this.note.data = res.data.data
        this.note.state.success()
      }
      return res
    },

    async passFetch(slug: INote.Slug['slug'], data: INoteData.Password) {
      this.note.state.loading()
      const res = await NotesService.passFetch(slug, data)
      if (res.error) {
        this.note.state.error()
      } else {
        this.note.data = res.data.data
        this.note.state.success()
      }
      return res
    },
  },
})
