<script setup lang="ts"></script>

<template>
  <div class="not-found-page">
    <span class="text">
      {{ $t('notFound') }}
    </span>
  </div>
</template>

<style lang="scss" scoped>
.not-found-page {
  position: relative;
  flex-basis: 100%;
  display: flex;
  justify-content: center;
  align-items: center;

  .text,
  &::before {
    background: linear-gradient(to top, var(--color-gradient-primary));
    background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .text {
    white-space: pre-line;
    text-align: center;
    font-weight: 600;
    font-size: 0.05 * $bp-lg;
  }

  &::before {
    content: '404';
    position: absolute;
    overflow: hidden;
    z-index: -1;
    font-size: min(0.5 * $bp-lg, 140vh);
    font-weight: 700;
    line-height: 0.8;
    opacity: 0.2;
  }

  @media screen and (max-width: $bp-md-max) {
    .text {
      font-size: min(5vw, 9vh);
    }

    &::before {
      font-size: min(50vw, 80vh);
    }
  }

  &:deep(+ .a-spacer) {
    display: none;
  }
}
</style>
