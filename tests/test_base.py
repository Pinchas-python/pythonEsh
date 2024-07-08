import logging
import pytest
from infra.browser import Browser
from infra.teardown.tear_down import tear_down_tasks


class TestBase:
    test_failed = True
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    @pytest.fixture(scope="function")
    def before_after_test(self, request):
        test_name = request.node.originalname
        print('Starting test "' + test_name + '"')
        failed_before = request.session.testsfailed

        yield
        if request.session.testsfailed != failed_before:
            try:
                pass
                #playwright trace
            except:
                pass
        print('\r*****DONE*****')

