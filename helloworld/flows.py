from viewflow import flow
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from viewflow import frontend

from .models import LeaveProcess

@frontend.register
class LeaveWorkflow(Flow):
    process_class = LeaveProcess

    start = (
        flow.Start(
            CreateProcessView,
            fields=["employee_name", "leave_type", "start_date", "end_date"]
        ).Permission(
            auto_create=True
        ).Next(this.approve)
    )

    approve = (
        flow.View(
            UpdateProcessView,
            fields=["approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_approve)
    )

    check_approve = (
        flow.If(lambda activation: activation.process.approved)
        .Then(this.send)
        .Else(this.end)
    )

    send = (
        flow.Handler(
            this.send_leave_request
        ).Next(this.end)
    )

    end = flow.End()

    def send_leave_request(self, activation):
        print(str(activation.process))