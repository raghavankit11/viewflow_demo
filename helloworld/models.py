from django.db import models
from viewflow.models import Process
import datetime


class LeaveProcess(Process):
    employee_name = models.CharField(max_length=150)
    leave_type = models.CharField(max_length=150)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    approved = models.BooleanField(default=False)

    @property
    def leave_days(self):
        return (self.end_date - self.start_date).days + 1

    def __str__(self):
        return f"{self.employee_name} - {self.leave_type} from {self.start_date} to {self.end_date}"
