// Smooth login button animation
document.addEventListener("DOMContentLoaded", () => {
  const btn = document.querySelector("button[type='submit']");
  const form = document.querySelector("form");

  form.addEventListener("submit", () => {
    btn.innerHTML = "Signing in...";
    btn.classList.add("opacity-80");
    btn.disabled = true;
  });
});
