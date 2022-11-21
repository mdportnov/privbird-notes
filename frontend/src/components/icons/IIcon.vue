<script setup lang="ts">
import { onMounted, ref } from 'vue'
import type { Ref } from 'vue'

defineProps<{
  noFill?: boolean
  stroke?: boolean
}>()

interface HTMLSVGElement extends HTMLElement {
  viewBox: {
    baseVal: {
      x: number
      y: number
      width: number
      height: number
    }
  }
}

const wrapper = ref() as Ref<HTMLSpanElement>

const aspectRatio = ref('1')

onMounted(() => {
  const icon = wrapper.value.firstElementChild as HTMLSVGElement
  const viewBox = icon.viewBox.baseVal
  aspectRatio.value = `${viewBox.width} / ${viewBox.height}`
})
</script>

<template>
  <span ref="wrapper" class="i-icon" :class="{ 'i-icon--no-fill': noFill, 'i-icon--stroke': stroke }">
    <slot />
  </span>
</template>

<style lang="scss" scoped>
.i-icon {
  display: inline-block;
  height: 1em;
  aspect-ratio: v-bind(aspectRatio);
  flex-shrink: 0;

  &:deep(svg) {
    vertical-align: top;
  }

  &:not(.i-icon--no-fill) {
    &:deep(svg) {
      fill: currentColor;
    }

    &.i-icon--stroke {
      &:deep(svg) {
        fill: none;
        stroke: currentColor;
      }
    }
  }
}
</style>
