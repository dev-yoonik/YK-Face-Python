""" Utilities for the Python SDK of the YooniK Face API.
"""
import yk_utils.apis


class Key:
    """Manage Subscription Key."""
    @classmethod
    def set(cls, key: str):
        """Set the Subscription Key.
        :param key:
        :return:
        """
        yk_utils.apis.Key.set(key)


class BaseUrl:
    """Manage YooniK Face API base URL."""
    @classmethod
    def set(cls, base_url: str):
        yk_utils.apis.BaseUrl.set(base_url)
