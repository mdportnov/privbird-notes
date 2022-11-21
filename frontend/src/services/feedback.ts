import { $api } from '@/http'
import type { IFeedbackData } from '@/models/feedback/data'
import type { IRes } from '@/models/resource/default'
import { IResourceError } from '@/models/resource/error'
import type { IResource } from '@/models/resource/resource'
import axios from 'axios'

export const FeedbackService = {
  async send(data: IFeedbackData): Promise<IResource<IRes<null>>> {
    try {
      const res = await $api.post<IRes<null>>('/feedbacks/', data)
      return { data: res.data }
    } catch (e) {
      if (axios.isAxiosError(e)) {
        return { error: IResourceError.build(e) }
      }
      throw e
    }
  },
}
