<script setup lang="ts">
import { nextTick, ref, type Ref } from 'vue'
import AMessage, { type AMessageProps } from './AMessage.vue'

interface AClosableMessageProps {
  type: AMessageProps['type']
}

defineProps<AClosableMessageProps>()

const show = ref(true)

const $ref = ref() as Ref<HTMLDivElement>
const translate = ref<string>()
const close = async () => {
  translate.value = '-' + ($ref.value.style.height = getComputedStyle($ref.value).height)
  await nextTick()
  show.value = false
}
</script>

<template>
  <transition name="a-closable-message">
    <div v-if="show" ref="$ref" class="a-closable-message">
      <a-message :type="type" @close="close">
        <slot />
      </a-message>
    </div>
  </transition>
</template>

<style lang="scss" scoped>
$transition-closable: 0.4s;

.a-closable-message {
  &-leave-active {
    transition: height $transition-closable, opacity $transition-closable, transform $transition-closable;
  }

  &-leave-to {
    height: 0 !important;
    opacity: 0;
    transform: translateY(v-bind(translate));
  }
}
</style>
