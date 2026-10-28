---
layout: kpop-pocket-korean
title: Privacy policy
lang: en
policy_language: en
---

# Privacy policy

Effective date: October 28, 2026. This policy describes K-pop Pocket Korean for Android, package `com.minororbit.fankorean`, across its guide languages. The developer's public support contact is **davidleepub@gmail.com**.

## 1. Learning on your device

The app provides Korean expressions, Hangul practice and fan-related learning situations. Its learning content is bundled with the app. There is no developer-operated learning server, user account, login or cloud synchronization. We do not operate a separate analytics or crash-reporting service in this version. This does **not** mean that the entire app has no external data processing: Google and Unity advertising services, the selected Android speech provider and services you choose to open may process data as explained below.

## 2. Information stored locally

The app stores saved expression IDs, completed situation IDs, completion counts and timestamps, earned badge records and dates, practice-set titles and ordered expression IDs, listening counts, the last learning position, display and speech settings, selected speech engine and voices, locally unlocked lessons, and the expiry of a temporary banner-ad pause. It also keeps local mascot-message rotation records and the first-open time and foreground duration used for introductory greetings. These records support learning, resuming, customization and advertising rewards. They are stored in the app's private database or preferences, without being uploaded to a developer learning server.

## 3. Optional microphone recording

Microphone access is requested when you choose to record your own practice. You can decline permission and continue using other learning features. A recording lasts up to 30 seconds and is stored as an audio file in the app's private storage. A successful new recording replaces the previous recording for that expression. You can play or delete it in the app.

The app does not send practice recordings to the developer, Google advertising services or an AI service. It does not perform speech recognition or automated pronunciation scoring. Recording is for your own listening comparison; avoid recording other people without their permission.

## 4. Android text-to-speech

Learning expressions use pre-generated Google Cloud Text-to-Speech audio files bundled with the app by default. In audio settings or a practice screen, you can instead choose a compatible installed Android Korean text-to-speech voice. This alternative uses the device speech engine, not the Google Cloud TTS generation API. The developer generated these files from the app's fixed curriculum, not from user recordings or learning records. Playback does not call the Google Cloud Text-to-Speech API. Voice choices for expressions and individual dialogues are stored locally.

Some Hangul practice sounds and helper text use an installed Android text-to-speech engine. The app selects installed Korean voices that the engine identifies as not requiring a network connection. Installing an engine or downloading a voice may require internet access. The engine is separate software and may process its own diagnostic or service data under its provider's policy. The app does not send your practice recordings to that engine. Device speech tools are available in audio help.

The optional home-mascot audio consists of preset, pre-generated files bundled with the app. The installed app does not call fal.ai or ElevenLabs to generate those greetings, and does not transmit your recordings or learning records to those services.

## 5. Google advertising and consent

The app uses Google AdMob through the Google Mobile Ads SDK and Google's User Messaging Platform. It displays banner ads and optional rewarded ads. The advertising SDK can collect or share IP addresses (which can be used to estimate approximate location), device or advertising identifiers, app/ad interaction information and diagnostic information for advertising, measurement and fraud prevention. Advertising can therefore involve transfers to Google and its advertising partners and processing outside your country. The app does not request precise GPS location for learning or advertising.

The app requests consent information and shows Google's consent form when required by that service. Advertising initialization is gated by Google's ability-to-request-ads signal. When Google requires a privacy-options entry, an advertising privacy control appears in the app's settings. Device advertising-ID controls and the available consent choices may also affect advertising. Available choices depend on region and Google's configuration; we do not promise that all ads are personalized or that a banner pause stops every SDK activity.

Rewarded ads are optional. One reward pauses banner ads for two hours; a separate reward unlocks one additional learning situation on this device. The reward is applied after the SDK confirms that it was earned. These rewards are local records, not purchases, money or transferable account entitlements. Clearing app storage or uninstalling can remove them.

