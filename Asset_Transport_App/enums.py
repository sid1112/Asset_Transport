from enum import Enum


class AssetType(Enum):
    LAPTOP = "LAPTOP"
    TRAVEL_BAG = "TRAVEL_BAG"
    PACKAGE = "PACKAGE"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class AssetSensitivity(Enum):
    HIGHLY_SENSITIVE = "HIGHLY_SENSITIVE"
    SENSITIVE = "SENSITIVE"
    NORMAL = "NORMAL"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class RequestStatus(Enum):
    CONFIRM = "CONFIRM"
    PENDING = "PENDING"
    EXPIRED = "EXPIRED"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class TravelMedium(Enum):
    BUS = "BUS"
    CAR = "CAR"
    TRAIN = "TRAIN"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class MatchedRequestStatus(Enum):
    APPLIED = "APPLIED"
    NOTAPPLIED = "NOTAPPLIED"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)
