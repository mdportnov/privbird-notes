import type { IFeedbackForm } from './form'

export interface IFeedbackData {
  email: Nullable<string>
  feedback: string
}

export namespace IFeedbackData {
  export function fromForm(form: IFeedbackForm): IFeedbackData {
    return {
      email: form.email || null,
      feedback: form.feedback,
    }
  }
}
