from plan import basic_plan, standard_plan, premium_plan, Plan

plan_employee = Plan(
    can_stream= True,
    can_download= True,
    has_sd = True,
    has_hd= True,
    has_uhd=False,
    num_devices=2,
    content="Basic Plan + Sports",
    price= 0,
    plan_name="Standard Plan",
    level = 2
)

print(plan_employee.price)
print(plan_employee.plan_name)