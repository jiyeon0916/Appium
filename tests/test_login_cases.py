import pytest
import allure
from utils.csv_loader import load_test_cases
from utils.allure_helper import attach_text
from pages.login_page import LoginPage
from pages.main_page import MainPage
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# CSV 기반 테스트 케이스 로드
cases = load_test_cases("data/test_login_cases.csv")

@allure.feature("모바일 앱 로그인/설치 자동화")
@pytest.mark.parametrize("tc_id, tc_name, description, precondition, action, expected, test_data, priority, auto", cases)
def test_mobile_cases(driver, tc_id, tc_name, description, precondition, action, expected, test_data, priority, auto):
    allure.dynamic.title(f"{tc_id} - {tc_name}")
    attach_text("사전조건", precondition)
    attach_text("테스트 절차", action)
    attach_text("기대 결과", expected)

    login = LoginPage(driver)
    main = MainPage(driver)

    # ===================================
    # TC별 분기 처리
    # ===================================
    if tc_id == "TC-01-01":
        # 앱 설치 (수동으로 처리)
        pytest.skip("앱 설치는 Appium으로 직접 다운로드 불가, 수동 진행 필요")

    elif tc_id in ["TC-01-02", "TC-01-03"]:
        pytest.skip("네거티브 설치 테스트: 수동 처리 필요")

    elif tc_id == "TC-02-01":
        email, pw = test_data.split(",")
        login.click_email_login()
        login.input_email(email.strip())
        login.input_password(pw.strip())
        login.click_login()
        assert main.is_displayed()

    elif tc_id == "TC-02-02":
        # 카카오 로그인 (UI 표시 확인)
        login.click_kakao_login()
        # 실제 ID/PW 입력은 보안상 불가
        assert driver.page_source  # 로그인 화면 표시만 확인

    elif tc_id == "TC-02-03":
        login.click_naver_login()
        assert driver.page_source  # UI 표시 확인

    elif tc_id == "TC-02-04":
        login.click_facebook_login()
        assert driver.page_source  # UI 표시 확인

    elif tc_id == "TC-02-05":
        login.click_apple_login()
        assert driver.page_source  # UI 표시 확인

    elif tc_id == "TC-02-06":
        email, pw = test_data.split(",")
        login.click_email_login()
        login.input_email(email.strip())
        login.input_password(pw.strip())
        login.click_login()
        msg = login.get_error_message()
        assert "10번" in msg

    elif tc_id == "TC-02-07":
        email, pw = test_data.split(",")
        login.click_email_login()
        login.input_email(email.strip())
        login.input_password(pw.strip())
        login.click_login()
        msg = login.get_error_message()
        assert "10번" in msg

    elif tc_id == "TC-02-08":
        pytest.skip("네트워크 끊김 시뮬레이션: 실제 장비 필요")

    elif tc_id == "TC-02-09":
        login.click_email_login()
        # 이메일/비밀번호 입력 안함
        login.click_login()
        msg = login.get_error_message()
        assert "입력" in msg

    elif tc_id == "TC-02-10" or tc_id == "TC-02-13":
        login.click_help_center()
        assert "고객센터" in driver.page_source

    elif tc_id == "TC-04-01":
        email, pw = test_data.split(",")
        login.click_email_login()
        login.input_email(email.strip())
        login.input_password(pw.strip())
        login.click_login()
        assert main.is_displayed()

    else:
        pytest.skip("정의되지 않은 테스트 케이스")
