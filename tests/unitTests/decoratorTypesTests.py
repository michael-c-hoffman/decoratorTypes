"""
Test decoratorTypes
"""
import logging
import time

from testfixtures import LogCapture

import decoratorTypes

logger = logging.getLogger()


def testSingletonNewClass():
    """
    Test singletone class decorator works
    instatiate 2 instances should both have same id
    """

    @decoratorTypes.singleton
    class Foo:
        """
        basic class with attribute to validate singleton with
        """

        def __init__(self, bar: int) -> None:
            self.bar = bar

    instance1 = Foo(15)
    instance2 = Foo(20)
    assert id(instance1) == id(instance2)
    assert instance1.bar == instance2.bar


def testTimer():
    """
    Test timer function decorator works
    given a function log elapsed time
    """
    with LogCapture() as logCapture:
        timelogger = logging.getLogger(__name__ + "::testTimer")

        @decoratorTypes.timer(1)
        def myFunction():
            """
            myFunction test for time decorator with 1 precision
            """
            logging.info("Testing timer sleeping for 1s")
            time.sleep(1)

        myFunction()
        logger.info(myFunction.__doc__)
    # validate log capture
    # myFunction logs info "Testing timer sleeping for 1s
    # decoratorTypes info "def myFunction elapsed time=1.0
    # myFunction test for time decorator with 1 precision
    logCapture.check(
        ("root", "INFO", "Testing timer sleeping for 1s"),
        ("decoratorTypes", "INFO", "def myFunction elapsed time=1.0"),
        (
            "root",
            "INFO",
            "\n            myFunction test for time decorator with 1 precision\n            ",
        ),
    )
