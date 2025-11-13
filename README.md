# Appium-Android-Test

## 📌 소개
- 본 프로젝트는 Android 앱 테스트를 위한 Appium 환경 설정 및 테스트 예제 프로젝트입니다.

---
## 📂 폴더 구조 및 설명

```
1️⃣ 디렉토리 구조 예시
mobile_automation/
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── main_page.py
├── tests/
│   └── test_login_cases.py
│   └── conftest.py
├── data/
│   └── test_login_cases.csv
├── utils/
│   ├── csv_loader.py
│   └── allure_helper.py
├── requirements.txt
└── README.md

```
---

## ⚙️ 필수 설치
- Python **3.11**
- Appium **2.0.0**
- UiAutomator2 드라이버 **6.1.1**
- Android SDK 및 ADB 설치 필요
- 에뮬레이터 또는 실제 디바이스 연결

---

## 🚀 설치 및 환경 설정 방법

#### 1. Appium 설치
```powershell
npm install -g appium
appium driver install uiautomator2
```
#### 2. APK 설치
```powershell
adb install \bucketplace-inc.apk
```
#### 3. 디바이스 확인
```powershell
adb devices
adb shell pm list packages | findstr test_app
```
#### 4. Python 라이브러리 설치
```powershell
pip install -r lib/requirements.txt
```
#### 5. pytest 실행 + Allure 결과 생성
```powershell
pytest -v --alluredir=allure-results
```
#### 6. Allure 보고서 확인
```powershell
allure serve allure-results
```
## 🔧 문제 해결
- Error type 3: Activity가 존재하지 않을 때 발생. appPackage와 appActivity 확인 필요
- spawn EINVAL: Appium 드라이버 실행 실패. Windows 환경에서 Appium 버전 호환 확인 필요
- 앱 실행 실패 시, APK가 설치되어 있는지 adb shell pm list packages로 확인
- ModuleNotFoundError: No module named 'utils' 에러인 경우: $env:PYTHONPATH = "{실행경로}" 추가
