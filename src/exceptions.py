class ErrorMessage:
    EVENT_NOT_FOUND = "Event with id not found."
    INVALID_BET_SUM = "Bet sum must be greater than zero."
    INVALID_EVENT_STATUS = "Cannot place a bet on a pending event"


class EventNotFoundError(Exception):
    def __init__(self):
        super().__init__(ErrorMessage.EVENT_NOT_FOUND)


class InvalidBetSumError(Exception):
    def __init__(self):
        super().__init__(ErrorMessage.INVALID_BET_SUM)


class InvalidEventStatusError(Exception):
    def __init__(self):
        super().__init__(ErrorMessage.INVALID_EVENT_STATUS)
