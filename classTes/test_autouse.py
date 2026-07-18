import time
import pytest
@pytest.fixture(autouse=True, scope="session")
def footer_session_scope():
    yield
    now = time.time()
    print("finished :{}".format(time.strftime("%d %b %X", time.localtime(now))))


@pytest.fixture(autouse=True)
def footer_function_scope():
    start = time.time()
    yield
    delta = time.time() - start

    print("\n test duration :{:0.3} seconds".format(delta))


def test_1():
    time.sleep(1)


def test_2():
    time.sleep(1.23)