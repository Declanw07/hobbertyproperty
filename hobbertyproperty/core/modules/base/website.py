import abc
from typing import List


class PropertyWebsiteBase(metaclass=abc.ABCMeta):

    def __init__(
            self,
            base_url: str
    ) -> None:
        self._base_url = base_url
        self._searches = []

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def searches(self) -> List[str]:
        return self._searches

    @abc.abstractmethod
    def add_search(
            self,
            min_price: int,
            max_price: int,
            min_bedrooms: int,
            max_bedrooms: int,
            min_bathrooms: int,
            max_bathrooms: int
    ) -> None:
        """
        Adds a search string to self._searches, this will be a formatted URI
        that is specific to the website. Requires implementation on a
        per-website basis.

        Args:
            min_price:          Minimum price in GBP (£)
            max_price:          Maximum price in GBP (£)
            min_bedrooms:       Minimum number of bedrooms
            max_bedrooms:       Maximum number of bedrooms
            min_bathrooms:      Minimum number of bathrooms
            max_bathrooms:      Maximum number of bathrooms
        """


