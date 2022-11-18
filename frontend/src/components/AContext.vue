<script setup lang="ts">
import { nextTick } from '@/utils/nextTick'
import { ref } from 'vue'

const props = defineProps<{
  position?: {
    y?: 'top' | 'bottom'
    x?: 'left' | 'right'
  }
}>()

const show = ref(false)
const posY = ref('bottom')
const posX = ref('left')
const $container = ref<HTMLElement>()
const $context = ref<HTMLElement>()

const closeIfOutside = (evt: MouseEvent) => {
  if (!evt.composedPath().includes($context.value!)) swap(false)
}

const swap = async (val?: boolean) => {
  const newShow = val ?? !show.value

  if (newShow) {
    const box = $container.value!.getBoundingClientRect()
    posY.value = props.position?.y ?? (box.top + box.bottom > window.innerHeight ? 'top' : 'bottom')
    posX.value = props.position?.x ?? (box.left + box.right > window.innerWidth ? 'right' : 'left')
  }

  show.value = newShow

  await nextTick()

  if (show.value) document.addEventListener('click', closeIfOutside)
  else document.removeEventListener('click', closeIfOutside)
}
</script>

<template>
  <div ref="$container" class="root" :class="[posY, posX]">
    <slot name="main" :swap="swap" />
    <transition name="context">
      <div v-if="show" ref="$context" class="context">
        <slot name="context" :swap="swap" />
      </div>
    </transition>
  </div>
</template>

<style lang="scss" scoped>
.root {
  width: fit-content;

  .context {
    position: absolute;
    z-index: 100;
    min-width: 100%;
  }

  .context-enter-active,
  .context-leave-active {
    transition: transform 0.3s, opacity 0.3s;
  }

  .context-enter-from,
  .context-leave-to {
    opacity: 0;
  }

  $offset: var(--gap-sm);

  &.top {
    .context {
      top: 0;
      transform: translateY(calc(-100% - $offset));
    }

    .context-enter-from,
    .context-leave-to {
      transform: translateY(-100%);
    }
  }

  &.bottom {
    .context {
      bottom: 0;
      transform: translateY(calc(100% + $offset));
    }

    .context-enter-from,
    .context-leave-to {
      transform: translateY(100%);
    }
  }

  &.right {
    .context {
      right: 0;
    }
  }
}
</style>
