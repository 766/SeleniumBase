""" The main purpose of this file is to demonstrate running SeleniumBase
    scripts without the use of Pytest by calling the script directly
    with Python or from a Python interactive interpreter. Based on
    whether relative imports work or don't, the script can autodetect
    how this file was run. With pure Python, it will initialize
    all the variables that would've been automatically initialized
    by the Pytest plugin. The setUp() and tearDown() methods are also
    now called from the script itself.

    One big advantage to running tests with Pytest is that most of this
    is done for you automatically, with the option to update any of the
    parameters through command line parsing. Pytest also provides you
    with other plugins, such as ones for generating test reports,
    handling multithreading, and parametrized tests. Depending on your
    specific needs, you may need to call SeleniumBase commands without
    using Pytest, and this example shows you how. """

try:
    # Running with Pytest / (Finds test methods to run using autodiscovery)
    # Example run command:  "pytest raw_parameter_script.py"
    from .my_first_test import MyTestClass  # (relative imports work: ".~")

except (ImportError, ValueError):
    # Running with pure Python OR from a Python interactive interpreter
    # Example run command:  "python raw_parameter_script.py"
    from my_first_test import MyTestClass  # (relative imports DON'T work)

    sb = MyTestClass("test_basic")
    sb.browser = "chrome"
    sb.headless = False
    sb.headed = False
    sb.start_page = None
    sb.servername = "localhost"
    sb.port = 4444
    sb.data = None
    sb.environment = "test"
    sb.user_agent = None
    sb.extension_zip = None
    sb.extension_dir = None
    sb.database_env = "test"
    sb.log_path = "latest_logs/"
    sb.archive_logs = False
    sb.disable_csp = False
    sb.enable_sync = False
    sb._reuse_session = False
    sb.visual_baseline = False
    sb.maximize_option = False
    sb.save_screenshot_after_test = False
    sb.timeout_multiplier = None
    sb.pytest_html_report = None
    sb.report_on = False
    sb.with_db_reporting = False
    sb.with_s3_logging = False
    sb.js_checking_on = False
    sb.is_pytest = False
    sb.slow_mode = False
    sb.demo_mode = False
    sb.demo_sleep = 1
    sb.message_duration = 2
    sb.settings_file = None
    sb.user_data_dir = None
    sb.proxy_string = None
    sb.ad_block_on = False
    sb.highlights = None
    sb.check_js = False
    sb.cap_file = None

    sb.setUp()
    try:
        sb.test_basic()
    finally:
        sb.tearDown()
        del sb
