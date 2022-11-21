import type { IFeedbackData } from '@/models/feedback/data'
import type { IRes } from '@/models/resource/default'
import { FeedbackService } from '@/services/feedback'
import { useSingleState } from '@/utils/states/singleState'
import { defineStore } from 'pinia'

export const useFeedbackStore = defineStore('feedback', {
  state: () => ({
    res: useSingleState<IRes<null>>(),
  }),
  actions: {
    async send(data: IFeedbackData) {
      this.res.state.loading()
      const res = await FeedbackService.send(data)
      if (res.error) {
        this.res.state.error()
      } else {
        this.res.data = res.data.data
        this.res.state.success()
      }
      return res
    },
  },
})
