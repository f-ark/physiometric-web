// Tema düğmesi: açık ve koyu arasında geçer; seçim bu tarayıcıda hatırlanır.
// İlk değer <head> içindeki küçük betikle, sayfa çizilmeden önce uygulanır (yanıp sönme olmaz).
const btn = document.querySelector('[data-theme-toggle]');
if (btn) {
  btn.addEventListener('click', () => {
    const root = document.documentElement;
    const dark = root.dataset.theme
      ? root.dataset.theme === 'dark'
      : matchMedia('(prefers-color-scheme: dark)').matches;
    const next = dark ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('theme', next); } catch (e) { /* gizli pencere: yalnızca bu sayfada geçerli */ }
  });
}
