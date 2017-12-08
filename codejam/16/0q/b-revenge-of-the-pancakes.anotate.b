[ https://www.nayuki.io/page/brainfuck-interpreter-javascript ]

cell design
===========

    (case left) (case no) (tmp1) (tmp2) (answer) (prev) (next) (flag/last) (tmps/garbage)


read number into (case left)
============================
[-]>[-]+[[-]>[-],[+[-----------[>[-]++++++[<------>-]
<--<<[->>++++++++++<<]>>[-<<+>>]<+>]]]<]<


begin test case loop
====================
[
    initial each test case by clear and init value
    ==============================================
    > +                 inc (case no)
    >>> [-]             clear (answer)
    > ,                 read char into (prev)
    >> [-] +            set (flag) to true


    read input loop
    ===============
    [
        < ,                 read char into (next)


        if else on value of (next) equal to new line or not
        ===================================================
        ---- ---- --        convert (next) to zero if newline
        <<< [-]
        < [-]
        >>>> [
            <<< +
            < +
            >>>> -
        ]
        <<< [
            >>> +
            <<< -
        ] +
        < [                 if (next) is not new line then
            >>>>
            ++++ ++++ ++        set (next) back to read char
            <<< -
            < [-]
        ]
        > [                 else
            >>>
            ++++ ++++ ++++
            ++++ ++++ ++++
            ++++ ++++ ++++
            ++++ +++            set (next) to plus sign
            > [-]               set (flag) as false
            <<<< -
        ]


        move (next) to (prev) then test neq both vars then store res in (next)
        ======================================================================
        [-]
        < [-]
        >>> [
            <<< +
            >>> -
        ]
        > [
            <<< +
            < -
            >>>> -
        ]
        <<< [
            >> +
            << -
        ]
        < [
            >>>> +
            <<<< [-]
        ]


        if (next) that repr (prev) neq (next) then inc (anwer)
        ======================================================
        >>>> [
            << +
            >> [-]
        ]


        if (flag) then loop read input again
        ====================================
        >
    ]


    output case indicator text
    ==========================
    ++++ ++++ ++++
    ++++ ++++ ++++
    ++++ ++++ ++++
    ++++ ++++ ++++
    ++++ ++++ ++++
    ++++ +++
    .
    ++++ ++++ ++++
    ++++ ++++ ++++
    ++++ ++
    .
    ++++ ++++ ++++
    ++++ ++
    .
    ---- ---- ----
    --
    .
    ---- ---- ----
    ---- ---- ----
    ---- ---- ----
    ---- ---- ----
    ---- ---- ----
    ---- ---- -
    .
    +++
    .


    copy (case no) to (last) then print number from (last)
    ======================================================
    [-]
    <<<< < [-]
    < [
        > +
        >>>> > +
        <<<< << -
    ]
    > [
        < +
        > -
    ]
    >>>> >
    [>>+>+<<<-]>>>[<<<+>>>-]<<+>[<->[>++++++++++<[->-[>+>>]>[+[-<+>]>+>>]<<<<<]>[-]
    ++++++++[<++++++>-]>[<<+>>-]>[<<+>>-]<<]>]<[->>++++++++[<++++++>-]]<[.[-]<]<
    [-]


    output separator
    ================
    ++++ ++++ ++++
    ++++ ++++ ++++
    ++++ ++++ ++++
    ++++ ++++ ++++
    ++++ ++++ ++
    .
    ---- ---- ----
    ---- ---- ----
    --
    .


    move (answer) to (last) then print number from (last)
    =====================================================
    [-]
    <<< [
        >>> +
        <<< -
    ]
    >>>
    [>>+>+<<<-]>>>[<<<+>>>-]<<+>[<->[>++++++++++<[->-[>+>>]>[+[-<+>]>+>>]<<<<<]>[-]
    ++++++++[<++++++>-]>[<<+>>-]>[<<+>>-]<<]>]<[->>++++++++[<++++++>-]]<[.[-]<]<
    [-]


    output newline
    ==============
    ++++ ++++ ++
    .
    [-]


    halt if no (case left)
    ======================
    <<<< <<< -             dcr (case left)
]