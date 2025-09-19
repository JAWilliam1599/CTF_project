; (c) kcbowhunter - do not upload challenge source or solutions to any website or github
[bits 64]

extern _PrintString
extern _StringLength
extern _Usage

section .data
    welcome     db "Hello CTFlearn.com Raspberry Reversing Challenge by kcbowhunter",0ah,0h
    badflag     db "Sorry dude bad flag for you :-(",0ah,0h
    alldone     db "All Done!",0ah,0h
    toolong     db "Your flag is too long dude!",0ah, 0h
    tooshort    db "Your flag is too short bruh!", 0ah, 0h
    congrats    db "Congrats!! You found the flag!!", 0ah, 0h
    falseflag   db "CTFlearn{Raspberry_Pie!}", 0ah, 0h
    badchar     db "Bad Character: ", 0h
    newline     db 0ah,0h
    keeptrying  db "Keep Trying!! Don't give up!! (The Ascii Table is your friend)", 0ah, 0h

section .bss
    buffer resb 64


section .text
    global _start

_start:
    mov r10, 0x00   ; return code
    mov rax, welcome
    call _PrintString
    mov rax, newline
    call _PrintString

_CheckArgs:
    pop r8  ; pop the number of arguments to r8
    cmp r8, 1
    jne _Step1
    call _Usage
    mov rax, newline

    jmp _AllDone

_Step1:
    mov rax, [rsp+8]    ; user flag from argument stack
    mov r8, rax         ; cache the user flag here

    call _StringLength
    cmp rbx, 32
    ja _TooLong

    xor rcx, rcx
; C
_FirstLetter:
    xor rbx, rbx
    mov bl, [r8]
    cmp bl, 67
    jne _BadChar

    call _PrintChar

; T
_SecondLetter:
    inc rcx
    xor rbx, rbx
    mov bl, [r8+1]

    cmp bl, 0h
    je _TooShort

    cmp bl, 0x54
    jne _BadChar

    call _PrintChar

; F
_ThirdLetter:
    inc rcx
    xor rbx, rbx
    mov bl, [r8+2]

    cmp bl, 0h
    je _TooShort

    cmp bl, 46h
    jne _BadChar

    call _PrintChar

; l
_FourthLetter:
    inc rcx
    xor rbx, rbx
    mov bl, byte [r8+3]

    cmp bl, 0h
    je _TooShort

    add rbx, 0xab
    cmp rbx, 0x0117
    mov bl, byte [r8+3]
    jne _BadChar

    mov bl, [r8+3]
    call _PrintChar

; e
_FifthLetter:
    inc rcx
    xor rbx, rbx
    mov bl, byte [r8+4]

    cmp bl, 0h
    je _TooShort

    cmp rbx, 0x65

    jne _BadChar

;    mov bl, [r8+4]
    call _PrintChar

; a
_SixthLetter:
    inc rcx
    xor rbx, rbx
    mov bl, byte [r8+5]

    cmp bl, 0h
    je _TooShort

    xor rbx, 0xab
    cmp rbx, 0xca
    mov bl, byte [r8+5]
    jne _BadChar

    call _PrintChar

; r
_SeventhLetter:
    inc rcx
    xor rdx, rdx
    xor rbx, rbx
    xor rax, rax
    mov al, byte [r8+6]

    cmp al, 0h
    je _TooShort

    mov rbx, 0xbaadf00d
    mul rbx
    mov rbx, rax
    mov rax, 0x532174e5ca
    cmp rax, rbx
    mov bl, byte [r8+6]
    jne _BadChar

    call _PrintChar

; n
_EighthLetter:
    inc rcx
    xor rdx, rdx
    xor rbx, rbx
    xor rax, rax
    mov al, byte [r8+7]

    cmp al, 0h
    je _TooShort

    mov bl, 0x03
    div rbx
    mov bl, byte [r8+7]

    cmp rax, 36
    jne _BadChar

    cmp rdx, 2
    jne _BadChar

    call _PrintChar

