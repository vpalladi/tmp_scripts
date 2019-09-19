#!/usr/bin/python

import uhal


uhal.setLogLevelTo( uhal.LogLevel.ERROR )

manager = uhal.ConnectionManager("file:///home/cmx/kadamidi_tmp/28Gbps_test/28Gbps_test/28Gbps_connections.xml")

# Connection file

X0      = manager.getDevice("ku15p_1")
X1      = manager.getDevice("ku15p_2")

X = [X0, X1]

# Grab the device's URI
#X0_uri = X0.uri()
#X1_uri = X1.uri()


for i,x in enumerate(X) :
    for q in range(10,18) :
        print ('FPGA_',i,':')
        
        x.getNode ( "datapath.ctrl.quad_sel" ).write(q)
        x.getNode ( "datapath.region.mgt.rw_regs.ch0.control.loopback" ).write(2) 
        x.getNode ( "datapath.region.mgt.rw_regs.ch1.control.loopback" ).write(2) 
        x.getNode ( "datapath.region.mgt.rw_regs.ch2.control.loopback" ).write(2) 
        x.getNode ( "datapath.region.mgt.rw_regs.ch3.control.loopback" ).write(2) 
        x.dispatch()

        _loopback = x.getNode ( "datapath.region.mgt.rw_regs.ch0.control.loopback"  ).read()
        x.dispatch()
        
        # if _loopback == 0:
        #     print("Loopback On.")
        # else :
        #     print("Error setting loopback On.")

