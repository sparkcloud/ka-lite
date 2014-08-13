from kalite.student_testing.models import TestLog


class CreateTestLogMixin(object):
    DEFAULTS = {
        'test': 'g3_t1',  # this must be an actual exercise
        'index': '0',
        'complete': True,
        'started': True,
        'total_number': 4,
        'total_correct': 2,
    }
    @classmethod
    def create_test_log(cls, **kwargs):
        fields = CreateTestLogMixin.DEFAULTS.copy()
        fields['user'] = kwargs.get("user")
        # allow specification of totals and total correct, otherwise use default
        fields['total_number'] = kwargs.get("total_number", fields['total_number'])
        fields['total_correct'] = kwargs.get("total_correct", fields["total_correct"])

        return TestLog.objects.create(**fields)


class StudentTestingMixins(CreateTestLogMixin):
    '''
    Toplevel class that has all the mixin methods defined above
    '''
    pass