; {
_NinthLetter:
    inc rcx
    xor rax, rax
    xor rbx, rbx
    xor rdx, rdx
    mov bl, byte [r8+8]

    cmp bl, 0h
    je _TooShort

    cmp bl, 7bh
    jne _BadChar

    call _PrintChar

; +
_TenthLetter:
    inc rcx
    xor rax, rax
    xor rbx, rbx

    mov al, byte [r8+9]
    cmp al, 0h
    je _TooShort

    cmp al, 2bh
    mov bl, byte [r8+9]
    jne _BadChar

    call _PrintChar

; F
_EleventhLetter:
    inc rcx
    xor rax, rax
    xor rbx, rbx

    mov al, byte [r8+10]
    cmp al, 0h
    je _TooShort

    xor al, 0xcb
    cmp al, 0x8d

    mov bl, byte [r8+10]
    jne _BadChar

    call _PrintChar

; r
_TwelfeLetter:
    inc rcx
    xor rax, rax
    xor rbx, rbx

    mov al, byte [r8+11]
    cmp al, 0h
    je _TooShort

    mov bl, byte [r8+11]
    add rax, 0x22
    cmp rax, 0x94
    jne _BadChar

    call _PrintChar

; u
_ThirteenthLetter:
    inc rcx
    xor rax, rax
    xor rbx, rbx

    mov al, byte [r8+12]
    cmp al, 0h
    je _TooShort

    mov bl, byte [r8+12]
    sub rax, 0x22
    cmp rax, 0x53
    jne _BadChar

    call _PrintChar

; i
_FourteenthLetter:
    inc rcx
    xor rax, rax
    xor rbx, rbx

    mov al, byte [r8+13]
    cmp al, 0h
    je _TooShort

    mov rbx, 0x15
    mul rbx
    cmp rax, 0x089d

    mov bl, byte [r8+13]
    jne _BadChar

    call _PrintChar

; t
_FifthteenthLetter:
    inc rcx
    xor rax, rax
    xor rbx, rbx
    xor rdx, rdx

    mov al, byte [r8+14]
    cmp al, 0h
    je _TooShort

    mov rbx, 0x15
    div rbx
    cmp rax, 0x05

    mov bl, byte [r8+14]
    jne _BadChar

    cmp rdx, 11
    jne _BadChar

    call _PrintChar

; 1
_SixteenthLetter:
    inc rcx
    xor rax, rax
    xor rbx, rbx
    xor rdx, rdx

    mov al, byte [r8+15]
    cmp al, 0h
    je _TooShort

    mov bl, byte [r8+15]
    shl rax, 1
    cmp rax, 62h

    jne _BadChar

    call _PrintChar

; 2
_SeventeenthLetter:
    inc rcx
    xor rax, rax
    xor rbx, rbx
    xor rdx, rdx

    mov bl, byte [r8+16]
    cmp bl, 0h
    je _TooShort

    cmp bl, 50
    jne _BadChar
    call _PrintChar

; 3
_EighteenthLetter:
    inc rcx
    xor rax, rax
    xor rbx, rbx
    xor rdx, rdx

    mov al, byte [r8+17]
    cmp al, 0h
    je _TooShort

    mov bl, byte [r8+17]
    shl rax, 0x04
    cmp rax, 0x0330
    jne _BadChar
    call _PrintChar

; }
_NineteenthLetter:
    inc rcx
    xor rax, rax
    xor rbx, rbx
    xor rdx, rdx

    mov al, byte [r8+18]
    cmp al, 0h
    je _TooShort

    mov bl, byte [r8+18]
    cmp rax, 0x7d
    jne _BadChar
    call _PrintChar

;   check for null byte in string
    mov al, byte [r8+19]
    cmp al, 0h
    jne _TooLong

    mov rax, congrats
    call _PrintString

    mov rax, r8
    call _PrintString

    mov rax, newline
    call _PrintString

    jmp _AllDone

_PrintChar:
    mov byte [buffer], bl
    mov byte [buffer+1], 0ah
    mov byte [buffer+2], 0h
    mov rax, buffer
    call _PrintString
    ret

_BadChar:
    mov rax, badchar
    call _PrintString

    mov byte [buffer], bl
    mov byte [buffer+1], 0h
    mov rax, buffer
    call _PrintString
    mov rax, newline
    call _PrintString

    mov rax, keeptrying
    call _PrintString

    mov rax, newline
    call _PrintString

    jmp _AllDone2

_TooLong:
    mov rax, toolong
    call _PrintString
    mov rax, newline
    call _PrintString

    jmp _AllDone

_TooShort:
    mov rax, tooshort
    call _PrintString
    mov rax, newline
    call _PrintString

    jmp _AllDone

_AllDone:
_AllDone2:
    mov rax, alldone
    call _PrintString

    mov rax, 60     ; exit system call
    mov rdi, r10    ; return code
    syscall
