<script setup lang="ts">
import { ElCollapse, ElCollapseItem } from 'element-plus'
</script>

<template>
  <div class="faq-page">
    <el-collapse accordion>
      <el-collapse-item v-for="(item, idx) of $tm('faq')" :key="idx" :name="idx">
        <template #title>
          <h1 class="title">{{ Number(idx) + 1 }}. {{ item.title }}</h1>
        </template>
        <div v-html="item.text" />
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<style lang="scss" scoped>
.faq-page {
  text-align: justify;

  &:deep(.el-collapse) {
    transition: border-color $transition-theme;

    .el-collapse-item__header {
      height: auto;
      min-height: 50px;
      color: var(--color-text);

      .title {
        padding: 0.7em;
        font-size: 20px;
        font-weight: 500;
        line-height: initial;
      }

      @media screen and (max-width: $bp-xs-max) {
        font-size: 18px;
      }
    }

    .el-collapse-item__header,
    .el-collapse-item__wrap {
      background-color: var(--color-background);
      transition: $transition-theme;

      .el-collapse-item__content {
        color: var(--color-text);
        transition: color $transition-theme;
        padding: 1em;
        padding-top: 0;
        font-size: 18px;

        @media screen and (max-width: $bp-xs-max) {
          font-size: 16px;
        }
      }
    }
  }
}
</style>