For the service's details, see [Google's privacy policy](https://policies.google.com/privacy), [Google advertising information](https://policies.google.com/technologies/ads), and [Google Mobile Ads SDK data disclosure](https://developers.google.com/admob/android/privacy/play-data-disclosure). The installed SDK version for this release is 24.9.0; Google's disclosure page may describe a newer version.


### Unity Ads direct SDK

From version 0.8.8, the app also uses Unity Ads SDK 4.21.0 directly for banners and voluntary rewarded ads. Unity may collect and share IP-derived approximate location, device/advertising and SDK identifiers, ad interactions and diagnostics for advertising, measurement, app functionality and fraud prevention. The app sends Unity a refusal of personalized advertising and sale/sharing consent; contextual ads still process data and may involve international transfers. Learning progress and practice recordings are not sent to Unity. No LevelPlay or Ad Quality SDK is included in this version. See [Unity's privacy policy](https://unity.com/legal/privacy-policy), [Unity Ads data disclosure](https://docs.unity.com/en-us/ads-android/4.21.0/privacy/developer-consent/disclosures/google-data-safety) and [Unity privacy choices](https://unity.com/legal/privacy-policy#privacy-rights).

Unity's published SDK disclosure also lists personal identifiers and purchase history among SDK data categories. This app does not create user accounts, offer in-app purchases, or supply account IDs or purchase records through a developer integration. Advertising identifiers and advertising-related information may still be processed by the SDK under Unity's policy. Its disclosure lists personal identifiers for app functionality and purchase history for advertising/marketing and analytics. Acquire Optimization is not enabled for this app; we do not enable the optional retention/app-usage-time collection described for that feature.

## 6. Sharing and manual backups

If you share a practice set, the app creates a file containing its title, expression IDs, their order and format/content version information, and gives that file to the app you select through Android's sharing interface. It does not include recordings, learning progress or advertising unlocks. Do not put sensitive personal information in set titles. The receiving app or service may store or transmit the file under its own policy. Temporary sharing files are kept in the app cache and older files are cleaned during subsequent exports.

You can manually export a learning backup using Android's document picker. It contains saved expressions, completed situations and practice sets. It does not contain recordings, completion counts, earned badge records, settings, listening counts, mascot rotation records or advertising rewards/unlocks. Restored completed-situation records can recover lesson-based badge eligibility, but do not restore repeat or voice badge records. You choose where the file is saved; a cloud document provider you select may upload it. Imports merge supported learning records. Files outside app storage remain under your control and must be deleted separately.

The app disables Android automatic backup and configures cloud-backup and device-transfer exclusions for its app data. These settings do not prevent a user-selected document provider from storing a manual export.

## 7. Retention, deletion and security

Local learning records remain until you remove supported individual items, clear app storage or uninstall the app. Unsaving an expression, deleting a practice set and deleting a recording remove the corresponding item. Hiding a completed lesson does not delete its learning record. To remove all local app data, use Android Settings → Apps → K-pop Pocket Korean → Storage → Clear storage, or uninstall the app. This also removes locally unlocked lessons and ad-pause records. Delete exported files separately. Speech-engine downloads are managed by the speech provider, not by this app.

We cannot remotely access or delete records held only on your device. Google and other services manage retention and deletion for data they process under their own policies. The app uses Android's private app storage; this is not a promise of additional end-to-end encryption or protection on a compromised device. Google states that Mobile Ads SDK network data is encrypted in transit.

## 8. External pages, support and younger users

Opening an external learning resource or this policy contacts that website. These policy pages are hosted on GitHub Pages, whose hosting service may process request information such as IP addresses under [GitHub's privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). This hosting is not a learning-data backend.

If you email support, we receive your email address and the information you choose to send, and use them to respond to your request. Please do not send passwords, unnecessary personal information or private recordings. There is no in-app account registration or age-profile collection. A parent or guardian with a concern about a younger user's use or data can contact support; device-level microphone and advertising controls remain available.

## 9. Contact and changes

For privacy questions, contact **[davidleepub@gmail.com](mailto:davidleepub@gmail.com)**. We may revise this policy when app features or service practices change and will update the effective date. Material changes will also be described through appropriate app or release information.

[Usage & content notices](../notices/)

## Remote advertising settings


Advertising settings are periodically downloaded from GitHub Pages. GitHub may process your IP address for this request; your learning records and recordings are not sent. The app uses one fixed HTTPS address and checks at most once every six hours on foreground entry. Settings are verified against the existing ads-v1 public key before use. Failed downloads keep the last verified settings. Only ad-network activation and the initial request weight can change; ad IDs, consent requirements and executable code cannot. Diagnostic event codes and ad-failure times remain on the device and are not uploaded by this feature.
