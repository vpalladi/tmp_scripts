#!/usr/bin/python

import uhal

uhal.setLogLevelTo( uhal.LogLevel.ERROR )

# Connection file
#manager = uhal.ConnectionManager("file:///home/cmx/kadamidi_tmp/28Gbps_test/28Gbps_test/28Gbps_connections.xml")
manager = uhal.ConnectionManager("file:///home/cmx/vpalladi_utils/28Gbps_test/28Gbps_connections.xml")

X0      = manager.getDevice("ku15p_1")
X1      = manager.getDevice("ku15p_2")

dev = [X0, X1]
#for x in (11,13,15) :

print("{:<5s} {:<4s} {:<4s} {:<8s} {:<9s} {:<13s} {:<13s} {:<20s} {:<20s} {:<17s} {:<8s}"
      .format("Quad", "Channel", "InitDone", "LinkStatus", "Link_Dw_Ltc", "Reset_tx_done", "Reset_rx_done", "Bufferbypass_tx_done", "Bufferbypass_rx_done", "Crc_channel_error", "Crc_channel_checked"))

for d in dev:
    k = -1
    for q in range(10,18):  
        
        d.getNode ( "datapath.ctrl.quad_sel" ).write(q)
        d.dispatch()
        initDone            = d.getNode ( "datapath.region.mgt.ro_regs.common.status.init_done" ).read()
        
        for i in range(0,4) :
            txrstdone           = d.getNode ( "datapath.region.mgt.ro_regs.ch"+str(i)+".status.txusrrst" ).read()
            rxrstdone           = d.getNode ( "datapath.region.mgt.ro_regs.ch"+str(i)+".status.rxusrrst" ).read()
            tx_fsm_reset_done   = d.getNode ( "datapath.region.mgt.ro_regs.ch"+str(i)+".status.tx_fsm_reset_done" ).read()
            rx_fsm_reset_done   = d.getNode ( "datapath.region.mgt.ro_regs.ch"+str(i)+".status.rx_fsm_reset_done" ).read()
            link_status         = d.getNode ( "datapath.region.mgt.ro_regs.ch"+str(i)+".status.link_status" ).read()
            link_down_latched   = d.getNode ( "datapath.region.mgt.ro_regs.ch"+str(i)+".status.link_down_latched" ).read();
            crc_error           = d.getNode ( "datapath.region.mgt.ro_regs.ch"+str(i)+".status.crc_error" ).read();
            crc_checked         = d.getNode ( "datapath.region.mgt.ro_regs.ch"+str(i)+".status.crc_checked" ).read();
            results = [ link_status, link_down_latched, txrstdone, rxrstdone, tx_fsm_reset_done, rx_fsm_reset_done, crc_error, crc_checked ]
            d.dispatch();
            k = k +1
            
            print("{:<7d} {:<10d} {:<10d} {:<10d} {:<9d} {:<13d} {:<13d} {:<20d} {:<20d} {:<17x} {:<8d}"
                  .format(q, k, initDone, link_status, link_down_latched, txrstdone, rxrstdone, tx_fsm_reset_done, rx_fsm_reset_done, crc_error, crc_checked))
