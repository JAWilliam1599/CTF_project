; (c) kcbowhunter - do not upload challenge source or solutions to any website or github

[bits 64]

global _PrintString
global _StringLength

section .text

; rax is the address of the string to write to stdout
; output - write string to stdout
_PrintString:
    push rax       ; note that rax is pushed twice
    push rdx
    push rcx
    push rbx
    push rax        ; save rax on the stack
    xor  rbx, rbx   ; rbx is the counter for the string length
    xor  rcx, rcx
_printStringLoop:
    inc rax
    inc rbx
    mov cl, [rax]
    cmp cl, 0h
    jne _printStringLoop

_PrintString2:
    ; system call to write to stdout
    mov rax, 1      ; sys_write system call
    mov rdi, 1      ; stdout (write to screen)
    pop rsi         ; memory location of string to write, pop rax off the stack directly to rsi
    mov rdx, rbx    ; number of characters in string to write
    syscall

    pop rbx
    pop rcx
    pop rdx
    pop rax
    ret
;   end _printString subroutine


; determine the length of the string pointed to in rax
; return the size in rbx
_StringLength:
    push rcx
    push rax        ; save rax on the stack
    xor  rbx, rbx   ; rbx is the counter for the string length
_StringLengthLoop:
    inc rax
    inc rbx
    mov cl, [rax]
    cmp cl, 0h
    jne _StringLengthLoop
    pop rax
    pop rcx
    ret

