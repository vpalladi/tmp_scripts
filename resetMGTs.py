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
        
        d.getNode ( "datapath.region.mgt.rw_regs.common.control.soft_reset" ).write(1)
        d.getNode ( "datapath.region.mgt.rw_regs.common.control.soft_reset" ).write(0)
        d.dispatch();
        
        
        
        print("Reset RX Datapath Quad", q)    
        
