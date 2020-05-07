; Prints a histogram


; MAIN
    LDI R0, 65          ; Load 'A' into R0
    LDI R1, 0xA0        
    ST R1, R0           ; Store 'A' into memory at 0xA0
    INC R1
    ST R1, R0           ; Store 'A' into memory at 0xA1
    INC R1
    ST R1, R0           ; Store 'A' into memory at 0xA2
    INC R1
    ST R1, R0           ; Store 'A' into memory at 0xA3
    LDI R0, 0xA0        
    PRM R0, R1          ; Print string stored in address range R0 - R1
    HLT