<script setup lang="ts">
import { useEscape } from '@/utils/escape'
import { watch } from 'vue'
import AMessage, { type AMessageProps } from './AMessage.vue'

interface AMessageModalProps {
  show: boolean
  type: AMessageProps['type']
  timeout?: number
}

const props = defineProps<AMessageModalProps>()

const emit = defineEmits<{
  (e: 'update:show', val: boolean): void
  (e: 'close'): void
}>()

let timer: Nullable<number> = null
const close = () => {
  if (timer) {
    clearTimeout(timer)
    timer = null
  }
  emit('update:show', false)
  emit('close')
}
watch(
  () => props.show,
  () => {
    if (props.show && props.timeout) {
      timer = setTimeout(close, props.timeout)
    }
  },
)
useEscape(close)
</script>

<template>
  <teleport to="#app">
    <transition name="a-message-modal">
      <div v-if="show" @click.self="close" class="a-message-modal">
        <a-message :type="type" @close="close"><slot /></a-message>
      </div>
    </transition>
  </teleport>
</template>

<style lang="scss">
$transition-modal: 0.3s;
.a-message-modal {
  position: fixed;
  z-index: 10;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: var(--color-overlay);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: var(--gap-lg);

  @media screen and (max-width: $bp-sm-max) {
    padding: var(--gap-md);
  }

  &-enter-active,
  &-leave-active {
    transition: opacity $transition-modal;
  }

  &-enter-from,
  &-leave-to {
    opacity: 0;
  }
}
</style>
