; Tests the ADDi instruction


; MAIN
    LDI R0, 0xF         ;Load 15 into R0
    ADDi R0, 0x1       ; Add 1
    PRN R0
    HLT