<script setup lang="ts"></script>

<template>
  <div class="about-page" v-html="$t('about')" />
</template>

<style lang="scss" scoped>
.about-page {
  font-size: 24px;
  font-weight: 300;
  text-indent: 2em;
  text-align: justify;

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
