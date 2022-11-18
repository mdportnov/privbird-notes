import type { ILocale } from '../i18n/locale'
import type { EExpires } from './expires'
import type { INoteForm } from './form'
import type { ENetwork } from './network'

export interface INoteData {
  note: INoteData.Note
  fake: INoteData.Fake
  options: INoteData.Options
}

export namespace INoteData {
  export interface Note {
    content: string
    password: Nullable<string>
    notification: boolean
  }

  export interface Fake {
    content: Nullable<string>
    password: Nullable<string>
    notification: Nullable<boolean>
  }

  export interface Options {
    network: ENetwork
    expires: EExpires
    email: Nullable<string>
    language: Uppercase<ILocale>
  }

  export type Password = Pick<Note, 'password'>

  export function fromForm(form: INoteForm, locale: ILocale): INoteData {
    return {
      note: {
        content: form.note.content,
        password: form.note.password || null,
        notification: form.note.notification || false,
      },
      fake: {
        content: form.fake?.content || null,
        password: form.fake?.password || null,
        notification: form.fake?.content ? form.fake.notification || false : null,
      },
      options: {
        network: form.options?.network || 'HTTPS',
        expires: form.options?.expires || 'Expires.YEAR',
        email: form.options?.email || null,
        language: locale.toUpperCase() as Options['language'],
      },
    }
  }
}
