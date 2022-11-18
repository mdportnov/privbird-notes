<script setup lang="ts"></script>

<template>
  <div class="privacy-page" v-html="$t('privacy')" />
</template>

<style lang="scss" scoped>
.privacy-page {
  font-size: 24px;
  font-weight: 300;
  text-indent: 2em;
  text-align: justify;

  &:deep(p) {
    margin-bottom: 1em;
  }

  &:deep(b) {
    font-weight: 600;
  }

  @media screen and (max-width: $bp-sm-max) {
    font-size: 20px;
  }

  @media screen and (max-width: $bp-xs-max) {
    font-size: 18px;
  }
}
</style>
