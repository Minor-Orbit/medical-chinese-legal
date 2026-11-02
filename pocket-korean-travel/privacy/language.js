// Browser language is used only at the old shared entry URL.
// An explicit /privacy/{locale}/ page is never redirected.
(function () {
  "use strict";
  const supported = ["en","ja","zh-Hant","zh-Hans","es","pt-BR","fr","de","tr","id","vi","th","hi","ne","km","bn"];
  function resolve(tag) {
    const parts = String(tag || "").replace(/_/g, "-").toLowerCase().split("-");
    const language = parts[0];
    const subtags = parts.slice(1);
    if (language === "zh") {
      if (subtags.includes("hant")) return "zh-Hant";
      if (subtags.includes("hans")) return "zh-Hans";
      return subtags.some(x => ["tw","hk","mo"].includes(x)) ? "zh-Hant" : "zh-Hans";
    }
    if (language === "pt") return "pt-BR";
    if (language === "in") return "id";
    return supported.includes(language) ? language : "en";
  }
  // Export only the pure function for deterministic local verification.
  if (typeof module !== "undefined" && module.exports) { module.exports = resolve; return; }
  if (typeof window === "undefined") return;
  const target = resolve((navigator.languages && navigator.languages[0]) || navigator.language);
  if (target !== "en") window.location.replace(new URL(target + "/", window.location.href).href);
})();
