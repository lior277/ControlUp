class CustomAssert:
    @staticmethod
    def assert_all(*assertions):
        errors = []

        for i, assertion in enumerate(assertions):
            try:
                assertion()
            except AssertionError as e:
                errors.append(f"Assertion {i + 1} failed: {str(e)}")

        if errors:
            raise AssertionError("\n".join(errors))
