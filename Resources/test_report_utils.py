import os
import webbrowser


def print_failed_tests():
    """Prints failed test cases from the last pytest run"""
    pytest_cache_dir = ".pytest_cache/v/cache/lastfailed"

    if os.path.exists(pytest_cache_dir):
        with open(pytest_cache_dir, "r") as file:
            failed_tests = file.read().strip()

        if failed_tests:
            print("\n❌ FAILED TEST CASES:")
            print("=" * 80)
            print(failed_tests)
            print("=" * 80)


def print_report_link():
    """Displays and opens the generated HTML report"""

    report_path = os.path.abspath("reports/test_report.html")
    report_url = "file:///" + report_path.replace("\\", "/")  # Convert \ to /
    print("\n📄 Test Report: " + report_url)

    print("=" * 80)


def generate_test_summary():
    """Executes after all tests to print failed test cases and open the report"""
    print_failed_tests()
    print_report_link()
