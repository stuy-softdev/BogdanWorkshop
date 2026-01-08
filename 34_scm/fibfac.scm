(define (fact n)
  (if (= n 0)
      1
      (* n (fact (- n 1)))))

(fact 7)
(fact 5)
(fact 6)
(fact 8)
(fact 9)

(define (fib n)
  (if (< n 2)
      n
      (+ (fib (- n 1)) (fib (- n 2)))))

(fib 7)
(fib 5)
(fib 6)
(fib 8)
(fib 9)
