; (c) kcbowhunter - do not upload to any website
[bits 64]

extern _PrintString

global _Usage
global _Sum8Bytes
global _HexToString
global _PrintHexNumber

section .data
    usage1   db "Usage: Raspberry CTFlearn{kernel}",0ah,0h
    usage2   db "       where you need to find 'kernel' to solve the challenge",0ah,0h
    newline  db 0ah, 0h
    hexchars db "0123456789abcdef", 0h

section .bss
    hexbuffer resb 24
    flag000 resq 1

section .text

_Usage:
    mov rax, usage1
    call _PrintString
    mov rax, usage2
    call _PrintString

    ret

; print a hex number with a new line
_PrintHexNumber:
    push rax
    call _HexToString
    call _PrintString
    mov rax, newline
    call _PrintString
    pop rax
    ret

; Convert the rax value a string
; Return the pointer to the string in rax
_HexToString:

   cmp rax, 0h
   jne _HexToStringNonZero
   mov byte [hexbuffer],   '0'
   mov byte [hexbuffer+1], 'x'
   mov byte [hexbuffer+2], '0'
   mov byte [hexbuffer+3], '0'
   mov byte [hexbuffer+4], 0h
   mov rax, hexbuffer
   ret

_HexToStringNonZero:
    push rbx
    push rcx
    push rdx
    push r8
    push r9
    push r10

    xor rbx, rbx
    xor rcx, rcx
    xor rdx, rdx
    xor r8, r8
    xor r9, r9
    xor r10, r10

    mov rbx, rax
    mov rax, hexbuffer  ; so you can watch the string in gdb
    bswap rbx           ; Intel is little endian
_HexToStringLabel1:
    mov rdx, rbx        ; rdx holds the byte to process
    and rdx, 0xff
    shr rbx, 8
    cmp rdx, 0h
    je _HexToStringLabel1

    mov byte [hexbuffer],   '0'
    mov byte [hexbuffer+1], 'x'
    mov rcx, 2h

_HexToStringLabel2:
    mov r8, rdx
    shr rdx, 4

    lea r11, [hexchars]
    lea r9, [r11+rdx]
;    lea r9,  [hexchars+rdx]
    mov r10b, byte [r9]

    lea r11, [hexbuffer]
    mov byte [r11+rcx], r10b
;    mov byte [hexbuffer+rcx], r10b
    inc rcx

    mov rdx, r8
    and rdx, 0x0f
    lea r11, [hexchars]
    lea r9, [r11+rdx]
;    lea r9, [hexchars+rdx]
    mov r10b,  byte [r9]

    lea r11, [hexbuffer]
    mov byte [r11+rcx], r10b
;    mov byte [hexbuffer+rcx], r10b
    inc rcx

    lea r11, [hexbuffer]
    mov byte [r11+rcx], 0h
;    mov byte [hexbuffer+rcx], 0h

    mov rax, hexbuffer
_HexToStringLabel3:

    cmp rbx, 0h
    je _HexToStringAllDone

    mov rdx, rbx
    and rdx, 0xff
    shr rbx, 8
    jmp _HexToStringLabel2

_HexToStringAllDone:

    pop r10
    pop r9
    pop r8
    pop rdx
    pop rcx
    pop rbx

    ret

; 64 bit int in rax
; sum the value of each byte
; return the sum in rax
_Sum8Bytes:
    push rbx
    push rcx
    push rdx
    push r8

    xor rbx, rbx    ; original number shifted
    xor rcx, rcx    ; counter to 8
    xor rdx, rdx    ; sum of bytes
    xor r8, r8      ; isolate the low byte here

    mov rbx, rax
_Sum8BytesLoop:
    mov r8, rbx
    and r8, 0xff

    add rdx, r8
    shr rbx, 8
    inc rcx
    cmp rcx, 8
    jb _Sum8BytesLoop

    mov rax, rdx

    pop r8
    pop rdx
    pop rcx
    pop rbx

    ret