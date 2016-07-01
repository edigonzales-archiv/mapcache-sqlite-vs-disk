# -*- coding: utf-8 -*- 
import matplotlib
matplotlib.use( "agg" )
import matplotlib.pyplot as plt
import pylab


t11 = [1, 2, 3, 4, 5, 6, 7]
t12 = [1, 2, 4, 8, 16, 32, 64]

# CWM (req/s)
#filename = "cwm_req_per_sec"
#title = "Cadastral Web Map"
#disk = [61.9, 120.0, 185.2, 192.4, 161.9, 166.0, 166.1]
#sqlite = [59.9, 118.2, 192.3, 201.8, 181.8, 181.5, 184.9]

# CWM (max response time)
#filename = "cwm_max_resp_time"
#title = "Cadastral Web Map"
#disk = [0.1, 0.1, 0.1, 0.3, 1.0, 2.8, 4.7]
#sqlite = [0.1, 0.1, 0.1, 0.2, 0.8, 2.8, 3.3]

# CWM (req/s)
filename = "cwm_req_per_sec_forward_direct"
title = "Cadastral Web Map"
forward = [4.7, 9.7, 17.6, 22.8, 23.2, 23.1, 22.8]
direct = [12.8, 26.2, 48.4, 49.5, 47.9, 48.9, 48.5]

# CWM (max response time)
#filename = "cwm_max_resp_time_forward_direct"
#title = "Cadastral Web Map"
#forward = [3.8, 3.7, 3.7, 4.0, 5.1, 11.0, 38.0]
#direct = [0.5, 0.5, 0.5, 12.1, 22.2, 58.1, 64.1]

# Orthofoto (average)
#filename = "ortho_resampling_req_per_sec"
#title = "Orthofoto (average)"
#mapserver = [4.4, 8.3, 14.9, 16.1, 15.9, 16.0, 16.0]
#mapserver_fcgi = [4.9, 9.7, 17.4, 18.1, 17.9, 18.2, 18.4]
#qgisserver = [6.3, 12.4, 22.3, 23.2, 23.1, 23.0, 23.2]

# Orthofoto (average / max_resp_time)
#filename = "ortho_resampling_max_resp_time"
#title = "Orthofoto (average)"
#mapserver = [4.8, 4.8, 5.2, 10.5, 20.9, 42.1, 84.5]
#mapserver_fcgi = [4.6, 4.7, 5.0, 10.0, 58.5, 64.1, 65.8]
#qgisserver = [0.8, 1.4, 1.6, 2.8, 25.3, 47.1, 64.1]

plt.plot(t11, forward,  marker='s', color='b', label='forward', linewidth='2')
plt.plot(t11, direct, marker='o', color='y', label='direct', linewidth='2')

plt.xlabel('N Requests')
plt.ylabel('Throughput (Req/s)')
#plt.ylabel('Max response time (s)')
plt.title(title)
plt.legend(bbox_to_anchor=(0.02, 0.98), loc=2, borderaxespad=0.)

plt.xticks( [1, 2, 3, 4, 5, 6, 7],  t12 )
#plt.ylim([0, 210])
plt.ylim([0, 50])

plt.grid(b=True, which='major', linestyle='dotted') 

plt.savefig('./'+filename+'.png', dpi=100)
