import payroll as pr

menu = "PAYROLL\n\n\nMenu:\n1-Add a worker\n2-Remove a Worker\n\n E-Exit\n"
payroll = pr.Payroll()
opt = "start"

while opt.upper() != "E":
    print(menu)
    opt = input("Insert your desired operation:")
    if opt == 1:
        name = input("insert name:")
        address = input("insert address:")
        w_type = input("insert worker type: HOURLY, MONTHLY, COMMISSIONED")

        payroll.add(name, address, w_type)
    elif opt == 2:
        target = input("insert worker id")
        payroll.remove(int(target))
    input("press enter to continue")
