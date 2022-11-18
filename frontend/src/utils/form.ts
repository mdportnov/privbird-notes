import { computed, toRef, type DefineComponent } from 'vue'
import { useField as veeUseField } from 'vee-validate'
import type { SFCWithInstall } from 'element-plus/es/utils'
import { useI18n } from 'vue-i18n'
import { setLocale } from 'yup'

export type ElProps<T extends SFCWithInstall<DefineComponent<any, any, any, any, any, any, any, any>>> = Omit<
  Partial<Parameters<Defined<T['data']>>[0]['$props']>,
  'modelValue'
>

export function useField<T = any>(props: { name: string }) {
  const { handleBlur, validate, meta, errorMessage, ...rest } = veeUseField<T>(toRef(props, 'name'))
  const { t } = useI18n()

  const onBlur = (evt: Event) => {
    handleBlur(evt)
    validate()
  }

  const error = computed(() => {
    if (!meta.touched || !errorMessage.value) return undefined
    const params = errorMessage.value.split('|')
    return params.length > 1 ? t('validation.' + params[0], { param: params[1] }) : t('validation.' + params[0])
  })

  return {
    ...rest,
    handleBlur,
    onBlur,
    validate,
    meta,
    error,
  }
}

export function useValidationLocale() {
  setLocale({
    mixed: {
      default: 'default',
      required: 'required',
    },
    string: {
      email: 'email',
      max: ({ max }) => `max|${max}`,
    },
  })
}
