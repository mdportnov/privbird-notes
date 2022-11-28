import { $api } from '@/http'
import type { INoteData } from '@/models/notes/data'
import type { INote } from '@/models/notes/notes'
import type { IRes } from '@/models/resource/default'
import { IResourceError } from '@/models/resource/error'
import type { IResource } from '@/models/resource/resource'
import axios from 'axios'

export const NotesService = {
  async create(data: INoteData): Promise<IResource<IRes<INote.Slug>>> {
    try {
      const res = await $api.post<IRes<INote.Slug>>('/privnote/api/notes/', data)
      return { data: res.data }
    } catch (e) {
      if (axios.isAxiosError(e)) {
        return { error: IResourceError.build(e) }
      }
      throw e
    }
  },

  async fetch(slug: INote.Slug['slug']): Promise<IResource<IRes<INote>>> {
    try {
      const res = await $api.get<IRes<INote>>(`/privnote/api/notes/${slug}/`)
      return { data: res.data }
    } catch (e) {
      if (axios.isAxiosError(e)) {
        return { error: IResourceError.build(e) }
      }
      throw e
    }
  },

  async passFetch(slug: INote.Slug['slug'], data: INoteData.Password): Promise<IResource<IRes<INote>>> {
    try {
      const res = await $api.post<IRes<INote>>(`/privnote/api/notes/${slug}/`, data)
      return { data: res.data }
    } catch (e) {
      if (axios.isAxiosError(e)) {
        return { error: IResourceError.build(e) }
      }
      throw e
    }
  },
}
