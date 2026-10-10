from src.logger import logger
from pathlib import Path


class Valindation_Template:
    def __init__(self) -> None:
        self.train_total: int = 0
        self.test_total: int = 0

    # get parameters in types of validation logic funtions and can returns different types according to waht type of data need to return accornding
    # to validation logic in src/vehicale_detection_tracing/data/validation/images.py
    def checking_validationing(self, train_set_res, test_set_res, error_msg: str):
        errors_train = []
        errors_test = []

        train_valid = True
        test_valid = True

        if isinstance(train_set_res, list):
            train_valid = False
            errors_train.extend([[error_msg, train_set_res]])

        if isinstance(test_set_res, list):
            test_valid = False
            errors_test.extend([[error_msg, test_set_res]])

        length_of_train_failed = len(errors_train)
        length_of_test_failed = len(errors_test)

        if not train_valid or not test_valid:
            val_res = (
                errors_train,
                errors_test,
                length_of_train_failed,
                length_of_test_failed,
            )
            return val_res
        else:
            return True

    def logging_blank(self, val_result, type_of_validation: str):

        if isinstance(val_result, bool):
            logger.info("%s validaiton successeful", type_of_validation)

        if isinstance(val_result, tuple):
            logger.error("%s validation failled:", type_of_validation)
            failed_train, failed_test, num_failed_train, num_failed_test = val_result
            percent_failed_train = num_failed_train / self.train_total * 100
            percent_failed_test = num_failed_test / self.test_total * 100
            logger.error("Train failed: %s percent", percent_failed_train)
            logger.error("Test failed: %s percent", percent_failed_test)
            logger.error("%s train failed in: %s", type_of_validation, failed_train)
            logger.error("%s test failed in: %s", type_of_validation, failed_test)
