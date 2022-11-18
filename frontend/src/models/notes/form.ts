import { bool, object, string, ref, type SchemaOf, type StringSchema } from 'yup'
import type { INoteData } from './data'
import { EExpires } from './expires'
import { ENetwork } from './network'

export interface INoteForm {
  note: INoteForm.Note
  advanced?: boolean
  fake?: INoteForm.Fake
  options?: INoteForm.Options
}

export namespace INoteForm {
  export interface Note {
    content: string
    password?: string
    repeatPassword?: string
    notification?: boolean
  }

  export interface Fake extends Omit<Note, 'content'> {
    content: string
    enable?: boolean
    enablePassword?: boolean
  }

  export interface Options {
    network: ENetwork
    expires: EExpires
    email: string
  }

  export function validation(): SchemaOf<INoteForm> {
    return object().shape(
      {
        note: object({
          content: string().default('').required().max(40000),
          password: string().default(''),
          repeatPassword: string()
            .default('')
            .when('password', { is: (val: string) => !!val, then: string().required() })
            .oneOf([ref('password'), ''], 'passIdentical'),
          notification: bool().default(false),
        }).when('fake.enablePassword', {
          is: true,
          then: object({
            password: string().required(),
            repeatPassword: string().required(),
          }),
        }),
        advanced: bool(),
        fake: object({
          enable: bool(),
          content: string()
            .default('')
            .when('enable', { is: true, then: string().required().max(40000) }),
          enablePassword: bool(),
          password: string().default('').when('enablePassword', { is: true, then: string().required() }),
          repeatPassword: string()
            .default('')
            .when('enablePassword', {
              is: true,
              then: string()
                .required()
                .oneOf([ref('password'), ''], 'passIdentical'),
            }),
          notification: bool().default(false),
        }).when('note.password', {
          is: (val: string) => !!val,
          then: object({
            enablePassword: bool().when('enable', { is: true, then: bool().required().isTrue('required') }),
          }),
        }),
        options: object({
          network: (string() as StringSchema<ENetwork>).default('HTTPS').oneOf([...ENetwork.values]),
          expires: (string() as StringSchema<EExpires>).default('Expires.YEAR').oneOf([...EExpires.values]),
          email: string().email().default(''),
        }).when(['note.notification', 'fake.notification'], {
          is: (...values: boolean[]) => values.some((el) => el),
          then: object({ email: string().required() }),
        }),
      },
      [['note', 'fake']],
    )
  }

  export function passValidation(): SchemaOf<INoteData.Password> {
    return object({
      password: string().required(),
    })
  }
}
