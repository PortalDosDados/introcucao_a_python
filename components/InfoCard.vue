<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(
  defineProps<{
    title?: string
    variant?: 'blue' | 'teal' | 'amber' | 'slate' | 'indigo' | 'rose' | 'dark'
  }>(),
  { variant: 'blue' }
)

const styleMap = {
  blue: 'bg-[#e8eaf6] border-[#1a237e] text-slate-800',
  teal: 'bg-[#e0f2f1] border-[#00695c] text-slate-800',
  amber: 'bg-[#fff8e1] border-[#ff8f00] text-slate-800',
  slate: 'bg-[#f8fafc] border-[#64748b] text-slate-800',
  indigo: 'bg-[#eef2ff] border-[#4f46e5] text-slate-800',
  rose: 'bg-[#fff1f2] border-[#be123c] text-slate-800',
  dark: 'bg-[#1e1e1e] border-[#3949ab] text-slate-100',
}

const titleMap = {
  blue: 'text-[#1a237e]',
  teal: 'text-[#004d40]',
  amber: 'text-[#b45309]',
  slate: 'text-[#1e293b]',
  indigo: 'text-[#3730a3]',
  rose: 'text-[#9f1239]',
  dark: 'text-[#93c5fd]',
}

const cardClass = computed(() => styleMap[props.variant] || styleMap.blue)
const headingClass = computed(() => titleMap[props.variant] || titleMap.blue)
</script>

<template>
  <div
    :class="[
      'rounded-xl border-l-4 px-3.5 py-2.5 shadow-sm text-[0.8rem] leading-snug',
      cardClass,
    ]"
  >
    <div v-if="title" :class="['font-bold text-[0.88rem] mb-1', headingClass]">
      {{ title }}
    </div>
    <div class="space-y-1 [&>p]:m-0 [&>ul]:m-0 [&>ul]:pl-4 [&>ol]:m-0 [&>ol]:pl-4">
      <slot />
    </div>
  </div>
</template>
