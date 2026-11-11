import { defineConfig } from 'unocss'

export default defineConfig({
  blocklist: [
    /^\[[0-9]+:[0-9]+\]$/,
  ],
})
