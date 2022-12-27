/// <reference types="vite/client" />

interface ImportMeta {
  readonly env: ImportMetaEnv
}

declare const process: {
  readonly env: {
    readonly VITE_FEEDBACK_URL: string
    readonly VITE_PRIVNOTE_URL: string
    readonly VITE_FEEDBACK_API_URL: string
    readonly VITE_PRIVNOTE_API_URL: string
  }
}
