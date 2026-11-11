<script setup lang="ts">
defineProps<{
  title: string
  subtitle?: string
  badge?: string
}>()
</script>

<template>
  <header class="mb-3">
    <div class="flex items-start justify-between gap-3">
      <div class="min-w-0 flex-1">
        <div class="flex items-center gap-2.5 flex-wrap">
          <h1 class="!m-0 !text-[1.45rem] !leading-tight font-extrabold text-[#1a237e]">
            {{ title }}
          </h1>
          <span
            v-if="badge"
            class="inline-block rounded-full bg-[#e8eaf6] text-[#1a237e] border border-[#c5cae9] px-2.5 py-0.5 text-[11px] font-bold uppercase tracking-wide"
          >
            {{ badge }}
          </span>
        </div>
        <p v-if="subtitle" class="!m-0 !mt-0.5 text-[0.86rem] font-medium text-[#5c6bc0] leading-snug">
          {{ subtitle }}
        </p>
      </div>
    </div>
    <div class="mt-2 h-[2.5px] w-full rounded-full bg-gradient-to-r from-[#1a237e] via-[#5c6bc0] to-[#e8eaf6]" />
  </header>
</template>
