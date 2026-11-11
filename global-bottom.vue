<template>
  <footer
    v-if="!$slidev.nav.currentSlideRoute?.meta?.slide?.frontmatter?.hideFooter"
    class="pointer-events-none fixed bottom-2 left-9 right-9 flex items-center justify-between text-xs text-slate-400"
  >
    <span class="font-medium tracking-wide">
      Lógica de Programação (60h) · Prof. Dione Nascimento
    </span>
    <div class="flex items-center gap-4">
      <span class="font-mono text-[11px] bg-slate-100 text-slate-600 px-2 py-0.5 rounded">
        {{ $slidev.nav.currentPage }} / {{ $slidev.nav.total }}
      </span>
      <img
        v-if="!$slidev.nav.currentSlideRoute?.meta?.slide?.frontmatter?.hideLogo"
        src="/images/senai_logo.png"
        alt="SENAI Ceará"
        class="h-6 w-auto object-contain opacity-90"
      />
    </div>
  </footer>
</template>
