import type { INoteData } from '@/models/notes/data'
import type { INote } from '@/models/notes/notes'
import type { IRes } from '@/models/resource/default'
import { NotesService } from '@/services/notes'
import { useSingleState } from '@/utils/states/singleState'
import { defineStore } from 'pinia'

export const useNoteFormStore = defineStore('noteForm', {
  state: () => ({
    url: useSingleState<IRes<INote.Url>>(),
  }),
  actions: {
    async create(data: INoteData) {
      this.url.state.loading()
      const res = await NotesService.create(data)
      if (res.error) {
        this.url.state.error()
      } else {
        this.url.data = res.data
        this.url.state.success()
      }
      return res
    },
  },
})
