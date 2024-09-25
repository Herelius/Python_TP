class ThresholdExceededException(Exception):
    def __init__(self, threshold: int, exec_time: int, message: str="The time threshold has been exceeded"):
        self.threshold = threshold
        self.exec_time = exec_time
        self.message = f"{message} : threshold = {threshold}, execution time = {exec_time}"
        super().__init__(self.message)

