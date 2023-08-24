import abc

from hobbertyproperty.core.modules.base.settings import (
    FLAT_PROPERTY_TYPE_NAME,
    VILLA_PROPERTY_TYPE_NAME,
    BUNGALOW_PROPERTY_TYPE_NAME,
    MAISONETTE_PROPERTY_TYPE_NANE,
    TERRACED_HOUSE_PROPERTY_TYPE_NAME,
    DETACHED_HOUSE_PROPERTY_TYPE_NAME,
    SEMI_DETACHED_HOUSE_PROPERTY_TYPE_NAME
)


class AbstractPropertyType(metaclass=abc.ABCMeta):
    def __init__(self, property_type_name):
        self._property_type_name = property_type_name

    @property
    def property_type_name(self):
        return self._property_type_name


class FlatPropertyType(AbstractPropertyType):
    def __init__(self):
        super(FlatPropertyType, self).__init__(
            property_type_name=FLAT_PROPERTY_TYPE_NAME
        )


class MaisonettePropertyType(AbstractPropertyType):
    def __init__(self):
        super(MaisonettePropertyType, self).__init__(
            property_type_name=MAISONETTE_PROPERTY_TYPE_NANE
        )


class TerracedHousePropertyType(AbstractPropertyType):
    def __init__(self):
        super(TerracedHousePropertyType, self).__init__(
            property_type_name=TERRACED_HOUSE_PROPERTY_TYPE_NAME
        )


class SemiDetachedHousePropertyType(AbstractPropertyType):
    def __init__(self):
        super(SemiDetachedHousePropertyType, self).__init__(
            property_type_name=SEMI_DETACHED_HOUSE_PROPERTY_TYPE_NAME
        )


class DetachedHousePropertyType(AbstractPropertyType):
    def __init__(self):
        super(DetachedHousePropertyType, self).__init__(
            property_type_name=DETACHED_HOUSE_PROPERTY_TYPE_NAME
        )


class BungalowPropertyType(AbstractPropertyType):
    def __init__(self):
        super(BungalowPropertyType, self).__init__(
            property_type_name=BUNGALOW_PROPERTY_TYPE_NAME
        )


class VillaPropertyType(AbstractPropertyType):
    def __init__(self):
        super(VillaPropertyType, self).__init__(
            property_type_name=VILLA_PROPERTY_TYPE_NAME
        )
