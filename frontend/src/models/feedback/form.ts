import { object, string, type SchemaOf } from 'yup'

export interface IFeedbackForm {
  email: string
  feedback: string
}

export namespace IFeedbackForm {
  export function validation(): SchemaOf<IFeedbackForm> {
    return object({
      email: string().default('').email().max(256),
      feedback: string().required().max(1000),
    })
  }
}
