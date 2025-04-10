class CustomAssert:
    @staticmethod
    def assert_all(*assertions):
        """
        Executes all assertions passed to it and collects any failures.

        :param assertions: Lambda functions containing assertions
        """
        errors = []

        for i, assertion in enumerate(assertions):
            try:
                assertion()  # This calls each lambda (which contains the assertion)
            except AssertionError as e:
                errors.append(f"Assertion {i + 1} failed: {str(e)}")

        # If there are any errors, raise them all together with detailed information
        if errors:
            raise AssertionError("\n".join(errors))
