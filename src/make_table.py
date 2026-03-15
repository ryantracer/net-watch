import libs

def make_device_table(devices):
    try:
        df = libs.pandas.DataFrame(devices)
        dftrsp = df.transpose()
        dftrsp.columns = ['IP', 'MAC']

        w1, w2 = 20, 20
        print(f"{dftrsp.columns[0]:<{w1}} {dftrsp.columns[1]:<{w2}}")
        print("-" * (w1 + w2 + 2))
        for ip, mac in dftrsp.values:
            print(f"{ip:<{w1}} {mac:<{w2}}")
    except Exception as e:
        print(f'[!] Error [!]\n{e}')
