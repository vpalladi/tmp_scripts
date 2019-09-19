#!/usr/bin/python
                                                                                
import uhal
import time
uhal.setLogLevelTo( uhal.LogLevel.ERROR )

# Connection file
manager = uhal.ConnectionManager("file:///home/cmx/vpalladi_utils/28Gbps_test/28Gbps_connections.xml")

X0      = manager.getDevice("ku15p_1")
X1      = manager.getDevice("ku15p_2")

dev = [X0, X1]

for d in dev :

    for q in range(10,18):
        d.getNode ( "datapath.ctrl.quad_sel" ).write(q)
        d.dispatch();
    
        for i in range(0,4) :

            d.getNode ( "datapath.region.mgt.rw_regs.ch"+str(i)+".control.rx_polarity" ).write(1)
            d.dispatch();



        print("RX Polarity inverted ", str(i), q )
        time.sleep(0.1)

 

