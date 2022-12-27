import { fileURLToPath, URL } from 'node:url'

import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'

import ElementPlus from 'unplugin-element-plus/vite'

import { readFileSync } from 'node:fs'
import path from 'node:path'

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd())
  for (const key of Object.keys(env)) {
    const val = process.env[key.replace(/^VITE_/, '')]
    if (val) env[key] = val
  }

  return {
    plugins: [vue(), ElementPlus()],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url)),
      },
    },
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: scssVarsLoader('./src/css/imports.scss'),
        },
      },
    },
    server: {
      host: '0.0.0.0',
      port: 8080,
    },
    define: {
      __VUE_I18N_FULL_INSTALL__: true,
      __VUE_I18N_LEGACY_API__: false,
      __INTLIFY_PROD_DEVTOOLS__: false,
      'process.env': env,
    },
  }
})

function scssVarsLoader(rootPath: string) {
  const scss = loadScss(rootPath)

  return (content: string, src: string) => {
    const hasScss = content.includes('$')
    const isVue = path.parse(src).ext === '.vue'

    if (isVue && hasScss) return scss + content

    return content
  }

  function loadScss(filepath: string): string {
    const scss: string[] = []
    const fileDir = path.parse(filepath).dir

    const importReplacer = (_: string, param: string) => {
      const importPath = path.join(fileDir, param)
      scss.push(loadScss(importPath))
      return ''
    }
    scss.push(
      readFileSync(filepath)
        .toString()
        .replace(/@import '(.*)';/g, importReplacer)
        .replace(/:export\s{0,1}\{[\s\S]*\}/gm, ''),
    )

    return scss.join('\n')
  }
}
