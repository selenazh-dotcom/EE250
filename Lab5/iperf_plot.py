# Selena Zhang 2575286626

import csv
import pandas as pd
import plotly.express as px
import numpy as np
import subprocess
import csv
from io import StringIO
import plotly.io as pio


# pio.get_chrome()

DISTANCE = [2,4,6,8,10]

for d in DISTANCE:

  tcp_out = subprocess.check_output(f'tail -n 5 iperf_tcp_{d}m.csv', shell=True)
  tcp_mbps = list(csv.reader(StringIO(tcp_out.decode())))
  # print(tcp_mbps[1][1:6])

  udp_out = subprocess.check_output(f'tail -n 5 iperf_udp_{d}m.csv', shell=True)
  udp_mbps = list(csv.reader(StringIO(udp_out.decode())))
  # print(udp_mbps[1][1:6])

  throughput = tcp_mbps[1][1:6] + udp_mbps[1][1:6]
  throughput = list(map(float, throughput))
  print(throughput)
  runs = [1,2,3,4,5,1,2,3,4,5]
  # print(runs)
  type = ["TCP","TCP","TCP","TCP","TCP","UDP","UDP","UDP","UDP","UDP"]
  # print(type)
  df = pd.DataFrame(dict(
         Throughput = throughput,
         RunNumber = runs,
         Type = type))
  df = df.sort_values(by="RunNumber")
  fig = px.line(df, x="RunNumber", y="Throughput",color="Type", title=f'Throughput at {d}m')
  fig.show()
  # fig.write_image(f'Throughput_{d}m.png')
