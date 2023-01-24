from tabulate import tabulate
from dataclasses import dataclass

@dataclass
class Plan:
    can_stream: bool
    can_download: bool
    has_sd: bool
    has_hd:bool
    has_uhd:bool
    num_devices:int
    content:str
    price:int
    plan_name:str
    level:int

    def check_plan(self):
        data = [
            ["Service",self.plan_name],
            ["Can stream", u'\u2713' if self.can_stream else "-"],
            ["Can download", u'\u2713'if self.can_download else "-"],
            ["Has SD", u'\u2713' if self.has_sd else "-" ],
            ["Has HD", u'\u2713' if self.has_hd else "-" ],
            ["Has UHD", u'\u2713' if self.has_uhd else "-" ],
            ["Number of device", self.num_devices],
            ["Available content", self.content],
            ["Price", f"Rp. {self.price:,}"],
        ]

        print(tabulate(data, headers="firstrow"))

basic_plan = Plan(
    can_stream= True,
    can_download= True,
    has_sd = True,
    has_hd=False,
    has_uhd=False,
    num_devices=1,
    content="3rd party Movie only",
    price= 120_000,
    plan_name="Basic Plan",
    level = 1
) 

standard_plan = Plan(
    can_stream= True,
    can_download= True,
    has_sd = True,
    has_hd=True,
    has_uhd=False,
    num_devices=2,
    content="Basic Plan + Sports",
    price= 160_000,
    plan_name="Standard Plan",
    level = 2
) 

premium_plan = Plan(
    can_stream= True,
    can_download= True,
    has_sd = True,
    has_hd=True,
    has_uhd=True,
    num_devices=1,
    content="Basic Plan + Standard Plan + PacFlix Original",
    price= 200_000,
    plan_name="Premium Plan",
    level = 3
) 
