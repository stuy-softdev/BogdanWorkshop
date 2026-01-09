//Team RightMouseButtonS :: Sean, Bogdan
//SoftDev pd5
//K35 - Basic functions in JavaScript
//2026-01-09f

//JavaScript implementations of recursive Scheme functions

//factorial:

//<your team's fact(n) implementation>
function fac(n)
{
    if (n == 0)
        return 1;
    else
        return (n * fac(n - 1));
}
//TEST CALLS
// (writing here beforehand will facilitate EZer copy/pasting into dev console now and later...)
(fac 0);
(fac 3);
(fac 1);
(fac 5);
(fac 20);

//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>

function fib(n)
{
    if (n == 0)
        return 0;
    else if (n <= 2)
        return 1;
    else
        return (fib(n - 1) + fib(n - 2));
}

//TEST CALLS
// (writing here beforehand will facilitate EZer copy/pasting into dev console now and later...)

(fib 0);
(fib 3);
(fib 4);
(fib 6);
(fib 20);

//=================================================================