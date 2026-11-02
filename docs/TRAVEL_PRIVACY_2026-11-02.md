# Tourism privacy disclosure — 2026-11-02

User requested the tourism privacy policy match actual processing and supported
languages. Current published app identity remains Pocket Korean: Korea Travel,
com.minororbit.koreatravel; HANTEUM: Travel Korean is only a naming proposal so far.

## Scope and evidence

Reviewed current app manifest/backup rules, PocketAds, direct Unity adapter,
AdPrivacyNotice, RemoteAdPolicy, AndroidAdRuntime, recording/speech implementation,
review/K-pop preference stores, sharing and HANTEUM external-browser links.
Reviewed official Play User Data rules, AdMob 25.5.0 disclosure and Unity 4.21.0
Google Data safety documentation. Public data disclosures do not themselves prove
all regional legal obligations or external SDK operations have been audited.

Added complete static policies in en, ja, zh-Hant, zh-Hans, es, pt-BR, fr, de, tr,
id, vi, th, hi, ne, km and bn. Each has12 matching subject sections. Not a claim of
native-speaker or legal-professional certification. Source JSON is maintained in
four translations*.json files; build/test scripts only change the tourism folder.

Disclosures cover device-only learning and recording, optional microphone,
MP3/device TTS and its network-dependent engines, Unity/AdMob/UMP, contextual
privacy flags without a no-data claim, signed six-hour GitHub checks, verified
offline policy cache, local ad diagnostics, website/store/map destinations,
share-sheet data, local reminder choices, exports, deletion/backup, provider
retention, international processing and support email. No claim that excluding
EU/UK/Switzerland waives rights or establishes a universal legal exemption.

## Compatibility and language behavior

Existing public URL remains /pocket-korean-travel/privacy/. The current Android
version28 and Play listing link point to this shared address. Only the root entry
uses browser-language routing; it does not know the app's explicit language
selection. Unsupported browser languages stay on English. All16 languages are
always manually selectable. Explicit /privacy/{locale}/ links never redirect and
work without JavaScript. No account, forms, analytics, cookies or browser storage
were added. Browser routing reads no IP/location and sends no identity query.
Do not claim the existing AAB automatically passes the selected app UI language.
No AAB rebuild, app source edit, Play review restart or brand rename is needed for
this hosted-policy update. A future app revision can use explicit localized paths.

## Verification

- Static checks:16 independent locale pages,12 sections each,16 valid language
  links per page, contact/package/date and SDK/weight data, generated-file equality,
  no replacement characters/placeholders, no forms/iframes/images/remote scripts.
-20 pure browser-language normalization cases passed, including Chinese script
  priority, pt-BR, Android legacy in-ID, regional codes and unsupported input.
- Browser390px layout inspected for all16 languages:12 headings per page and no
  horizontal overflow. Visual glyph/layout checks for Bengali, Nepali and Khmer.
  Temporary browser viewport restored. No real ad clicks or authenticated TTS calls.
- Existing non-tourism pages and shared config/ads.json are outside the changes.

Official references:
- https://support.google.com/googleplay/android-developer/answer/10144311?hl=en
- https://developers.google.com/admob/android/privacy/play-data-disclosure
- https://docs.unity.com/en-us/ads-android/4.21.0/privacy/developer-consent/disclosures/google-data-safety

Publication and live HTTP verification are recorded after deployment, separately
from the local validation above.

## HANTEUM branding preparation (not yet published)

After the initial localized-policy publication, the user requested the HANTEUM
rebrand. Local policy sources/pages now use the16 localized tourism app names
and translated Previous name labels. Package, root URL, locale paths and data
disclosures are unchanged. The updated branding pages pass structural checks;
no rebrand commit, push or Pages deployment has been performed yet. The prior
publication record above refers to the original Pocket-named policies.
