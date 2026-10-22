# 한국일터 정책·데이터 보안 반영 기록

대상: Workplace Korean: Learn Korean (`com.minororbit.workplacekorean`)만 해당합니다.

- 2026-10-22 영문·한국어 개인정보처리방침 갱신. Unity 광고, 기기 TTS/내장 MP3, 이전 버전과 Unity 적용 업데이트의 차이를 명시했습니다.
- 정책 커밋: `c8befcd`. 양쪽 GitHub Pages URL에서 HTTP 200 및 Unity SDK 버전 표기를 확인했습니다.
- Play Console 기존 신고에 SDK 사용자 ID·구매 내역을 추가하고 위치·진단·기기 ID의 처리 목적을 보강했습니다. 이름·이메일·계좌·카드 정보나 마이크 녹음 업로드를 신고한 것은 아닙니다.
- 최종 신고 유형: 대략적인 위치, 사용자 ID, 구매 내역, 앱 상호작용, 진단, 기기 또는 기타 ID. 수집·공유 및 비임시 처리로 기록했습니다.
- Unity 설정에서 Acquire 최적화의 Google Play 항목은 비어 있고 편집이 비활성화된 상태를 확인했습니다. 이를 활성화한다면 추가 앱 활동 신고를 다시 검토해야 합니다.
- 데이터 보안 변경 **한 건만** 저장하고 검토 전송을 요청했습니다. Console은 ‘검토 중인 변경사항’과 자동 검사 진행 상태를 표시했습니다. 자동 검사 후 검토 전송되며, 승인·공개 완료를 의미하지 않습니다.
- 앱 바이너리/AAB, 테스터, 다른 앱의 신고·문서는 변경하지 않았습니다.

## 정책 URL

- https://minor-orbit.github.io/medical-chinese-legal/workplace-korean/privacy/
- https://minor-orbit.github.io/medical-chinese-legal/workplace-korean/privacy/ko/

## 확인 근거

- Unity Ads: https://docs.unity.com/en-us/grow/ads/privacy/google-data-safety
- Google Mobile Ads: https://developers.google.com/admob/android/privacy/play-data-disclosure
- Google Play: https://support.google.com/googleplay/android-developer/answer/10787469

AdMob은 앱 코드에서 계속 비활성화돼 있습니다. 신고 범위에는 기존 Google 광고 버전도 고려했습니다. 광고 사용을 재활성화하거나 SDK·선택형 데이터 기능을 변경할 때 다시 대조하세요.
