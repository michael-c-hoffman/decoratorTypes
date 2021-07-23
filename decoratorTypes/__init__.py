"""
decoratorTypes - Library of decorator types
"""
import functools
import logging
import timeit
import typing

logger = logging.getLogger(__name__)


def singleton(cls):
    """
    Make a class a Singleton class (only one instance)
    """

    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton


def timer(precision: typing.Optional[int] = None) -> typing.Callable:
    """
    Make a timer decorator utilizing time
    """

    def decorator(function):
        @functools.wraps(function)
        def wrapper_timer(*args, **kwargs):
            start_time = timeit.default_timer()
            functionReturn = function(*args, **kwargs)
            elapsed = timeit.default_timer() - start_time
            if precision is None:
                logger.info(f"def {function.__name__} elapsed time={elapsed}")
            else:
                logger.info(
                    f"def {function.__name__} elapsed time={elapsed:.{precision}f}"
                )
            return functionReturn

        return wrapper_timer

    return decorator
