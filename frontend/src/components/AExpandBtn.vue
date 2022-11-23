<script setup lang="ts">
import IArrowBottom from './icons/IArrowBottom.vue'

defineProps<{
  expand?: boolean
}>()

const emit = defineEmits<{
  (e: 'update:expand', val: boolean): void
}>()
</script>

<template>
  <button
    @click="emit('update:expand', !expand)"
    class="a-expand-btn"
    :class="{ 'a-expand-btn--expanded': expand }"
    type="button"
  >
    <i-arrow-bottom class="a-expand-btn__expand-icon a-expand-btn__expand-icon--part-1" />
    <i-arrow-bottom class="a-expand-btn__expand-icon a-expand-btn__expand-icon--part-2" />
  </button>
</template>

<style lang="scss">
.a-expand-btn {
  $size: 1em;
  width: $size;
  height: $size;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: hidden;

  &__expand-icon {
    font-size: 0.5 * $size;
    transition: transform $transition;

    &--part-1 {
      transform: translateY(50%);
    }

    &--part-2 {
      transform: translateY(-50%);
    }
  }

  &.a-expand-btn--expanded {
    .a-expand-btn__expand-icon {
      &--part-1 {
        transform: translateY(22%);
      }

      &--part-2 {
        transform: translateY(-22%) scaleY(-1);
      }
    }
  }
}
</style>
