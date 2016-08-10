import abc

class IResponse(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, request):
        """
            This is the basic interface for returning the values post processing
            Use the implemented classes for returning the right type of bootstrapping by the batchly agent
            Supported implementations are:-
            * DefaultResponse
            * FileResponse
            * DbResponse

            Type: IRequest
        """
        if request is not None:
            self._id = request.id
            self._status=None
        # self._is_processing_success = True
        # self._is_duplicate = False
    def status(self):
        return self._status
    # def is_processing_success(self):
    #     return self._is_processing_success;
    
    def status(self,value):
        self._status=value
    # def is_processing_success(self, value):
    #     """
    #         Status of processing.

    #         Type: Boolean
    #     """
    #     self._is_processing_success = value

    def id(self):
        return self._id

    # def is_duplicate(self):
    #     return self._is_duplicate

    # def set_is_duplicate(self, value):
    #     """
        #     In the off chance that a request comes for reprocessing after completion,
        #     and if you maintain state externally, you can mark the request as duplicate.
        #     Ideally processing should be Idempotent. A request processed again produces the same output
        #     without any errors.

        #     Type: Boolean
        # """
        # self._is_duplicate = value
